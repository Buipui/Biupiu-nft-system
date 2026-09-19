# Biupiu DMS Core Test Matrix v1.0

## Identity
- Valid login receives scoped session.
- Invalid credentials are rejected.
- MFA-required profiles cannot bypass MFA.
- Revoked sessions lose protected access.

## MIC authorization
- Unknown role is denied.
- Customer cannot access another customer's product.
- Site manager cannot cross assigned site boundary.
- Department user cannot call unrelated restricted module operations.
- ROOT can access all authorized administrative functions.

## Entitlements
- CORE receives only CORE features.
- Upgrade activates eligible features after entitlement refresh.
- Downgrade removes optional features after effective/grace period.
- Product-incompatible features remain unavailable regardless of tier.
- Safety-critical feature remains available regardless of tier.

## Tenant isolation
- Customer A cannot read Customer B records.
- Organization users cannot access unassigned sites.
- Device identity cannot impersonate another device.

## Audit
- Login, privilege changes, subscription changes and policy decisions generate correlation IDs.
- Denied requests are recorded without leaking sensitive credentials.

## Resilience
- Site Node queues approved non-critical events while offline.
- Expired cached entitlements cannot grant indefinite access.
- Reconnection reconciles events deterministically and records conflicts.

This matrix defines development gates; passing documentation alone does not constitute a security certification.
