# Biupiu Engine — Own Core v1.0

**Gate:** ENGINE-01
**Status:** INTEGRATED at source level

Biupiu Engine is now a native renderer-neutral engine core rather than a wrapper around UE5, Unity, Lumion or Bevy.

## Owns
- world/entity lifecycle
- Digital Twin identity
- simulation clock and deterministic stepping
- modular world layers
- asset bindings and provenance
- plugin lifecycle
- health/fault state
- canonical snapshots

## World layers
TERRAIN, HYDROLOGY, WEATHER, SOIL, VEGETATION, WILDLIFE, INFRASTRUCTURE, VEHICLE, HMI, XR.

## Provider architecture
`Biupiu Engine -> provider adapter -> UE5 / Unity / Lumion / Blender / Bevy / physics / XR`

Existing Biupiu 3D/CAD, civilisation-world, Bevy, simulation-core, living-system and XR systems remain integration sources. They are not discarded or made obsolete by the native core.

## Self-diagnostic loop
`BOOT -> HEALTH -> RUN -> OBSERVE -> INVARIANT CHECK -> FAULT ISOLATION -> LOG -> PAUSE/RECOVER`

The current native core is an orchestration/simulation foundation, not yet a complete AAA renderer. Photorealism can initially be supplied by connected render providers while native rendering, streaming, terrain, vegetation, animation and XR subsystems are built behind stable interfaces.
