package com.biupiu.minios.federation;

public final class AndroidCapabilityRegistryTest {
    public static void run() {
        AndroidCapabilityRegistry r = new AndroidCapabilityRegistry();
        if (!r.isUsable("aosp.mainline")) throw new AssertionError("AOSP capability missing");
        if (!r.isUsable("android.auto.projection")) throw new AssertionError("Android Auto capability missing");
        if (r.isUsable("gsm-flags-2.0")) throw new AssertionError("Unresolved capability must fail closed");
        if (r.isUsable("ax-manager.nexacore.combo")) throw new AssertionError("Unresolved external identity must fail closed");
        if (r.isUsable("vector.automotive.sil-hil")) throw new AssertionError("Licensed external framework must remain adapter-only");
        if (r.isUsable("motorola.ma1.transport")) throw new AssertionError("Physical accessory must fail closed without hardware");
        if (r.isUsable("ottocast.u2-air.transport")) throw new AssertionError("Physical accessory must fail closed without hardware");
        if (r.isUsable("snapperf.magisk.performance")) throw new AssertionError("Root performance module must remain reference-only");
        if (r.isUsable("android.dex2oat.optimizer")) throw new AssertionError("ART optimizer must remain reference-only until target/runtime validation");
    }
}
