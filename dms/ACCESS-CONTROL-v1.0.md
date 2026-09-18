# Biupiu DMS Access Control v1.0

## Objective

Establish centralized identity, profile-based access, subscription entitlements and administrative control for the Biupiu DMS.

## Authority model

The DMS uses a centralized **Main Intelligence Control (MIC)** as the authoritative policy/control plane. Department modules must not independently grant privileges that bypass MIC.

### Administrative profiles

**SYSTEM OWNER / ROOT** — reserved for the Biupiu owner account. Full administrative access across DMS, departments, sites, customer records, entitlements, security policy, audit and R&D controls. This account must use strong authentication and preferably a separate hardware-backed recovery process.

**PLATFORM ADMIN** — operational administration with explicitly scoped permissions; cannot silently assume ROOT ownership.

**DEPARTMENT ADMIN** — administration limited to assigned department(s) and sites.

**SITE MANAGER** — operational access for assigned site(s).

**STAFF / OPERATOR** — task-specific access only.

**R&D USER** — research functions permitted by project and role.

**CUSTOMER** — access to owned products, account information, support, permitted telemetry and subscribed functions.

**CUSTOMER R&D PARTICIPANT** — customer plus separately consented research-participation functions.

**SERVICE / DEVICE** — machine-to-machine identity with no interactive human privileges.

## Rules

1. ROOT is the only unrestricted profile.
2. Every other profile uses least privilege and explicit scope.
3. Department modules request authorization from MIC for protected operations.
4. Customer access is restricted by customer identity, organization, site and owned/authorized products.
5. Subscription changes update entitlements centrally and propagate to connected products.
6. Downgrade removes optional entitlements at the effective time subject to contractual grace periods; it must not remove legally required records or safety functions.
7. Deprovisioning revokes sessions/tokens and queues device entitlement synchronization.
8. All privileged actions are audited.
9. No module may hard-code a secret master account or bypass MIC.
