# Biupiu Render Integration Gate 06 v1.0

## Gate
RENDER-06 — canonical asset to engine adapters to provenance registry to showcase-output integration test.

## Objective
Define an end-to-end integration contract so a single authoritative Biupiu source asset can be routed through supported render adapters without losing identity, version, material provenance or audit information.

## Pipeline
AUTHORITATIVE_SOURCE_ASSET
→ SCENE_NORMALIZATION
→ ENGINE_ADAPTER
→ RENDER_CONFIGURATION
→ CONTROLLED_OUTPUT
→ PROVENANCE_RECORD
→ SHOWCASE_ASSET

## Supported adapters
- BLENDER_CYCLES: baseline/open render path.
- OCTANE: GPU photorealistic render adapter.
- V_RAY: production render adapter.
- UNREAL_ENGINE_5: real-time, interactive and virtual-production adapter.

## Required asset contract
- asset_id
- source_revision
- geometry_checksum
- physical_scale
- material_manifest
- texture_provenance
- camera_profile
- lighting_profile
- environment_id
- render_engine
- engine_version
- render_configuration_id
- output_id
- output_checksum
- creation_timestamp
- reviewer_status

## Integration tests
### INT-06-01 — Identity preservation
Pass only if the output remains traceable to the same source asset and revision.

### INT-06-02 — Geometry preservation
Pass only if transforms, scale and geometry revision are explicitly recorded.

### INT-06-03 — Material provenance
Pass only if every externally sourced texture/material is identifiable and licensing status is recorded.

### INT-06-04 — Adapter isolation
Pass only if proprietary engine binaries, credentials and restricted SDKs remain outside the repository.

### INT-06-05 — Output provenance
Pass only if each showcase output receives a unique output ID and checksum.

### INT-06-06 — Cross-engine traceability
Pass only if equivalent outputs can be associated with the same source asset without implying that visual equivalence equals engineering equivalence.

### INT-06-07 — Failure handling
Adapter failures, unsupported features and conversion warnings must be logged rather than silently discarded.

## Execution registry
| Test | Status | Evidence |
|---|---|---|
| INT-06-01 Identity preservation | PENDING | Workstation/integration run |
| INT-06-02 Geometry preservation | PENDING | Controlled scene comparison |
| INT-06-03 Material provenance | PENDING | Material manifest |
| INT-06-04 Adapter isolation | PASS (repository policy) | Repository inspection |
| INT-06-05 Output provenance | PENDING | Output hashes |
| INT-06-06 Cross-engine traceability | PENDING | Four-engine run |
| INT-06-07 Failure handling | PENDING | Adapter logs |

## Showcase output classes
- PRODUCT_STILL
- DIGITAL_TWIN
- CINEMATIC_SHOWREEL
- CONCEPT_VARIATION
- RESEARCH_VISUALIZATION

Showcase outputs are derivative assets. They do not replace authoritative CAD, engineering models, experimental data or research evidence.

## Current result
RENDER-06 architecture/integration contract: PASS.
Physical engine integration execution: PENDING workstation execution.

## Next gate
RENDER-07 — automated provenance and asset-lineage test harness.