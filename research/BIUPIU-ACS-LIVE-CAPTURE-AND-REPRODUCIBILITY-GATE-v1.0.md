# Biupiu ACS Live Capture & Reproducibility Gate v1.0

**Date:** 19 September 2026  
**Gate:** ACS-10  
**Track:** Assassin's Creed Shadows technical-reference rendering integration

## Purpose
Define the first live-capture gate after ACS-09. This gate converts the readiness contract into a deterministic capture/reproducibility procedure without fabricating workstation measurements.

## Preconditions
- ACS-07 validation harness registered.
- ACS-08 connected-host execution contract registered.
- ACS-09 readiness specification registered.
- Connected Windows/UE5/rendering host available.
- Original Biupiu Japan test scene and versioned asset/provenance manifests available.
- No Ubisoft/Assassin's Creed proprietary assets, extracted files, binaries, textures, characters, maps or restricted code are used.

## Capture sequence
1. Record host identity, OS, UE5 version, renderer build, GPU, CPU, driver and memory.
2. Validate scene, asset-manifest and licence/provenance hashes.
3. Lock camera path, output resolution, lighting/environment state and renderer settings.
4. Capture Mode A — UE5 baseline/Lumen.
5. Capture Mode B — UE5 hardware RT.
6. Capture Mode C — approved RT/path-tracing research configuration, where supported.
7. Capture Mode D — approved alternative renderer adapter, where available.
8. Emit machine-readable metadata beside each capture.
9. Record frame time/FPS, VRAM/system memory, output hash and visual observations.
10. Repeat the same capture sequence at least once.
11. Compare metadata, hashes and measured outputs for reproducibility.
12. Record PASS, CONDITIONAL, REJECT or PENDING for each mode.

## Evidence requirements
A live result is accepted only when it contains:
- host-generated measurement evidence;
- immutable scene/settings identification;
- asset/provenance manifest;
- output hash;
- renderer/engine version;
- repeat-capture evidence.

Repository-side preparation alone cannot be treated as a live render result.

## Reproducibility rule
A mode is reproducible only if the controlled scene/settings are repeated and the resulting metadata and output evidence can be compared. Any unexplained material divergence is recorded for investigation rather than silently accepted.

## Current execution state
- **ACS-10 repository capture/reproducibility contract:** EXECUTED.
- **ACS-10 live capture:** PENDING — no connected UE5/rendering workstation is available in the current execution environment.
- **ACS-10 reproducibility verification:** PENDING live captures.
- **No FPS, frame-time, GPU, memory or visual-equivalence claims are recorded.**

## Next gate
**ACS-11 — Evidence ingestion and reproducibility review:** ingest the first host-generated capture package, validate metadata/hashes/provenance, compare repeated captures, and issue a measured PASS/CONDITIONAL/REJECT decision.

## Rights boundary
Public technical research may inform implementation. Proprietary Ubisoft assets and extracted Assassin's Creed game content remain reference-only and are not copied into the Biupiu repository.
