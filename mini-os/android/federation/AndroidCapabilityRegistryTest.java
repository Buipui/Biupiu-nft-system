package com.biupiu.minios.federation;

public final class AndroidCapabilityRegistryTest {
    public static void run() {
        AndroidCapabilityRegistry r = new AndroidCapabilityRegistry();
        if (!r.isUsable("aosp.mainline")) throw new AssertionError("AOSP capability missing");
        if (!r.isUsable("android.auto.projection")) throw new AssertionError("Android Auto capability missing");
        if (r.isUsable("gsm-flags-2.0")) throw new AssertionError("Unresolved capability must fail closed");
        if (r.isUsable("vector.automotive.sil-hil")) throw new AssertionError("Licensed external framework must remain adapter-only");
        if (r.isUsable("motorola.ma2.transport")) throw new AssertionError("Physical accessory must fail closed without hardware");\n        if (!r.isUsable("godot.renderingdevice")) throw new AssertionError("Godot adapter capability missing");\n        if (!r.isUsable("vulkan.android-runtime")) throw new AssertionError("Vulkan adapter capability missing");\n        if (r.isUsable("vulkan.validation")) throw new AssertionError("Validation layer presence must not be treated as runtime validation evidence");\n\n        if (new VulkanCapabilityAdapter(null).isAvailable()) {\n            throw new AssertionError("Vulkan adapter must fail closed without Android context");\n        }

        AndroidAutoTransportAdapter nullContextAdapter = new AndroidAutoTransportAdapter(null);
        if (nullContextAdapter.isAvailable()) throw new AssertionError("Android Auto adapter must not claim live availability");
    }
}
