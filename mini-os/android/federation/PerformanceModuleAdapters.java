package com.biupiu.minios.federation;

public final class PerformanceModuleAdapters {
    private PerformanceModuleAdapters() {}

    public static ExternalTransportAdapter snapPerf() {
        return fixed("snapperf.magisk.performance");
    }

    public static ExternalTransportAdapter dex2oatOptimizer() {
        return fixed("android.dex2oat.optimizer");
    }

    public static ExternalTransportAdapter axManagerNexacoreCombo() {
        return fixed("ax-manager.nexacore.combo");
    }

    private static ExternalTransportAdapter fixed(final String id) {
        return new ExternalTransportAdapter() {
            @Override public String id() { return id; }
            @Override public boolean isAvailable() { return false; }
            @Override public String diagnosticState() {
                return "REFERENCE_ONLY; external/root/platform-specific implementation is not enabled in the normal Mini OS path";
            }
        };
    }
}
