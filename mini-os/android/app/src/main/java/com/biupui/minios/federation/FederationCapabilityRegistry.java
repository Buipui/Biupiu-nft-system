package com.biupui.minios.federation;

/** Provider-neutral capability probes; no third-party type leaks into core contracts. */
public final class FederationCapabilityRegistry {
    private FederationCapabilityRegistry() {}
    public static boolean classAvailable(String className) {
        try { Class.forName(className, false, FederationCapabilityRegistry.class.getClassLoader()); return true; }
        catch (ClassNotFoundException | LinkageError ignored) { return false; }
    }
    public static String diagnostic() {
        return "okhttp=" + classAvailable("okhttp3.OkHttpClient")
            + "; appauth=" + classAvailable("net.openid.appauth.AuthorizationService")
            + "; apollo=" + classAvailable("com.apollographql.apollo.ApolloClient")
            + "; coil=" + classAvailable("coil3.ImageLoader")
            + "; gif=" + classAvailable("pl.droidsonroids.gif.GifDrawable")
            + "; androidsvg=" + classAvailable("com.caverock.androidsvg.SVG")
            + "; jsoup=" + classAvailable("org.jsoup.Jsoup")
            + "; pdf=" + classAvailable("androidx.pdf.viewer.fragment.PdfViewerFragment")
            + "; lingver=" + classAvailable("com.yariksoffice.lingver.Lingver");
    }
}
