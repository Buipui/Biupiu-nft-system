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
        // Projection is an adapter boundary until Android Car APIs provide live runtime evidence.
        capabilities.put("android.auto.projection", State.ADAPTER_ONLY);
        capabilities.put("motorola.ma2.transport", State.DEVICE_REQUIRED);
        capabilities.put("aawireless.two.transport", State.DEVICE_REQUIRED);
        capabilities.put("carlinkit.2air.transport", State.DEVICE_REQUIRED);
        capabilities.put("vector.automotive.sil-hil", State.LICENSE_REVIEW);
        capabilities.put("lsposed.art-instrumentation", State.LICENSE_REVIEW);
        capabilities.put("gsm-flags-2.0", State.UNRESOLVED);
        capabilities.put("godot.renderingdevice", State.ADAPTER_ONLY);
        capabilities.put("vulkan.android-runtime", State.ADAPTER_ONLY);
        capabilities.put("vulkan.validation", State.ADAPTER_ONLY);
    }

    public Map<String, State> snapshot() {
        return Collections.unmodifiableMap(new LinkedHashMap<>(capabilities));
    }

    /** Runtime capability is usable only when the registry has positive runtime evidence. */
    public boolean isUsable(String capability) {
        return capabilities.get(capability) == State.AVAILABLE;
    }

    /** True when a native adapter/contract exists, without claiming live runtime availability. */
    public boolean isAdapterRegistered(String capability) {
        State state = capabilities.get(capability);
        return state == State.AVAILABLE || state == State.ADAPTER_ONLY;
    }

    public State stateOf(String capability) {
        State state = capabilities.get(capability);
        return state == null ? State.UNRESOLVED : state;
    }
}
