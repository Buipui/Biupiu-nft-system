# Biupiu Render Benchmark Validation Gate 05 v1.0

## Gate
RENDER-05 — benchmark evidence validation, results ingestion and cross-engine compatibility analysis.

## Purpose
Validate benchmark evidence before it is accepted into the Biupiu R&D OS. This gate separates measured workstation evidence from visual observations and prevents unsupported performance claims.

## Inputs
- BIUPIU-RENDER-BENCHMARK-RESULTS-v1.0.json
- BIUPIU-RENDER-BENCHMARK-RUN-MANIFEST-v1.0.md
- BIUPIU-RENDER-BENCHMARK-GATE-01-v1.0.md
- BIUPIU-RENDER-WORKSTATION-COMPATIBILITY-GATE-03-v1.0.md
- Canonical source scene and source-model version.

## Validation checks
1. Confirm all four engine records exist: Blender Cycles, OctaneRender, V-Ray and Unreal Engine 5.
2. Confirm every measurement has engine/version and workstation provenance.
3. Confirm source geometry, scale, camera, lighting, materials and resolution are controlled.
4. Confirm output hashes identify the actual rendered/test outputs.
5. Confirm unsupported features and conversion changes are recorded.
6. Reject missing, contradictory or manually invented measurements.
7. Keep subjective visual observations separate from measured performance.
8. Do not convert render performance into engineering-performance claims.
9. Confirm proprietary binaries, credentials and restricted assets are absent from the repository.
10. Record compatibility findings as per-engine observations rather than a winner/ranking.

## Cross-engine compatibility matrix
| Dimension | Cycles | Octane | V-Ray | UE5 | Evidence |
|---|---|---|---|---|---|
| Source geometry fidelity | PENDING | PENDING | PENDING | PENDING | Render evidence |
| Material conversion | PENDING | PENDING | PENDING | PENDING | Scene/output comparison |
| Camera/scale preservation | PENDING | PENDING | PENDING | PENDING | Scene metadata |
| Lighting conversion | PENDING | PENDING | PENDING | PENDING | Scene metadata/output |
| Transparency/refraction | PENDING | PENDING | PENDING | PENDING | Controlled test |
| Composite/coating appearance | PENDING | PENDING | PENDING | PENDING | Controlled test |
| Photonic/emissive element | PENDING | PENDING | PENDING | PENDING | Controlled test |
| Interoperability | PENDING | PENDING | PENDING | PENDING | Import/export logs |

## Current gate result
RENDER-05 framework validation: PASS.
Actual four-engine evidence validation: PENDING_WORKSTATION_EXECUTION.

## Exit criteria
RENDER-05 closes when the results registry contains reproducible evidence for all four engines, every output is traceable to the canonical source scene, and compatibility observations are reviewed.

## Next gate
RENDER-06 — render pipeline integration test: canonical asset -> engine adapters -> provenance registry -> showcase output.