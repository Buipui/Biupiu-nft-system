# Flight Simulation → UE5 Architecture v1.0

## Runtime layers

1. **UE5 presentation layer** — photorealistic environments, aircraft meshes, materials, lighting, cameras and showreel rendering.
2. **Flight model layer** — JSBSim 6-DoF dynamics, propulsion, controls, landing gear and atmosphere.
3. **Vehicle-design layer** — OpenVSP parametric geometry and engineering exports.
4. **Autonomy layer** — AirSim/Project AirSim APIs, sensor simulation and optional PX4/ArduPilot SITL.
5. **World/scenery layer** — FlightGear/SimGear and terrain-generation references.
6. **Biupiu intelligence/control layer** — experiment orchestration, scenario definitions, telemetry, AI/ML experiments and provenance.
7. **Repository/IP layer** — research IDs, algorithm versions, asset hashes and licence records.

## Required separation

The simulator integration must not silently convert third-party aircraft models, textures, scenery or code into Biupiu-owned IP. Only original Biupiu assets and legally reusable dependencies enter the production pipeline.

## Target outputs

- Photorealistic aircraft/VTOL/marine/automotive concept renders.
- Interactive UE5 flight-test scenes.
- Repeatable flight-dynamics experiments.
- AI/autonomy and sensor experiments.
- Engineering concept validation datasets.
- Showreel sequences generated from the same authoritative scene/asset records.
