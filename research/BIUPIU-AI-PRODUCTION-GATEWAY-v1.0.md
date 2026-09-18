# AI-16 — Production Gateway Schema, Rate/Cost Policy & Provider Staging Boundary

## Implemented

- bounded gateway request validation
- evidence and dataset cardinality limits
- explicit provider cost-unit ceiling
- staging enablement requires authentication, secure transport, privacy review, rate limiting and cost controls
- deterministic tests for request limits and staging prerequisites

## Production boundary

The repository defines the control gate but does not enable a live external provider. A provider cannot be considered staging-ready merely because an endpoint and API-key environment variable exist.

## Required staging controls

1. Authenticated caller.
2. Secure transport.
3. Privacy/data-use review.
4. Rate limiting.
5. Cost ceiling.
6. Explicit provider enablement.
7. Grounding/citation checks.
8. Provider failure and refusal handling.

## Current status

**Implemented:** policy contract and deterministic tests.

**Not implemented/verified:** live provider transport, identity-provider verification, production secret provisioning, TLS/certificate strategy, real rate-limit service, billing integration, Android network execution, and live CI result.

## Next gate

AI-17: gateway service implementation with request IDs, structured errors and provider-neutral transport adapter.
