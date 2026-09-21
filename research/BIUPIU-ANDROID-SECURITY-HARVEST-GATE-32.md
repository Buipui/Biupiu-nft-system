# BIUPIU ANDROID SECURITY HARVEST — GATE 32

Date: 21 September 2026

## Sources and integration
Official Android security guidance was cross-referenced for TLS, network security configuration, private internal storage, sandboxing and sensitive-data handling. GitHub security guidance was cross-referenced for least privilege, immutable action pinning, secrets handling and OIDC.

Integrated into the native Android shell:
- cleartext network traffic disabled by default;
- explicit network-security configuration;
- sensitive backup excluded;
- central Android security-policy boundary;
- exported department activities remain prohibited;
- runtime-session validation requires an active status and non-empty subscriber identity.

Existing architecture retained:
- Keystore/session security remains an architectural boundary;
- GitHub signing secrets remain outside source;
- authentication/authorization remains separate from UI;
- AI cannot bypass OS authorization.

## Repository/security controls
GitHub Actions should use least privilege and, where practical, full-length action SHA pinning. OIDC is preferred over long-lived cloud credentials for future cloud integrations. Android release signing remains fail-closed.

## Status
- Security harvest: IMPLEMENTED
- Android security policy: IMPLEMENTED
- Network security baseline: IMPLEMENTED
- Backup boundary: IMPLEMENTED
- Runtime-session security check: IMPLEMENTED
- Device/OEM security verification: PENDING
- Cryptographic/keystore runtime verification: PENDING
- Full GitHub workflow action-SHA audit: PENDING

## Next gate
G32-A — repository-wide security workflow audit, dependency/action pinning, Android Keystore runtime tests, and signed-build security verification.
