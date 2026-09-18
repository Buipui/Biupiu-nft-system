# Biupiu DMS Architecture v1.0

## 1. Layers

1. Identity & Access — users, organizations, sites, roles, service accounts and devices.
2. Entitlements — subscription plans, feature flags, licences and module access.
3. Core Records — sites, assets, products, orders, inventory, work orders and research records.
4. Department Modules — domain-specific workflows.
5. Site Node — local gateway/cache/event queue for physical facilities.
6. Integration Layer — versioned APIs, events, connectors and device protocols.
7. Analytics — operational metrics, reporting and approved AI services.
8. Audit — immutable-style append-only event records with retention controls.

## 2. Event flow

Device / operator action -> local validation -> Site Node event -> authenticated DMS ingestion -> authorization -> module handler -> audit event -> analytics projection.

If central connectivity fails, the Site Node queues non-critical events and synchronizes when connectivity returns. Conflict handling must be deterministic and audited.

## 3. Entitlement model

Every optional software capability has a stable feature ID. A subscription grants an entitlement set. The client may hide unavailable functions, but authoritative authorization occurs at the service boundary.

Example feature IDs:

- agri.analytics.basic
- hemp.traceability
- manufacturing.production
- manufacturing.advanced.analytics
- rnd.experiment-management
- dms.multi-site
- digital-twin.advanced
- ai.forecasting
- robotics.orchestration

Entitlement state must be versioned and auditable. Expiry must not silently disable safety, legal compliance, essential operation or previously required emergency functions.

## 4. Department isolation

Modules expose narrow contracts and should not directly depend on another department's database tables. Cross-department workflows use APIs/events. This permits individual modules to be packaged, deployed, upgraded or replaced independently.

## 5. Data classes

PUBLIC — published product information.
INTERNAL — normal operational data.
CONFIDENTIAL — commercial, customer or proprietary data.
RESTRICTED — credentials, security material, unpublished IP and sensitive R&D.

Each class receives appropriate access, storage, retention and export rules.

## 6. Future API families

/api/v1/identity
/api/v1/sites
/api/v1/devices
/api/v1/entitlements
/api/v1/subscriptions
/api/v1/assets
/api/v1/inventory
/api/v1/production
/api/v1/research
/api/v1/quality
/api/v1/maintenance
/api/v1/customer-feedback
/api/v1/digital-twins
/api/v1/events
/api/v1/audit

## 7. Repository boundary

This DMS specification defines the enterprise control plane. Department implementation packages should live under packages/dms-* or an equivalent dedicated DMS repository when the codebase is split into independently deployable repositories.
