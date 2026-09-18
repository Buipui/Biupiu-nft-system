# Biupiu Subscription & Entitlement Model v1.0

## Purpose

Provide a controlled way to activate optional digital functions across Biupiu products and services without hard-coding subscription logic into every product.

## Objects

Plan -> Entitlement Set -> Customer/Organization -> Product/Device -> Feature Gate

Each entitlement has:

- feature_id
- module_id
- version
- status
- effective_from
- effective_until
- scope (user, organization, site, device)
- source (plan, licence, grant, internal)
- audit reference

## Example tiers

CORE — essential product functions and required updates.
STANDARD — routine monitoring and software features.
PRO — advanced analytics, automation and diagnostics.
ENTERPRISE — multi-site DMS, APIs, fleet/site administration and advanced analytics.
R&D PARTNER — explicitly opt-in experimental features and research workflows.

These are architecture placeholders, not final commercial pricing or contractual promises.

## Rules

1. Safety-critical functions remain available regardless of subscription state.
2. Feature availability is checked against authoritative DMS entitlements.
3. Offline products receive signed cached entitlements with an expiry/grace policy appropriate to the product.
4. Subscription changes generate audit events.
5. Experimental features are separately identified and may require explicit beta consent.
6. Customers can opt out of optional R&D participation without losing ordinary product rights.
