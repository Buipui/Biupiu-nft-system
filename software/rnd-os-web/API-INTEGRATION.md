# Gate 05 — Client/API integration

The web client now has a shared API adapter contract for research, experiments, assets, audit events and release gates.

The existing localStorage prototype remains available as an offline test mode. Production mode should point `BIUPIU_API_BASE` at the authenticated API origin.

## Authentication boundary
Do not put credentials, private keys or service secrets in browser code. Production authentication should use a secure session/OIDC flow and server-side authorization.

## Client modes
- Offline prototype: localStorage.
- API mode: shared Biupiu R&D OS backend.
- Future sync mode: explicit conflict-aware synchronization between local workspace and server records.
