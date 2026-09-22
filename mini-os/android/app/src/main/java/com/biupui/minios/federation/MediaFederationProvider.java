package com.biupui.minios.federation;

/** Coil is primary; direct GIF/SVG libraries are specialized adapters only. */
public final class MediaFederationProvider implements ExternalTransportAdapter {
    @Override public String id() { return "media.coil"; }
    @Override public boolean isAvailable() { return FederationCapabilityRegistry.classAvailable("coil3.ImageLoader"); }
    @Override public String diagnosticState() { return isAvailable() ? "IMPLEMENTED; Coil primary; GIF/SVG extensions registered" : "MISSING_DEPENDENCY"; }
}
