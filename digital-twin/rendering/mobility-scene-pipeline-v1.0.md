# Biupiu Mobility Scene & Asset Pipeline v1.0

Status: IN PROGRESS
Scope: Automotive / Jet / eVTOL

## Pipeline
Design brief -> canonical asset specification -> source/licence manifest -> high-detail geometry -> PBR materials -> lighting/environment -> simulation hooks -> Blender scene -> UE/Digital Twin scene mapping -> render configuration -> QA -> provenance record -> approved benchmark.

## Asset layers
1. Product master geometry
2. Engineering/detail geometry
3. Materials and texture sets
4. Lighting rigs
5. Environment/test scenes
6. Simulation interfaces
7. Camera/composition presets
8. Biupiu branding
9. Render QA configuration
10. Provenance metadata

## Automotive
Master scene must support road/studio/test-track contexts and preserve readable body, glazing, aero, wheel, lighting and propulsion/technology details.

## Jet
Master scene must support studio, ground and airborne contexts and preserve readable aerodynamic surfaces, propulsion, control surfaces, cockpit/canopy and landing gear.

## eVTOL
Master scene must support studio, pad, hover and airborne contexts and preserve readable rotor/duct, nacelle/arm, fuselage, cabin, landing system and technology-module details.

## Quality controls
- No destructive overwriting of source assets.
- Separate concept assets from engineering-validated assets.
- Materials must use consistent PBR conventions.
- Lighting presets must include a neutral technical setup.
- Hero lighting may not obscure technical geometry.
- Camera presets must support repeatable before/after benchmarking.
- Every approved output must reference asset/build IDs and source/licence records.
- External assets are integration candidates until licence compatibility and technical suitability are verified.

## Current implementation state
Repository structure contains digital-twin datasets/schemas. This document establishes the mobility rendering mapping layer; it does not claim that all downstream 3D scenes or external assets have already been implemented.

## Next gate
Populate verified vehicle-specific asset manifests and map them to the canonical scene pipeline before claiming high-detail implementation complete.
