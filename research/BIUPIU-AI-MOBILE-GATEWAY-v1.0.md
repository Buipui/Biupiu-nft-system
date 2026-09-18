# AI-05 — Authenticated AI/Mobile Gateway

## Objective
Create the server boundary through which the Android R&D OS communicates with the AI layer.

## Data flow
Android → HTTPS API → authentication → AI gateway → RAG/evidence services → structured response.

## Implemented foundation
- framework-neutral authenticated API contract
- development token verifier
- authorization scope for AI reads and experiment writes
- unauthorized-request test
- Android gateway client interface

## Security boundary
The development verifier is not production authentication. No production secret is stored in the Android application. Production deployment requires a proper identity provider, short-lived tokens, secure token storage, TLS/certificate policy, rate limiting, audit logging and threat modelling.

## Write policy
AI responses do not receive unrestricted repository write access. Durable changes should pass through validated R&D OS operations and audit events.

## Next gate
AI-06: mobile offline queue/synchronisation and authenticated API implementation.
