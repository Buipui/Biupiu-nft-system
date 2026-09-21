# Biupiu OS Resource Consolidation & Housekeeping — Gate 29

**Date:** 21 September 2026  
**Status:** IMPLEMENTED — repository consolidation; runtime/host/device verification remains separate

## Objective

Deep-audit the existing repository and historical execution record, identify reusable Biupiu OS code/modules/contracts, remove architectural ambiguity from the active path, and create a canonical map so new gates extend existing work instead of duplicating it.

## Reusable active-path modules

| Layer | Existing resource | Use |
|---|---|---|
| Core ABI | `core/multilang/` | C ABI + Rust kernel boundary + C++ native contract |
| Android shell | `apps/android/app/src/main/.../BiupiuShell.kt` | native OS shell and navigation |
| Android contracts | `SharedContracts.kt`, `CapabilityRouter.kt` | request/response, adapter and capability routing |
| Hardware | `HardwareCapability.kt`, `HardwareReferenceProfiles.kt` | machine capability abstraction |
| OEM | `OemCompatibility.kt`, `OemResourceRegistry.kt`, `ForeignResourceRegistry.kt` | OEM/resource discovery and governed adapter boundary |
| Runtime | `apps/shared/runtime/` | department routing, service gateway, registry, render queue and release gates |
| Intelligence governance | AI-44 through AI-73 | evidence, routing, readiness, release, regression, state, governance and closure controls |
| Rendering | `packages/biupiu-3d-engine/`, `packages/biupiu-blender/` | Digital Twin/visualisation integration |
| World | `world/client/`, `world/access/`, `world/environments/` | controlled World shell, access and environment contracts |
| Research | `research/BIUPIU-RESOURCE-MANIFEST-v1.0.json` | open-resource candidate register |
| Governance | `BIUPIU-HOUSEKEEPING-AND-GATE-RECONCILIATION-PROTOCOL-v1.0.md` | canonical evidence-preserving housekeeping |

## Consolidation decisions

1. **Extend existing contracts before creating new parallel modules.**
2. **Foreign/OEM resources remain metadata-first** until licence, security, compatibility and test gates pass.
3. **Core OS boundaries remain authoritative:** C ABI/HAL -> Rust/C++ services -> OS validation -> DMS -> Intelligence.
4. **Android remains a native shell/client boundary**, not proof of a finished cross-platform production OS.
5. **Department runtime remains contract-driven** through `apps/shared/runtime/`.
6. **AI governance remains separate from OS authority**; AI may propose, simulate and validate but does not silently bypass authorisation.
7. **Material/UX modules remain presentation layers** and cannot alter semantic state or engineering authority.
8. **World/rendering modules remain consumers of governed contracts**, not alternate OS authorities.
9. Historical/speculative research is preserved but cannot silently become verified implementation.

## Housekeeping findings

- The repository contains substantial existing functionality; the primary risk is **duplication/drift**, not absence of architecture.
- Multiple historical gate documents intentionally remain because they preserve provenance.
- Runtime evidence is uneven across Android, desktop, VM, UE5, physical hardware and production deployment.
- Existing manifests already provide resource/provider/integrity registries; Gate 29 therefore adds a consolidation index rather than another competing registry.
- Open work from Interrupted Analysis Queue v1.2 remains open: canonical test vectors, solver regression/failure injection, telemetry safeguards, physical correlation and UE5 verification.

## Canonical next-gate order

**G29-A:** repository consistency + orphan/duplicate detection  
**G29-B:** unit/build/emulator execution using current main  
**G29-C:** cross-platform contract execution  
**G29-D:** hardware/OEM adapter execution  
**G29-E:** VM/host OS execution  
**G29-F:** physical/HIL and production gates

No later gate may be promoted from architecture-only evidence.

## Promotion boundary

**Gate 29 status: IMPLEMENTED.** This record does not claim that Android, desktop, VM, physical hardware, UE5, live hosting or production deployment is verified.
