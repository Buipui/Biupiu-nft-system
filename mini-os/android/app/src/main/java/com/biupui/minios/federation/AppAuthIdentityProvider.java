package com.biupui.minios.federation;

/** Identity boundary; AppAuth handles OAuth2/OIDC and PKCE outside transport. */
public final class AppAuthIdentityProvider implements ExternalTransportAdapter {
    @Override public String id() { return "identity.appauth.oauth2-oidc"; }
    @Override public boolean isAvailable() { return FederationCapabilityRegistry.classAvailable("net.openid.appauth.AuthorizationService"); }
    @Override public String diagnosticState() { return isAvailable() ? "IMPLEMENTED; AppAuth present; PKCE/auth-flow configuration required" : "MISSING_DEPENDENCY"; }
}
