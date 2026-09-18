# AI-17 — Provider-Neutral Gateway Service

## Implemented

- gateway orchestration service with request IDs
- structured authentication, request-validation and provider-failure errors
- provider-neutral adapter invocation
- policy enforcement before provider execution
- Android envelope specification for success and structured errors

## Security boundary

Bearer authentication is validated before provider invocation. Provider credentials remain outside the client contract. Error payloads expose stable error codes and safe exception type names rather than secrets or provider payloads.

## Acceptance criteria

1. Every gateway request receives a request ID.
2. Authentication failures are structured.
3. Request-policy failures are structured.
4. Provider failures are contained and structured.
5. Provider implementation remains replaceable behind the adapter contract.
6. Android can represent both success and structured error responses.

## Verification status

**Implemented:** repository gateway service and tests.

**Specified:** Android envelope extension.

**Not implemented/verified:** live network transport, production token verification, real provider credentials, TLS/certificate deployment, external rate-limit service, billing integration, Android compilation and live CI execution.

## Next gate

AI-18: replay/idempotency controls, audit events and abuse-resistant gateway state.
