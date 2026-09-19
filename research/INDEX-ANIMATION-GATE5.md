# Biupiu Animation Research Index — Gate 5

**Version:** 1.0  
**Date:** 2026-09-19  
**Status:** TEST MATRIX IMPLEMENTED — RUNTIME VALIDATION PENDING

## Added
- `research/pipeline-tests/INTERCHANGE-MATRIX-GATE5.md`

## Pipeline progression
Gate 1–2 established the minimal USD and OTIO fixtures. Gate 3 added static validation. Gate 4 synchronized that validator with the actual OTIO structure and added dedicated CI configuration.

Gate 5 now formalizes the runtime interchange matrix for:
- OpenUSD stage parsing
- Blender USD import/export
- Unreal USD Stage / Interchange import
- Round-trip preservation of hierarchy and animation
- OTIO editorial handoff

## Current status
The repository contains the test contract, but no runtime pass is claimed until actual DCC/engine execution produces evidence.

## Next gate
Gate 6: add machine-readable expected-results fixtures and comparison tooling so runtime exports can be compared against the canonical USD scene.
