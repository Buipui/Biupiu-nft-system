# Biupiu DMS Customer Database Schema v1.0

## Purpose

Provide a controlled customer/account model that links people and organizations to products, sites, subscriptions, entitlements, support records and optional R&D participation.

## Core entities

**CustomerAccount**
- customer_id
- account_type (individual/organization)
- legal/display name
- contact details
- status
- created_at / updated_at
- privacy/consent references

**UserIdentity**
- user_id
- customer_id
- authentication provider reference
- profile_id
- MFA state
- account status

**Organization**
- organization_id
- customer_id
- sites
- organization roles

**Site**
- site_id
- organization_id/customer_id
- location metadata
- assigned modules
- device inventory

**ProductInstance**
- product_id
- customer_id
- site_id
- product type
- serial/device identity
- software version
- status

**Subscription**
- subscription_id
- customer_id
- plan_id
- status
- start/end/renewal dates
- billing provider reference

**Entitlement**
- entitlement_id
- subscription_id
- feature_id
- scope
- effective dates
- state
- policy version

**Feedback / R&D Contribution**
- contribution_id
- customer_id
- product_id
- consent reference
- contribution type
- submitted content reference
- IP/licence status
- review state

**AuditEvent**
- event_id
- actor_id/service_id
- action
- resource
- policy decision
- timestamp
- correlation_id

Sensitive authentication secrets and payment credentials must not be stored directly in this application database; use appropriate identity/payment providers and store references/tokens only.

## Privacy boundary

Collect only information necessary for defined purposes. Provide access, correction, deletion/retention workflows where legally applicable. Customer R&D participation must be separately consented and must not be inferred from ordinary product purchase.
