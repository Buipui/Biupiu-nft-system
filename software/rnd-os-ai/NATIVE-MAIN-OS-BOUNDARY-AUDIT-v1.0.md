# AI-NATIVE-02 — Native vs Main OS Boundary Audit v1.0
**Status:** REGISTERED + IMPLEMENTED / HOST VERIFICATION PENDING

## Revised gate protocol
HARVEST -> MAP -> CHALLENGE -> PROPOSE -> IMPLEMENT -> VERIFY -> REGRESS -> AUDIT -> PROMOTE

## Objective
Prevent the Native mini-OS proving ground from silently becoming a second authoritative Main OS. Define explicit ownership and C-compatible boundaries before promotion.

## Rules
- Native owns experimental/proving-ground implementations.
- Main OS owns production authority and policy.
- Shared services require explicit stable interfaces.
- External providers are adapters/evidence sources, never authoritative OS state.
- Any ambiguous ownership is REVIEW/BLOCKED rather than silently promoted.
- Every promoted module requires deterministic tests and regression evidence.

## Initial boundary
Native visual runtime -> Native authority.
Main OS integration adapters -> Main authority.
Shared scheduler/contracts -> explicit C ABI.
Third-party SDKs/providers -> external evidence/provider boundary.

## Promotion
REGISTERED -> IMPLEMENTED -> HOST_TESTED -> REGRESSION_PASS -> VERIFIED
