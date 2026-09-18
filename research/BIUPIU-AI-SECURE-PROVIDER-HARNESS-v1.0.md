# AI-14 — Secure Provider Harness & Mobile API Contract

## Implemented

- deterministic provider test harness with injected transport
- citation enforcement at the provider boundary
- contained provider-exception/timeout testing
- Kotlin request/response/error contract for the Android AI gateway

## Security controls

- no API credentials are stored in the repository
- tests do not contact a live model provider
- provider calls are dependency-injected so network behavior can be tested without secrets
- citation requirements can fail closed before a response is accepted

## Verification boundary

The repository now has a testable contract for provider failure and grounding behavior. This does **not** establish a live provider connection, production authentication, certificate pinning, rate limiting, billing controls, or a compiled Android network test.

## Acceptance criteria

1. Provider failure is represented explicitly.
2. Missing citations can be rejected.
3. Mobile request/response fields have a stable contract.
4. No credentials are committed.
5. Live transport remains disabled until production security controls are separately validated.

## Next gate

AI-15: authenticated gateway transport specification and CI integration.
