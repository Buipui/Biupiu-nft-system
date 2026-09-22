package com.biupiu.minios.notification;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Locale;

public final class NotificationStore {
    public static final class Item {
        private final long time;
        private final String app;
        private final String title;
        private final String text;

        public Item(long time, String app, String title, String text) {
            this.time = time; this.app = app; this.title = title; this.text = text;
        }
        public long time() { return time; }
        public String app() { return app; }
        public String title() { return title; }
        public String text() { return text; }
    }

    private static final List<Item> ITEMS = Collections.synchronizedList(new ArrayList<>());

    public static void save(long time, String app, String title, String text) {
        ITEMS.add(new Item(time, app, title, text));
        if (ITEMS.size() > 5000) ITEMS.remove(0);
    }

    public static List<Item> query(String keyword, String packageName) {
        String k = keyword == null ? "" : keyword.toLowerCase(Locale.ROOT);
        List<Item> out = new ArrayList<>();
        synchronized (ITEMS) {
            for (Item i : ITEMS) {
                boolean textMatch = k.isEmpty() || (i.title()+" "+i.text()).toLowerCase(Locale.ROOT).contains(k);
                boolean appMatch = packageName == null || packageName.isEmpty() || i.app().equals(packageName);
                if (textMatch && appMatch) out.add(i);
            }
        }
        Collections.reverse(out);
        return out;
    }
}
