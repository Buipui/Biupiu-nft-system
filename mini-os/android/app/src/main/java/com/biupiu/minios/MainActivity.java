package com.biupiu.minios;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.provider.Settings;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.TextView;

public final class MainActivity extends Activity {
    @Override public void onCreate(Bundle state) {
        super.onCreate(state);
        LinearLayout root = new LinearLayout(this);
        root.setOrientation(LinearLayout.VERTICAL);
        root.setPadding(32, 32, 32, 32);

        TextView title = new TextView(this);
        title.setText("Buipui Mini OS\nNative Android control layer");
        title.setTextSize(24);
        root.addView(title);

        Button notifications = new Button(this);
        notifications.setText("Enable Notification History");
        notifications.setOnClickListener(v ->
            startActivity(new Intent("android.settings.ACTION_NOTIFICATION_LISTENER_SETTINGS")));
        root.addView(notifications);

        Button accessibility = new Button(this);
        accessibility.setText("Enable One-Hand / Gesture Service");
        accessibility.setOnClickListener(v ->
            startActivity(new Intent(Settings.ACTION_ACCESSIBILITY_SETTINGS)));
        root.addView(accessibility);

        Button notificationHistory = new Button(this);
        notificationHistory.setText("Open Buipui Notification History");
        notificationHistory.setOnClickListener(v ->
            startActivity(new Intent(this, com.biupiu.minios.notification.NotificationHistoryActivity.class)));
        root.addView(notificationHistory);

        setContentView(root);
    }
}
