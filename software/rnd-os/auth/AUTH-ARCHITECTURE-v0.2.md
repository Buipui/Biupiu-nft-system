# Authentication & Organisation Architecture v0.2

## Tenant model
Every production record belongs to an organisation. Users authenticate into an organisation and receive role-based permissions.

### Roles
- `owner` — organisation configuration and membership administration
- `admin` — operational administration
- `research_lead` — research workflow and project oversight
- `researcher` — create and update permitted research records
- `reviewer` — evidence, validation and replication review
- `viewer` — read-only access

## Security requirements before production
1. Passwordless/OIDC or another established identity provider.
2. Short-lived sessions/tokens with secure rotation.
3. Server-side authorisation on every organisation-scoped request.
4. Audit events for authentication, permission changes and sensitive data access.
5. Encryption in transit and at rest.
6. Secret management outside source control.
7. Rate limiting and abuse protection.
8. Backup, recovery and account-recovery procedures.
9. Optional MFA for privileged roles.
10. Independent security review before SaaS deployment.

## Current MVP boundary
The v0.1 local server is intentionally not presented as production authentication. The PostgreSQL schema now establishes the organisation/user boundary needed for the next implementation stage.
