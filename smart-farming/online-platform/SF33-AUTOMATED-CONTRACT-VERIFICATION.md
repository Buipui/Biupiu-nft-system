# SF-33 — Automated Contract Verification & Cross-Platform Release Readiness

## Purpose
Define automated checks for the shared Biupiu World runtime/mobile contracts.

Status: CONTRACT-READY / EXECUTION PENDING

## Verification domains
1. Schema integrity
2. Stable-ID integrity
3. Scene-to-asset resolution
4. Context-key completeness
5. Claim-status consistency
6. Rights-state gating
7. Mobile route coverage
8. Commerce guard behaviour
9. Archive/version integrity
10. Release-state consistency

## Cross-platform rule
Desktop/world and mobile must consume the same canonical IDs and claim/rights states. Platform-specific presentation may differ, but semantic identity must not.

## Blocking conditions
Any orphaned ID, missing required context key, invalid claim state, unresolved rights state or route without a destination blocks release readiness.

## Execution target
The verification runner should emit:
- PASS
- FAIL
- BLOCKED
- NOT_TESTED

and produce a machine-readable report with test ID, input, expected state, observed state and timestamp.
