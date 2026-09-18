# Biupiu Render Benchmark Run Manifest v1.0

## Gate
RENDER-04 — Canonical four-engine render benchmark.

## Objective
Run the same controlled source scene through Blender Cycles, OctaneRender, V-Ray, and Unreal Engine 5, then record reproducible measurements without fabricating or mixing engineering validation with visual-render observations.

## Run order
1. Verify source scene ID and immutable scene version.
2. Record workstation CPU, GPU, VRAM, RAM, driver and display/colour-management state.
3. Record engine and integration versions.
4. Load the canonical scene without changing source geometry.
5. Validate camera, scale, lighting, materials and output resolution.
6. Execute a controlled render/test frame in each engine.
7. Record render time, memory/VRAM, output size and unsupported/conversion features.
8. Hash outputs and attach provenance metadata.
9. Record subjective visual observations separately from measured results.
10. Populate the BIUPIU-RENDER-BENCHMARK-RESULTS-v1.0.json registry.
11. Preserve original source scene and all conversion notes.

## Required evidence
- Engine version
- Workstation hardware and driver
- Source model/scene ID and version
- Render settings
- Output file hash
- Measurements
- Conversion notes
- Reviewer/date

## Acceptance
RENDER-04 is complete only when all four engines have controlled workstation evidence and the results registry is populated. Until then the repository status remains PENDING_WORKSTATION_EXECUTION.

## Security and IP
Do not commit proprietary binaries, licence keys, credentials, restricted SDKs, or unlicensed assets. Store only legal configuration, metadata, adapter contracts and benchmark evidence.

## Important
This benchmark measures visualization/render-pipeline behaviour. It does not constitute engineering simulation validation, safety certification, or product-performance proof.