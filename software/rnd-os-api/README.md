# Biupiu R&D OS API v1.0

Shared backend contract for Windows/PWA and Android clients.

## Purpose
This layer defines the server-side boundary for authenticated research, experiments, audit events, digital assets and controlled NFT release preparation.

## API surface
- POST /v1/auth/session
- GET /v1/research
- POST /v1/research
- GET /v1/experiments
- POST /v1/experiments
- GET /v1/assets
- POST /v1/assets
- POST /v1/assets/{id}/gate
- GET /v1/audit
- POST /v1/export

The reference implementation in this gate is an API contract and validation layer, not a production hosted service.

## Roles
VIEWER — read permitted records.
RESEARCHER — create research and experiments.
REVIEWER — review evidence and advance controlled gates.
ADMIN — manage users, policies and system configuration.

## Security
Authentication, authorization and audit persistence must be enforced server-side in production. Clients must never receive signing secrets. NFT transaction signing remains isolated from the general R&D API.
