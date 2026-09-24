# BIUPIU ANDROID WORKTREE CONSOLIDATION ARCHITECTURE — 2026-09-24

Status: REGISTERED / SOURCE ARCHITECTURE CONSOLIDATED / BUILD + DEVICE VERIFICATION OPEN

## Canonical worktree

`apps/android/` is the canonical native Biupiu R&D OS Android shell and Gradle application build authority.

It owns:
- native shell/navigation;
- Android platform integration;
- Android UI/resources;
- platform adapters;
- native C/C++ bridge where required;
- Android application build/test configuration.

## Federation compatibility worktree

`mini-os/android/` remains the Mini-OS federation/compatibility surface.

It owns:
- provider-neutral capability contracts;
- federation-specific adapter boundaries;
- Mini-OS compatibility experiments;
- legacy/reference implementation lineage that has not yet been reconciled into the canonical app.

It is not a second canonical Android shell.

## Shared layers

`apps/shared/runtime/` owns shared runtime contracts and language/runtime boundaries.

`packages/` owns shared TypeScript/domain/federation contracts.

`software/rnd-os-ai/` owns Native Biupiu Intelligence, learning, optimisation routing, evidence and proposal generation.

`core/multilang/` owns native ABI/math/simulation foundations.

## Consolidation protocol

1. Inventory every Android source path.
2. Hash/identify duplicate implementations.
3. Cross-reference dependencies and build inputs.
4. Compare semantics against the Coding Matrix and Federation contracts.
5. Assign canonical owner.
6. Retain legacy/reference material where lineage is unresolved.
7. Remove only after duplicate authority is proven and tests/references are reconciled.
8. Re-run semantic catalogue and DigiFile checks.
9. Run Android build/unit tests.
10. Run emulator/device and hardware gates.
11. Only then consider destructive physical consolidation.

## Current mapping

| Area | Canonical location | Secondary/reference | Authority |
|---|---|---|---|
| Android shell | `apps/android/` | `mini-os/android/app/` | apps/android |
| Android federation | shared contracts + approved app adapters | `mini-os/android/federation/` | Federation contracts |
| Language/runtime | `apps/shared/runtime/` | locale-specific history | shared runtime |
| AI/learning | `software/rnd-os-ai/` | external providers | Native Intelligence |
| Native math/simulation | `core/multilang/` | specialist adapters | Core/native domain |
| Build | `apps/android/` | Mini-OS build surface | owning build system |
| Device capability | Android registry/contracts | OEM/provider references | Android/Federation |
| Filing metadata | Digital Filing Cabinet | none | Digital Filing Cabinet |

## No-brick rule

Do not replace a working Android implementation merely because another tree looks newer or more complete. Replacement requires compatibility, regression, provenance, rollback and explicit owner approval.

## Verification boundary

Source architecture: REGISTERED.
Semantic ownership: CHECKED.
Build: OPEN.
Device/emulator: OPEN.
GPU/NPU/NEON: OPEN.
Runtime E2E: OPEN.
