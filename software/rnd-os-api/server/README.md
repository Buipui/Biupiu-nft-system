# Reference persistence/auth gate

This gate adds a SQLite persistence reference, server-side audit ledger, role enforcement and release-gate enforcement.

It is a development/reference implementation. The role header is intentionally a test adapter, not production authentication. Production deployment must replace it with OIDC/OAuth2/JWT verification and a managed database.

Run:
npm install
npm test
npm start

Production hardening remains required before public deployment.