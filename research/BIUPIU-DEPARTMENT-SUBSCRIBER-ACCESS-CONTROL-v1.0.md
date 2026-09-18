# Biupiu Department Subscriber Access Control v1.0

**Status:** Architecture specification
**Date:** 18 September 2026

## Purpose

Biupiu uses one common subscriber/tenant model while restricting each subscriber workspace to the department resources it is licensed or authorised to use.

The same identity, billing/licensing, audit and security framework can therefore serve multiple specialist products without exposing unrelated research.

## Core rule

**Subscriber access is department-scoped, not repository-wide.**

A subscriber receives:
- a subscriber identity;
- an organisation/workspace;
- one or more department entitlements;
- role permissions within each entitled department;
- access only to resources whose department scope matches the entitlement.

Cross-department discovery is disabled by default. Shared/public resources may be explicitly marked as cross-department.

## Department entitlement model

`SUBSCRIBER → ORGANISATION → DEPARTMENT ENTITLEMENT → PROJECT → RESOURCE`

Example entitlements:
- `METALLURGY`
- `FARMING`

A subscriber may have one entitlement or several. The entitlement does not automatically grant access to every Biupiu department.

## Access dimensions

Every protected object should carry:

- `department_id`
- `tenant_id`
- `visibility`
- `resource_type`
- `classification`
- `owner`
- `licence`
- `created_at`
- `version`

Recommended visibility states:

`PRIVATE → TENANT → DEPARTMENT → SHARED`

The default is `TENANT`; department products should normally use `DEPARTMENT`.

## Roles

Within an entitled department:

- **Subscriber:** consume licensed resources and create permitted personal records.
- **Contributor:** create/edit department records.
- **Department Admin:** manage department workspace and users.
- **Platform Admin:** administer the platform but should not automatically receive research-content access without an explicit audit-controlled grant.

## Information firewall

A metallurgy subscriber must not receive:
- farming datasets;
- farming experiment records;
- farming sensor configurations;
- unrelated agriculture research;
- other department private/IP records.

A farming subscriber must not receive:
- metallurgy process records;
- metallurgy experiment datasets;
- furnace/forge process records;
- unrelated materials/IP records.

Search, AI retrieval, recommendations, exports and notifications must apply the same department filter. Security must be enforced server-side; hiding a menu item is not an access control.

## Shared resources

A resource can be explicitly classified `SHARED` when Biupiu intends it to be available across departments, for example:
- general safety material;
- general platform documentation;
- common account help;
- approved cross-department standards;
- deliberately published research.

Shared status must never be inferred from a user's subscription.

## Department product pattern

Each specialist product is a controlled view over the same platform architecture:

`Common Identity + Subscriber Engine + Department Data Boundary + Specialist Knowledge/Tools + Audit`

This permits separate products without duplicating the entire OS.

## Audit requirements

Record:
- login/session;
- entitlement changes;
- resource reads for protected/IP-sensitive data;
- create/update/delete;
- export/download;
- AI retrieval against protected records;
- sharing changes;
- administrator access grants.

## Example policy

```text
if user.tenant != resource.tenant:
    DENY

if resource.visibility == DEPARTMENT:
    if resource.department not in user.active_entitlements:
        DENY

if resource.visibility == TENANT:
    allow when tenant matches

if resource.visibility == SHARED:
    allow according to publication/licence rules
```

The production implementation must perform these checks on the server/API and database layer, with tests for cross-tenant and cross-department leakage.

## Product registry

Initial specialist products:

| Product | Department scope | Primary users |
|---|---|---|
| Biupiu Smart Metal Workshop | METALLURGY | hobbyist/home metalworking subscribers |
| Biupiu Smart Farming | FARMING | growers/farm operators/farming subscribers |

The products share the subscriber model but have separate resource registries and department-scoped retrieval.

## Safety boundary

The platform can provide documented metallurgy and farming knowledge, records, calculations, monitoring and workflow assistance. Physical operations remain subject to appropriate workshop/farm safety procedures, equipment limits, local regulations and competent supervision.

## Acceptance criteria

1. A metallurgy subscriber can create and retrieve metallurgy records.
2. The same subscriber cannot retrieve farming-only records unless separately entitled.
3. A farming subscriber cannot retrieve metallurgy-only records unless separately entitled.
4. Search and AI retrieval respect department scope.
5. Exports respect department scope.
6. Entitlement changes are audited.
7. Cross-department resources require explicit `SHARED` classification.
8. Automated tests include attempted cross-department access.
