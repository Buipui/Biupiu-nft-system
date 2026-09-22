package com.biupiu.minios.federation;

public final class AndroidCapabilityRegistryTest {
    public static void run() {
        AndroidCapabilityRegistry r = new AndroidCapabilityRegistry();
        if (!r.isUsable("aosp.mainline")) throw new AssertionError("AOSP capability missing");
        if (!r.isUsable("android.auto.projection")) throw new AssertionError("Android Auto capability missing");
        if (r.isUsable("gsm-flags-2.0")) throw new AssertionError("Unresolved capability must fail closed");
        if (r.isUsable("vector.automotive.sil-hil")) throw new AssertionError("Licensed external framework must remain adapter-only");
        if (r.isUsable("motorola.ma2.transport")) throw new AssertionError("Physical accessory must fail closed without hardware");

        AndroidAutoTransportAdapter nullContextAdapter = new AndroidAutoTransportAdapter(null);
        if (nullContextAdapter.isAvailable()) throw new AssertionError("Android Auto adapter must not claim live availability");
    }
}
