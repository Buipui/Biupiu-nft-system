# Biupiu Render Workstation Compatibility — Gate RENDER-03

**Status:** Executed as a repository readiness gate
**Date:** 18 September 2026
**Parent:** BIUPIU-RENDER-BENCHMARK-GATE-01-v1.0

## Objective

Define a reproducible workstation preflight before the first real Cycles / Octane / V-Ray / Unreal Engine 5 benchmark.

## Preflight matrix

| Component | Required evidence | Gate state |
|---|---|---|
| Blender | Installed version + successful launch | PENDING workstation |
| OctaneRender | Installed version + compatible OctaneBlender integration | PENDING workstation |
| V-Ray | Installed version + successful scene load | PENDING workstation |
| Unreal Engine 5 | Installed version + project launch | PENDING workstation |
| GPU | Model, driver, VRAM | PENDING workstation |
| CPU/RAM | Model, RAM capacity | PENDING workstation |
| Storage | Available working space | PENDING workstation |
| Display/colour | Resolution and colour-management target | PENDING workstation |
| Benchmark scene | Versioned source scene | READY |
| Provenance metadata | Source-model/render-engine schema | READY |

## Execution rule

The repository can validate the benchmark architecture and preflight contract, but cannot truthfully mark workstation installation or render execution as passed without direct workstation evidence.

No performance ranking is generated from unmeasured assumptions.

## First-run procedure

1. Record workstation hardware and driver versions.
2. Launch Blender and validate the canonical benchmark scene.
3. Validate Octane integration and render a small test frame.
4. Validate V-Ray and render a small test frame.
5. Open the corresponding Unreal Engine 5 scene.
6. Record engine-specific material/lighting conversions.
7. Run the canonical benchmark only after all four adapters pass basic scene-load checks.
8. Store measurements and output hashes separately from subjective visual review.
9. Attach engine/version/hardware metadata to each result.
10. Preserve the original source scene unchanged.

## Security/provenance

Do not commit:
- proprietary binaries
- license keys
- credentials
- unlicensed texture/material libraries
- vendor installers

Commit only reproducible configuration, metadata, adapter contracts and legally distributable test assets.

## Gate result

**RENDER-03 architecture/preflight: PASS**

**RENDER-03 workstation execution: NOT CLAIMED**

This distinction is intentional. The next gate is the actual controlled render run once workstation evidence is available.

## Next gate

**RENDER-04 — first canonical four-engine render benchmark and results registry.**
