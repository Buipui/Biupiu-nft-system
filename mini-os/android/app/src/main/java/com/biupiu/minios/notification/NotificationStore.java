package com.biupiu.minios.notification;

import android.content.Context;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public final class NotificationStore {
    public record Item(long time, String app, String title, String text) {}
    private static final List<Item> ITEMS = Collections.synchronizedList(new ArrayList<>());

    public static void save(long time, String app, String title, String text) {
        ITEMS.add(new Item(time, app, title, text));
        if (ITEMS.size() > 5000) ITEMS.remove(0);
    }

    public static List<Item> query(String keyword, String packageName) {
        String k = keyword == null ? "" : keyword.toLowerCase();
        List<Item> out = new ArrayList<>();
        synchronized (ITEMS) {
            for (Item i : ITEMS) {
                boolean textMatch = k.isEmpty() || (i.title()+" "+i.text()).toLowerCase().contains(k);
                boolean appMatch = packageName == null || packageName.isEmpty() || i.app().equals(packageName);
                if (textMatch && appMatch) out.add(i);
            }
        }
        Collections.reverse(out);
        return out;
    }
}
