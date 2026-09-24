# BIUPIU ANDROID WORKTREE CONSOLIDATION ARCHITECTURE — 2026-09-24

Status: REGISTERED / SOURCE ARCHITECTURE CONSOLIDATED / BUILD + DEVICE VERIFICATION OPEN

## Canonical
apps/android/ is the canonical native Biupiu R&D OS Android shell and Gradle application build authority.

## Federation compatibility
mini-os/android/ remains the Mini-OS federation/compatibility surface for provider-neutral capability contracts, federation adapters and unreconciled historical/reference lineage. It is not a second canonical Android shell.

## Shared
apps/shared/runtime/ = shared runtime/language contracts.
packages/ = shared TypeScript/domain/federation contracts.
software/rnd-os-ai/ = Native Intelligence, learning and optimisation.
core/multilang/ = native ABI/math/simulation foundations.

## Consolidation protocol
Inventory -> hash -> dependency/build cross-check -> semantic comparison -> canonical owner -> retain unresolved lineage -> semantic catalogue check -> Android build/unit -> emulator/device -> hardware/runtime -> destructive consolidation only after evidence.

## Current ownership map
| Function | Canonical |
|---|---|
| Android shell/build | apps/android/ |
| Mini-OS federation/compatibility | mini-os/android/ |
| Shared runtime contracts | apps/shared/runtime/ |
| Federation/domain contracts | packages/ |
| AI/learning/optimisation | software/rnd-os-ai/ |
| Native math/simulation | core/multilang/ |
| Filing metadata | software/digital-filing-cabinet/ |

## No-brick rule
Do not replace a working implementation merely because another tree looks newer. Replacement requires compatibility, regression, provenance, rollback and explicit owner approval.

## Gate state
Source architecture: REGISTERED.
Semantic ownership: CHECKED.
Android build: OPEN.
Device/emulator: OPEN.
GPU/NPU/NEON: OPEN.
Runtime E2E: OPEN.
PC execution: DEFERRED.
