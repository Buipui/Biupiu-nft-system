package org.buipui.control;

import android.app.Activity;
import android.os.Bundle;
import android.widget.TextView;

public final class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle state) {
        super.onCreate(state);

        TextView status = new TextView(this);
        status.setText(
            "Buipui Native Android\n\n" +
            "Control boundary online.\n" +
            "Native core integration is staged for Cuttlefish validation.\n" +
            "Security policy remains AOSP/SELinux authoritative."
        );
        status.setPadding(48, 48, 48, 48);
        setContentView(status);
    }
}
