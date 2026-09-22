package com.biupiu.minios.federation;

public final class AndroidCapabilityRegistryTest {
    public static void run() {
        AndroidCapabilityRegistry r = new AndroidCapabilityRegistry();

        if (!r.isUsable("aosp.mainline")) {
            throw new AssertionError("AOSP capability missing");
        }
        if (r.isUsable("android.auto.projection")) {
            throw new AssertionError("Android Auto adapter must not claim live projection");
        }
        if (!r.isAdapterRegistered("android.auto.projection")) {
            throw new AssertionError("Android Auto adapter registration missing");
        }
        if (r.isUsable("gsm-flags-2.0")) {
            throw new AssertionError("Unresolved capability must fail closed");
        }
        if (r.isUsable("vector.automotive.sil-hil")) {
            throw new AssertionError("Licensed external framework must remain unavailable");
        }
        if (r.isUsable("motorola.ma2.transport")) {
            throw new AssertionError("Physical accessory must fail closed without hardware");
        }
        if (!r.isAdapterRegistered("godot.renderingdevice")) {
            throw new AssertionError("Godot adapter registration missing");
        }
        if (r.isUsable("godot.renderingdevice")) {
            throw new AssertionError("Godot adapter must not claim engine runtime availability");
        }
        if (!r.isAdapterRegistered("vulkan.android-runtime")) {
            throw new AssertionError("Vulkan adapter registration missing");
        }
        if (r.isUsable("vulkan.android-runtime")) {
            throw new AssertionError("Vulkan source adapter must not claim device support");
        }
        if (r.isUsable("vulkan.validation")) {
            throw new AssertionError("Validation layer must not be treated as production capability");
        }

        if (new VulkanCapabilityAdapter(null).isAvailable()) {
            throw new AssertionError("Vulkan adapter must fail closed without Android context");
        }

        AndroidAutoTransportAdapter nullContextAdapter = new AndroidAutoTransportAdapter(null);
        if (nullContextAdapter.isAvailable()) {
            throw new AssertionError("Android Auto adapter must not claim live availability");
        }
    }
}
