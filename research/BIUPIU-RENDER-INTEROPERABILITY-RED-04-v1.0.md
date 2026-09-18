# Biupiu Render Interoperability Gate — RED-04

**Status:** IMPLEMENTED — LIVE CROSS-ENGINE EXECUTION GATED  
**Date:** 18 September 2026

## Objective

Validate that a single authoritative Biupiu source asset can move through the render-provider layer without losing asset identity, model version, evidence state or provenance.

## Provider matrix

| Provider | Role | Handoff input | Required provenance | Live execution |
|---|---|---|---|---|
| BLENDER | Authoring / open 3D | glTF/FBX/OBJ/native | source asset + version | gated |
| UNREAL_ENGINE_5 | Real-time world / cinematic | glTF/FBX/USD/native | source asset + version | gated |
| REDSHIFT | Production rendering | host scene/material references | source asset + shader IDs + render manifest | gated |
| VRAY | Production rendering | host scene/material references | source asset + material IDs + render manifest | gated |
| OCTANE | GPU rendering | host scene/material references | source asset + material IDs + render manifest | gated |
| LUMION | Real-time presentation | CAD/BIM/mesh interchange | source asset + version + import settings | gated |
| KEYSHOT | Product visualization | CAD/mesh/material interchange | source asset + material IDs | gated |

The matrix defines orchestration boundaries, not proof that each application is installed or interoperable on the current host.

## Canonical handoff

SOURCE_ASSET → NORMALIZED_ASSET → PROVIDER_SCENE → RENDER_OUTPUT → PROVENANCE_RECORD

The source asset remains authoritative. Rendered files are derivatives.

## Required cross-engine invariants

1. sourceAssetId is unchanged.
2. sourceModelVersion is preserved.
3. researchId is preserved when present.
4. Evidence/IP/licence states are preserved.
5. Provider and provider version are recorded.
6. Import/export settings are recorded.
7. Output SHA-256 is recorded.
8. Provider-specific material/shader identifiers are recorded.
9. Failed or lossy conversions are recorded rather than hidden.
10. A derivative render can never overwrite the authoritative source asset.

## RED-04 test sequence

1. Register a canonical test asset.
2. Create a normalized interchange representation.
3. Generate provider-specific scene/package manifests.
4. Render a still in each available provider.
5. Compare geometry, material and camera checks against the canonical manifest.
6. Record output hashes and provenance.
7. Repeat one provider handoff to test round-trip drift.
8. Store failures in the Failure/Lessons Register.

## Acceptance

RED-04 passes only when the connected test environment demonstrates the invariants and records measured conversion/render results. Repository-level implementation alone does not constitute live interoperability proof.

## Current state

**READY FOR LIVE CROSS-ENGINE TESTING.** Provider-neutral contracts and the Redshift adapter boundary are implemented; no unsupported claim of live application availability is made.
