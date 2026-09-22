package com.biupui.minios.federation;

/** Optional GraphQL boundary; schemas/models stay outside core contracts. */
public final class ApolloGraphQLProvider implements ExternalTransportAdapter {
    @Override public String id() { return "federation.graphql.apollo"; }
    @Override public boolean isAvailable() { return FederationCapabilityRegistry.classAvailable("com.apollographql.apollo.ApolloClient"); }
    @Override public String diagnosticState() { return isAvailable() ? "IMPLEMENTED; Apollo runtime present; schema/service generation optional" : "MISSING_DEPENDENCY"; }
}
