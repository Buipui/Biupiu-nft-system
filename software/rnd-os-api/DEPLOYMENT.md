# Biupiu R&D OS — Deployment Gate

## Target production topology

Windows/PWA + Android
        ↓
TLS / reverse proxy
        ↓
Biupiu R&D OS API
        ↓
PostgreSQL
        ↓
Audit + research + experiment + asset records

OIDC/JWT identity provider is external to the application.

## Required production configuration
- DATABASE_URL
- OIDC_ISSUER
- OIDC_AUDIENCE
- TLS termination
- secret management
- database backups
- monitoring/logging

## Deployment rule
Do not deploy with development role headers enabled. Production identity must come from verified OIDC/JWT claims plus server-side role lookup.

## Migration rule
Back up the database before migration. Apply migrations in order and record each successful migration in schema_version. Verify application health and read/write tests after migration.

## NFT boundary
The API does not hold wallet seed phrases/private keys. Blockchain signing must use a separate custody/signing boundary.