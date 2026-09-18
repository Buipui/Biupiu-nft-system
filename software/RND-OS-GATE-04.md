# Biupiu R&D OS — Gate 04

## Executed
Added a persistent development/reference backend layer.

### Added
- SQLite persistence for research, experiments and digital assets.
- Server-side append-only audit ledger.
- Role enforcement: VIEWER / RESEARCHER / REVIEWER / ADMIN.
- Controlled release-gate transitions.
- Admin-only final RELEASED transition.
- Automated Node integration tests for health, creation/audit and release authorization.
- Development secret/database exclusions.

### Security boundary
The role header is a test adapter only. Production authentication must replace it with OIDC/OAuth2/JWT verification, managed secrets, TLS, rate limiting and a production database.

### NFT boundary
The backend records the asset and release state; it does not hold private keys or perform production signing.

## Next gate
Connect the Android and Windows/PWA clients to the API contract, add authenticated session handling, migration/versioning, and end-to-end client/API tests.
