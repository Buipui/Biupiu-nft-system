package com.biupiu.minios.notification;

import android.app.Notification;
import android.service.notification.NotificationListenerService;
import android.service.notification.StatusBarNotification;

public final class BiupuiNotificationListener extends NotificationListenerService {
    @Override public void onNotificationPosted(StatusBarNotification sbn) {
        CharSequence text = sbn.getNotification().extras.getCharSequence(Notification.EXTRA_TEXT);
        String title = String.valueOf(sbn.getNotification().extras.getCharSequence(Notification.EXTRA_TITLE));
        NotificationStore.save(
            System.currentTimeMillis(),
            sbn.getPackageName(),
            title,
            text == null ? "" : text.toString());
    }
}
