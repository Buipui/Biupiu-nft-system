package com.biupiu.minios.notification;

import android.app.Notification;
import android.service.notification.NotificationListenerService;
import android.service.notification.StatusBarNotification;

public final class BiupuiNotificationListener extends NotificationListenerService {
    @Override public void onNotificationPosted(StatusBarNotification sbn) {
        if (sbn == null || sbn.getNotification() == null) return;

        NotificationStore.initialize(getApplicationContext());

        CharSequence text = sbn.getNotification().extras.getCharSequence(Notification.EXTRA_TEXT);
        CharSequence titleValue = sbn.getNotification().extras.getCharSequence(Notification.EXTRA_TITLE);
        String title = titleValue == null ? "" : titleValue.toString();

        NotificationStore.save(
                System.currentTimeMillis(),
                sbn.getPackageName(),
                title,
                text == null ? "" : text.toString());
    }
}
