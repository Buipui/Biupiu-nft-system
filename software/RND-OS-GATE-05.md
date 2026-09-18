# Biupiu R&D OS — Gate 05

## Executed
Connected the Windows/PWA and Android architecture to the shared API contract.

### Web
Added `software/rnd-os-web/api-client.js` for:
- research
- experiments
- assets
- audit
- release-gate transitions

### Android
Added a typed Retrofit API contract for the same entities and operations.

### Operating model
Offline/local mode remains available for early testing. API mode is now defined as the shared-system path.

## Security
Client applications remain untrusted clients. Authentication and authorization must be server-side. No wallet secrets are placed in either client.

## Next gate
Implement authenticated sessions, role-aware client permissions, synchronization/queue handling, and automated Android/web end-to-end tests against the backend.