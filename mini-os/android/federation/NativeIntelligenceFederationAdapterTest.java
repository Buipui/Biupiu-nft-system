package com.biupiu.minios.federation;

public final class NativeIntelligenceFederationAdapterTest {
    public static void run() {
        NativeIntelligenceFederationAdapter a = new NativeIntelligenceFederationAdapter();
        if (a.canExecute(NativeIntelligenceFederationAdapter.Authority.PROPOSE)) throw new AssertionError("Intelligence proposal must not become execution authority");
        if (a.canPromote(NativeIntelligenceFederationAdapter.Authority.COMMIT)) throw new AssertionError("Intelligence must not self-authorise promotion");
        if (!a.acceptsEvidence(NativeIntelligenceFederationAdapter.Evidence.OBSERVED)) throw new AssertionError("Observed evidence should be accepted");
        if (a.acceptsEvidence(NativeIntelligenceFederationAdapter.Evidence.UNRESOLVED)) throw new AssertionError("Unresolved evidence must fail closed");
        if (!a.route("android.aicore").startsWith("OS_DMS_VALIDATE:")) throw new AssertionError("Federated capability must return to OS/DMS validation");
        if (!a.route(" ").startsWith("QUARANTINE:")) throw new AssertionError("Blank capability must quarantine");
    }
}
