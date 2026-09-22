package com.biupiu.minios.federation;

import android.content.Context;

public final class AndroidAutoTransportAdapter implements ExternalTransportAdapter {
    private final Context context;

    public AndroidAutoTransportAdapter(Context context) {
        this.context = context == null ? null : context.getApplicationContext();
    }

    @Override public String id() { return "android.auto.projection"; }

    @Override public boolean isAvailable() {
        // Source-level adapter presence is not live projection evidence.
        return false;
    }

    @Override public String diagnosticState() {
        return context == null
                ? "RUNTIME_REQUIRED; Android context unavailable; projection not claimed"
                : "RUNTIME_REQUIRED; Android Car APIs must confirm live projection state";
    }
}
