package com.biupiu.minios.notification;

import android.app.Activity;
import android.os.Bundle;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.TextView;
import java.text.DateFormat;
import java.util.Date;

public final class NotificationHistoryActivity extends Activity {
    private LinearLayout list;
    private EditText search;

    @Override public void onCreate(Bundle b) {
        super.onCreate(b);
        NotificationStore.initialize(getApplicationContext());

        LinearLayout root = new LinearLayout(this);
        root.setOrientation(LinearLayout.VERTICAL);

        search = new EditText(this);
        search.setHint("Search notifications / keywords");
        root.addView(search);

        list = new LinearLayout(this);
        list.setOrientation(LinearLayout.VERTICAL);
        root.addView(list);

        search.setOnEditorActionListener((v, action, e) -> {
            render();
            return true;
        });

        setContentView(root);
        render();
    }

    @Override protected void onResume() {
        super.onResume();
        if (list != null) render();
    }

    private void render() {
        if (list == null || search == null) return;
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
