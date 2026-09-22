package com.biupiu.minios.federation;

import org.junit.Test;
import static org.junit.Assert.*;

public class HtmlFederationProviderTest {
    @Test public void sanitizesExecutableMarkup() {
        HtmlFederationProvider provider = new HtmlFederationProvider();
        String result = provider.sanitize("<p>Hello</p><script>alert('x')</script>");
        assertTrue(result.contains("Hello"));
        assertFalse(result.contains("<script"));
    }

    @Test public void rejectsNullInput() {
        try {
            new HtmlFederationProvider().sanitize(null);
            fail("Expected IllegalArgumentException");
        } catch (IllegalArgumentException expected) { }
    }
}
