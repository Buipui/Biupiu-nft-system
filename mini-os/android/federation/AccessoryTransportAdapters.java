package com.biupiu.minios.federation;

public final class AccessoryTransportAdapters {
    private AccessoryTransportAdapters() {}

    public static ExternalTransportAdapter motorolaMA2() {
        return fixed("motorola.ma2.transport");
    }

    public static ExternalTransportAdapter aawirelessTwo() {
        return fixed("aawireless.two.transport");
    }

    public static ExternalTransportAdapter carlinkit2Air() {
        return fixed("carlinkit.2air.transport");
    }

    private static ExternalTransportAdapter fixed(final String id) {
        return new ExternalTransportAdapter() {
            @Override public String id() { return id; }
            @Override public boolean isAvailable() { return false; }
            @Override public String diagnosticState() {
                return "DEVICE_REQUIRED; accessory discovery not claimed until physical hardware is present";
            }
        };
    }
}
