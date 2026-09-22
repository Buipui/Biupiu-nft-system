package com.biupui.minios.federation;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.safety.Safelist;

/** Parses untrusted federation documents without permitting executable HTML. */
public final class HtmlFederationProvider implements ExternalTransportAdapter {
    public Document parse(String html) {
        if (html == null) throw new IllegalArgumentException("html == null");
        return Jsoup.parse(html);
    }
    public String sanitize(String html) {
        if (html == null) throw new IllegalArgumentException("html == null");
        return Jsoup.clean(html, Safelist.relaxed());
    }
    @Override public String id() { return "federation.jsoup"; }
    @Override public boolean isAvailable() { return true; }
    @Override public String diagnosticState() { return "IMPLEMENTED; parse/sanitize boundary"; }
}
