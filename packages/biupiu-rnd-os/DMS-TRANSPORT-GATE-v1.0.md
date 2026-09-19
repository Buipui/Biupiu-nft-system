# Biupiu R&D OS — DMS Transport Gate v1.0

## Gate objective
Add a safe authenticated transport contract between the R&D OS digital-twin adapter and the modular DMS control plane.

## Contract
- Authentication is represented by an opaque `accessTokenRef`; credentials are never stored in source.
- Subject and scopes are explicit.
- Twin envelopes require twin, site, asset, model, payload, provenance and idempotency references.
- DMS remains authoritative for identity, entitlement and site scope.
- The OS remains authoritative for research-model provenance and experiment state.
- Transport adapters may target HTTPS/HTTP APIs, local IPC or Site Node queues without changing the twin model.

## Synchronization
Every outbound event must be idempotent. Offline Site Node implementations should queue immutable event envelopes and replay them in order after authorization and connectivity are restored.

## Security
No access token, refresh token, private key or credential is serialized into the repository, model payload, ordinary audit log or digital-twin provenance record.

## Status
Transport contract implemented. Live authenticated DMS endpoint and Site Node connectivity remain runtime validation gates.
