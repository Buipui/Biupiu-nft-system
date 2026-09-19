# Biupiu World Production Gate 02

## Status
**ASSET-CONVENTION SCAFFOLD COMPLETE**

This gate establishes canonical conventions before importing or creating real assets.

## Canonical asset layers
1. Approved/licensed source asset
2. Biupiu normalization layer
3. Rig/material convention layer
4. Digital Twin metadata layer
5. Desktop master and Android LOD derivatives

## Character convention
- Canonical scale: metres
- Forward axis: +Y
- Up axis: +Z
- Base rig identifier: `BPU_RIG_HUMANOID_V1`
- Required collections: `GEO`, `RIG`, `ANIMATION`, `MATERIALS`, `COLLIDERS`, `METADATA`
- Every imported asset requires provenance, licence status and evidence state.

## Product hero convention
- One master asset per Digital Twin ID
- Separate geometry, materials, technical overlays and presentation cameras
- Engineering values remain metadata until independently validated
- Visual labels must identify concepts, studies, prototypes or verified products accurately

## Gate boundary
No third-party asset is imported automatically. Rights, licence compatibility and source provenance must be reviewed before production use.

## Next gate
Gate 03: create the first canonical hero scene package with a placeholder-safe product assembly, material slots, camera shots and Digital Twin metadata validation.
