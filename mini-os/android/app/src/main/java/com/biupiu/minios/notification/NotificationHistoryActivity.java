package com.biupiu.minios.notification;

import android.app.Activity;
import android.os.Bundle;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.TextView;
import java.text.DateFormat;
import java.util.Date;

public final class NotificationHistoryActivity extends Activity {
    private final LinearLayout list = new LinearLayout(this);
    private final EditText search = new EditText(this);

    @Override public void onCreate(Bundle b) {
        super.onCreate(b);
        LinearLayout root = new LinearLayout(this);
        root.setOrientation(LinearLayout.VERTICAL);
        search.setHint("Search notifications / keywords");
        root.addView(search);
        root.addView(list);
        search.setOnEditorActionListener((v, action, e) -> { render(); return false; });
        setContentView(root);
        render();
    }

    private void render() {
        list.removeAllViews();
        String q = search.getText().toString();
        for (NotificationStore.Item i : NotificationStore.query(q, null)) {
            TextView row = new TextView(this);
            row.setPadding(16, 16, 16, 16);
            row.setText(DateFormat.getDateTimeInstance().format(new Date(i.time()))
                + "\n" + i.app() + "\n" + i.title() + "\n" + i.text());
            list.addView(row);
        }
    }
}
