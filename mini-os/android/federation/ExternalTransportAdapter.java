package com.biupiu.minios.federation;

public interface ExternalTransportAdapter {
    String id();
    boolean isAvailable();
    String diagnosticState();
}
