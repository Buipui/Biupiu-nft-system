# AI-NATIVE-04 — Failure-Learning & Regression Memory v1.0
**Status:** REGISTERED + IMPLEMENTED / HOST VERIFICATION PENDING

## Purpose
Turn build, test, provider, integration and security failures into deterministic reusable regression evidence.

## Rules
- A failure is retained; it is never silently discarded.
- Failure identity is deterministic from gate, category, message and evidence digest.
- Repeated identical failures deduplicate.
- Resolution is explicit and recorded.
- An unresolved failure remains available to future regression checks.
- This is evidence memory, not autonomous authority: AI may classify/propose; OS validation remains authoritative.

## Categories
build, test, provider, dependency, interface, schema, runtime, security, numerical, integration, provenance, licence, resource, unknown.

## Promotion
REGISTERED -> IMPLEMENTED -> HOST_TESTED -> REGRESSION_PASS -> VERIFIED
