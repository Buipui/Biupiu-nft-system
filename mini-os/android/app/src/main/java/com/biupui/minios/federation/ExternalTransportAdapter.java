package com.biupiu.minios.federation;

/** Common capability boundary for external federation providers. */
public interface ExternalTransportAdapter {
    String id();
    boolean isAvailable();
    String diagnosticState();
}
