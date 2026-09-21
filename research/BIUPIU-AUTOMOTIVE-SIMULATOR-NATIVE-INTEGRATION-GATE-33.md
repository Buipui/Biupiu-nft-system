# Biupiu Automotive / Car Mechanic Simulator Native Integration — Gate 33

**Date:** 21 September 2026
**Status:** SOURCE INTEGRATED / RUNTIME BUILD VERIFICATION PENDING

## Scope
Unify the automotive workshop, vehicle-dynamics, Digital Twin and external simulator/mod research into one governed native integration path.

## Native path
Core C ABI -> C++ deterministic vehicle model -> simulator adapter -> DMS/Digital Twin -> UE5 visual layer -> validation/replay.

The first native kernel is deliberately dependency-free and models longitudinal force balance. It is a foundation, not a complete vehicle dynamics solver.

## Harvested external families
- Car Mechanic Simulator 2021: workshop/diagnostics/component workflow and community mod patterns.
- Assetto Corsa: vehicle data/configuration and suspension-tool patterns.
- Gran Turismo: structured game-data/script modding research; reference only.
- Need for Speed: AttribSys/VLT tooling and structured data-editing patterns.
- Crash Team Racing: clean native-port/mod-SDK architecture as a case study in platform abstraction.
- GTA V: vehicle metadata/package tooling patterns; reference only.
- Forza: open-source mod-tool/repository patterns; reference only.
- CARLA/OpenADS: open vehicle physics/sensors/digital-twin backend candidates.
- SODA.Sim/OAS/Rigs of Rods: component validation, vehicle dynamics and soft-body references.
- ISO 23247 automotive digital-twin implementation research.

## Rights boundary
Only code with a verified compatible licence may be reused. Proprietary game binaries, extracted assets, copyrighted vehicle models/textures/audio, manufacturer IP and game-specific dumps are NOT copied into Biupiu. External repositories are cross-linked as research candidates and adapter specifications.

## Foreign-language lane
Chinese, German, Italian, Japanese, French, Spanish, Portuguese and Russian discovery is recorded as metadata. Language is not treated as evidence of quality or permission. Translation must preserve technical identifiers and licence terms.

## Native automotive contract
A vehicle is represented by:
1. stable asset/twin ID;
2. mass/inertia/geometry parameters;
3. propulsion/braking parameters;
4. thermal/electrical state;
5. suspension/tyre state;
6. component dependency graph;
7. fault state;
8. measurements/telemetry;
9. provenance and evidence state;
10. simulation model/version.

## Smoke-test boundary
The repository can validate source contracts and deterministic local tests, but it cannot honestly claim host compilation, UE5 execution, third-party simulator execution or hardware-in-loop until those environments are actually run.

## Promotion
DISCOVER -> LICENSE -> NORMALISE -> NATIVE CONTRACT -> STATIC/UNIT -> INTEGRATION -> DIGITAL-TWIN -> UE5 -> HIL -> RELEASE
