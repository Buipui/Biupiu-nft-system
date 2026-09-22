package com.biupiu.minios.federation;

import android.content.Context;

public final class AndroidAutoTransportAdapter implements ExternalTransportAdapter {
    private final Context context;

    public AndroidAutoTransportAdapter(Context context) {
        this.context = context.getApplicationContext();
    }

    @Override public String id() { return "android.auto.projection"; }

    @Override public boolean isAvailable() {
        return context != null;
    }

    @Override public String diagnosticState() {
        return "PUBLIC_ANDROID_API_BOUNDARY; projection state must be queried through Android Car APIs";
    }
}
