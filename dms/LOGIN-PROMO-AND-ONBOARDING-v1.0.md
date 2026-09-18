# Biupiu DMS Login Promotions & Onboarding v1.0

## Purpose

Create a customer-facing login experience that communicates available product functions and optional upgrades without bypassing the entitlement system.

## Login experience

1. Authenticate user.
2. Resolve customer, organization and product scope.
3. Retrieve current subscription and entitlements from MIC.
4. Show enabled functions.
5. Show unavailable optional functions with a clear upgrade message.
6. Display applicable plan comparison and upgrade path.
7. Show product/R&D participation invitations only where eligible and consent has not already been recorded.
8. Record promotion/impression events according to privacy policy.

## Promotion rules

- Promotions must reflect the user's actual eligible upgrade path.
- Do not advertise a function that the user's product hardware cannot support.
- Do not imply that safety-critical functions are subscription locked.
- Downgraded accounts must immediately reflect the current entitlement state after the effective change, subject to any contractual grace period.
- Promotional content is separate from authorization logic.

## Example UI states

AVAILABLE — "Included in your plan"
UPGRADE — "Available with Pro"
LOCKED — "Not supported by this product"
TRIAL — "Trial active until [date]"
PENDING — "Activation in progress"

Promotions are informational; the MIC entitlement service remains authoritative.
