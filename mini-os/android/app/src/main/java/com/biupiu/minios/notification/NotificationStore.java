package com.biupiu.minios.notification;

import android.content.Context;
import android.content.SharedPreferences;
import android.util.Base64;

import org.json.JSONArray;
import org.json.JSONObject;

import java.nio.charset.StandardCharsets;
import java.security.KeyStore;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Locale;
import java.util.concurrent.locks.ReentrantReadWriteLock;

import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.GCMParameterSpec;
import javax.crypto.spec.SecretKeySpec;

public final class NotificationStore {
    private static final String PREFS = "biupui_notification_store";
    private static final String KEY_ALIAS = "biupui_notification_aes_gcm";
    private static final String PAYLOAD = "payload";
    private static final int MAX_ITEMS = 5000;

    private static final ReentrantReadWriteLock LOCK = new ReentrantReadWriteLock();
    private static volatile SharedPreferences preferences;

    private NotificationStore() {}

    public static void initialize(Context context) {
        if (context == null) return;
        if (preferences == null) {
            synchronized (NotificationStore.class) {
                if (preferences == null) {
                    preferences = context.getApplicationContext()
                            .getSharedPreferences(PREFS, Context.MODE_PRIVATE);
                }
            }
        }
    }

    public static final class Item {
        private final long time;
        private final String app;
        private final String title;
        private final String text;

        public Item(long time, String app, String title, String text) {
            this.time = time;
            this.app = app == null ? "" : app;
            this.title = title == null ? "" : title;
            this.text = text == null ? "" : text;
        }

        public long time() { return time; }
        public String app() { return app; }
        public String title() { return title; }
        public String text() { return text; }
    }

    public static void save(long time, String app, String title, String text) {
        LOCK.writeLock().lock();
        try {
            List<Item> items = load();
            items.add(new Item(time, app, title, text));
            while (items.size() > MAX_ITEMS) items.remove(0);
            persist(items);
        } finally {
            LOCK.writeLock().unlock();
        }
    }

    public static List<Item> query(String keyword, String packageName) {
        LOCK.readLock().lock();
        try {
            String k = keyword == null ? "" : keyword.toLowerCase(Locale.ROOT);
            List<Item> out = new ArrayList<>();
            for (Item i : load()) {
                boolean textMatch = k.isEmpty()
                        || (i.title() + " " + i.text() + " " + i.app())
                        .toLowerCase(Locale.ROOT).contains(k);
                boolean appMatch = packageName == null
                        || packageName.isEmpty()
                        || i.app().equals(packageName);
                if (textMatch && appMatch) out.add(i);
            }
            Collections.reverse(out);
            return out;
        } finally {
            LOCK.readLock().unlock();
        }
    }

    private static List<Item> load() {
        SharedPreferences prefs = preferences;
        if (prefs == null) return new ArrayList<>();

        String encoded = prefs.getString(PAYLOAD, null);
        if (encoded == null || encoded.isEmpty()) return new ArrayList<>();

        try {
            byte[] packed = Base64.decode(encoded, Base64.DEFAULT);
            if (packed.length <= 12) return new ArrayList<>();

            byte[] iv = new byte[12];
            byte[] ciphertext = new byte[packed.length - iv.length];
            System.arraycopy(packed, 0, iv, 0, iv.length);
            System.arraycopy(packed, iv.length, ciphertext, 0, ciphertext.length);

            Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding");
            cipher.init(Cipher.DECRYPT_MODE, getKey(), new GCMParameterSpec(128, iv));
            JSONArray json = new JSONArray(
                    new String(cipher.doFinal(ciphertext), StandardCharsets.UTF_8));

            List<Item> items = new ArrayList<>();
            for (int i = 0; i < json.length(); i++) {
                JSONObject o = json.optJSONObject(i);
                if (o == null) continue;
                items.add(new Item(
                        o.optLong("time", 0L),
                        o.optString("app", ""),
                        o.optString("title", ""),
                        o.optString("text", "")));
            }
            return items;
        } catch (Exception ignored) {
            // Corrupt/unreadable local state is not trusted; return an empty view.
            return new ArrayList<>();
        }
    }

    private static void persist(List<Item> items) {
        SharedPreferences prefs = preferences;
        if (prefs == null) return;

        try {
            JSONArray json = new JSONArray();
            for (Item item : items) {
                JSONObject o = new JSONObject();
                o.put("time", item.time());
                o.put("app", item.app());
                o.put("title", item.title());
                o.put("text", item.text());
                json.put(o);
            }

            byte[] plaintext = json.toString().getBytes(StandardCharsets.UTF_8);
            byte[] iv = new byte[12];
            new java.security.SecureRandom().nextBytes(iv);

            Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding");
            cipher.init(Cipher.ENCRYPT_MODE, getKey(), new GCMParameterSpec(128, iv));
            byte[] ciphertext = cipher.doFinal(plaintext);

            byte[] packed = new byte[iv.length + ciphertext.length];
            System.arraycopy(iv, 0, packed, 0, iv.length);
            System.arraycopy(ciphertext, 0, packed, iv.length, ciphertext.length);

            prefs.edit()
                    .putString(PAYLOAD, Base64.encodeToString(packed, Base64.NO_WRAP))
                    .apply();
        } catch (Exception e) {
            throw new IllegalStateException("Notification store persistence failed", e);
        }
    }

    private static SecretKey getKey() throws Exception {
        KeyStore keyStore = KeyStore.getInstance("AndroidKeyStore");
        keyStore.load(null);
        if (keyStore.containsAlias(KEY_ALIAS)) {
            KeyStore.Entry entry = keyStore.getEntry(KEY_ALIAS, null);
            if (entry instanceof KeyStore.SecretKeyEntry) {
                return ((KeyStore.SecretKeyEntry) entry).getSecretKey();
            }
        }

        KeyGenerator generator = KeyGenerator.getInstance(
                "AES", "AndroidKeyStore");
        generator.init(256);
        return generator.generateKey();
    }
}
