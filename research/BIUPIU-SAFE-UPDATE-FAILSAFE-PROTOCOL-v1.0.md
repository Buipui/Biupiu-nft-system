# Biupiu Safe-Update / Fail-Safe Protocol v1.0

**Gate:** GPU-SYS-02  
**Date:** 19 September 2026  
**Purpose:** keep the Biupiu system usable while graphics, physics, AI, OS and dependency work is progressively integrated.

## Hard safety rules
1. No direct replacement of the Core OS. Experimental modules are adapters/packages, never silent replacements.
2. No automatic promotion. Research dependencies cannot enter a customer/runtime release without an explicit promotion gate.
3. No destructive cleanup during integration. Duplicate-looking or superseded files remain until a separate review confirms removal.
4. Dependency isolation. Third-party SDKs are referenced/pinned separately from Biupiu-owned interfaces.
5. Graceful fallback. If an optional renderer, physics solver or upscaler is unavailable, the system must fall back to the existing supported path.
6. Capability detection before use. GPU/API/SDK capabilities must be detected before selecting DX12, Vulkan, ray tracing, FSR, XeSS or another optional path.
7. No secrets in source control. API keys, private keys, credentials and local .env files remain excluded.
8. Version pinning. Experimental dependencies require an exact version or commit before runtime promotion.
9. Rollback boundary. Each integration gate must have a known-good parent commit and a reversible change set.
10. Offline-safe core. Network-dependent research/update services must not be required for basic OS operation.
11. Test before promotion. Syntax, import, configuration, contract and fallback tests precede runtime promotion.
12. No autonomous self-modification. AI/learning components may record proposed changes, but cannot silently rewrite authoritative OS, safety or release-control logic.

## Preliminary-test ladder
Level 0 — repository integrity: verify files, JSON/package syntax, index references and no accidental secrets.
Level 1 — static safety: validate adapter contracts and ensure optional dependencies do not become mandatory imports.
Level 2 — fallback: simulate missing GPU backend/SDK and confirm existing supported paths remain selectable.
Level 3 — runtime: only on a connected Windows/UE5 test environment; use a non-destructive smoke test and record results.

## Promotion states
RESEARCH -> PINNED -> STATIC-TESTED -> FALLBACK-TESTED -> LOCAL-RUNTIME-TESTED -> BENCHMARKED -> LICENCE-CLEARED -> PROMOTED
No state may be skipped.

## Bricking prevention
If an optional component fails: detect failure -> log -> disable component -> select fallback -> preserve authoritative state -> continue.
If a required component fails: stop that component only -> preserve repository/state -> produce diagnostic -> require explicit repair.
The system must not attempt destructive self-repair, mass deletion, automatic dependency replacement or uncontrolled rollback.

## Current gate result
Repository-level safety controls are registered. Actual Windows/UE5 hardware runtime tests cannot be claimed from GitHub alone and remain a separate host-validation gate.