package com.biupiu.minios.federation;

import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.Map;

public final class AndroidCapabilityRegistry {
    public enum State { AVAILABLE, ADAPTER_ONLY, DEVICE_REQUIRED, LICENSE_REVIEW, UNRESOLVED }

    private final Map<String, State> capabilities = new LinkedHashMap<>();

    public AndroidCapabilityRegistry() {
        capabilities.put("aosp.mainline", State.AVAILABLE);
        capabilities.put("pixel.gki.vendor-separation", State.ADAPTER_ONLY);
        capabilities.put("android.auto.projection", State.AVAILABLE);
        capabilities.put("motorola.ma2.transport", State.DEVICE_REQUIRED);
        capabilities.put("aawireless.two.transport", State.DEVICE_REQUIRED);
        capabilities.put("carlinkit.2air.transport", State.DEVICE_REQUIRED);
        capabilities.put("vector.automotive.sil-hil", State.LICENSE_REVIEW);
        capabilities.put("lsposed.art-instrumentation", State.LICENSE_REVIEW);
        capabilities.put("gsm-flags-2.0", State.UNRESOLVED);
    }

    public Map<String, State> snapshot() {
        return Collections.unmodifiableMap(capabilities);
    }

    public boolean isUsable(String capability) {
        State s = capabilities.get(capability);
        return s == State.AVAILABLE || s == State.ADAPTER_ONLY;
    }
}
