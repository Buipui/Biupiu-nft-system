# API security gate

This reference API is not production-ready.

Production requirements:
1. OIDC/OAuth2 or equivalent authentication.
2. Server-side RBAC enforcement.
3. Append-only audit storage with actor, timestamp, action and target.
4. Encryption in transit and at rest.
5. CSRF protection where browser cookies are used.
6. Rate limiting and abuse controls.
7. Input/schema validation.
8. Secret management outside Git.
9. Database backups and recovery testing.
10. Separate blockchain signing service/wallet custody.
11. Security testing before public deployment.

The local/PWA clients must be treated as untrusted clients. They may request operations but cannot authoritatively approve a release.
