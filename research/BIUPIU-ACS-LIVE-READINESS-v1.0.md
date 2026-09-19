# Biupiu ACS Live Readiness Gate v1.0

**Date:** 19 September 2026  
**Gate:** ACS-09

## Purpose
Define and verify the evidence package required before the first live UE5/rendering measurement is accepted.

## Readiness checklist
- Original Biupiu Japan test scene identified.
- Versioned asset manifest required.
- Provenance/licence manifest required.
- UE5/rendering host identity required.
- GPU/CPU/driver inventory required.
- Renderer and project settings capture required.
- Fixed camera path and resolution required.
- Output hash and machine-readable metadata required.
- At least two repeated captures required for reproducibility.

## Evidence rule
Repository preparation alone cannot satisfy live-host readiness. A host-generated evidence record is required before ACS-09 can be marked PASS.

## Current state
**ACS-09 repository readiness specification: EXECUTED.**
**ACS-09 live host readiness verification: PENDING — no connected UE5/rendering host is available in the current execution environment.**

No performance, visual-quality, or renderer-equivalence result is inferred.

## Next gate
ACS-10 = first live capture and reproducibility verification when the required host is connected.
