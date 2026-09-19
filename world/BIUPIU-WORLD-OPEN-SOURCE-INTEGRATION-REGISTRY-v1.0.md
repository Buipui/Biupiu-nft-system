# Biupiu World — Open-Source Integration Registry v1.0

Date: 2026-09-19

## Purpose
Biupiu World is the canonical shared world layer for visual assets, environments, lighting, shading/material definitions, weather/atmosphere, terrain, world-building conventions, provenance and reusable scene metadata.

Department simulators remain independently researchable and executable. They consume only the shared World contracts and the minimum department-specific adapters/resources required for their own domain.

## Core rule
WORLD owns:
- canonical environment and location definitions
- reusable terrain/world-building systems
- lighting and time-of-day conventions
- weather/atmosphere contracts
- materials/shaders and visual identity rules
- common asset metadata/provenance
- shared scene/coordinate conventions
- approved reusable assets

DEPARTMENT packages own:
- domain physics
- domain-specific sensors
- domain controllers/autonomy
- department test scenarios
- department-specific vehicle/robot/aircraft/vessel models
- department-specific solver adapters

No proprietary third-party assets or code are promoted into Biupiu-owned assets merely because they were discovered.

## Open-source sources audited

### World / rendering / engine
- Bevy — https://github.com/bevyengine/bevy — MIT/Apache-2.0; modular Rust ECS engine.
- OpenWorld UE starter — https://github.com/GameForgeStudio/Unreal-Open-World-Starter — open-source starter; requires licensed Unreal Engine.
- OpenWorld UE project — https://github.com/OpenWorldGame-Io/OpenWorld — UE5 open-world reference.
- Godot USD extension — https://github.com/migueldeicaza/godot-usd — OpenUSD/Godot interoperability reference.
- Godotiles — https://github.com/ziv/godotiles — MIT/Apache-2.0; large-world geospatial streaming, terrain LOD, fog and shadows.

### Automotive
- CARLA — https://github.com/carla-simulator/carla — autonomous-driving simulation and open digital assets.
- RWTH CARLA fork — https://github.com/ika-rwth-aachen/carla-simulator — modular CARLA simulation-core reference.

Routing: World supplies environments/materials/weather contracts; AUTO consumes only vehicle/traffic/sensor/physics resources.

### Marine
- VRX — https://github.com/osrf/vrx — Apache-2.0 maritime USV simulation.
- Honu Robotics maritime stack — https://github.com/HonuRobotics/gz-maritime — marine waves/rendering/ROS 2 architecture.
- VORC — https://github.com/osrf/vorc — Apache-2.0 maritime environment/challenge foundation.
- HoloOcean — https://github.com/byu-holoocean/HoloOcean — UE5 marine perception/autonomy reference.
- UNav-Sim — https://github.com/open-airlab/UNav-Sim — MIT underwater robotics simulation.
- Project DAVE / Stonefish / WEC-Sim — retain as department research references pending per-repository licence and compatibility checks.

Routing: World supplies shared water/environment/lighting/weather conventions; MARINE owns hydrodynamics, vessel dynamics, marine sensors and autonomy.

### Robotics
- Gazebo/ROS 2 ecosystem — department simulation reference.
- MuJoCo — https://github.com/google-deepmind/mujoco — physics/contact/control reference.
- Webots — independent robotics simulator benchmark.
- Genesis — embodied-AI physics benchmark.
- IR-SIM — robot-simulation benchmark.

Routing: World supplies common environments/assets; ROBOTICS owns robot models, control, sensors and training scenarios.

### Aerospace
- JSBSim — flight-dynamics reference.
- FlightGear/SimGear — open flight-simulation reference.
- OpenVSP — parametric aircraft geometry.
- AirSim/Project AirSim — autonomous vehicle/sensor reference.
- Flightmare — high-performance flight/robotics reference.

Routing: World supplies common terrain/weather/lighting/environment contracts; AERO owns flight dynamics, avionics, aircraft models and flight-test scenarios.

### Agriculture
- Farming Simulator — benchmark only; proprietary game content is not copied.
- Open-source agricultural/terrain/world resources are routed through the World asset/provenance gate before use.

Routing: World supplies terrain, climate, vegetation, water, roads and buildings; AGRICULTURE owns crop models, farm machinery, regenerative-agriculture logic and workflows.

## Promotion pipeline
DISCOVER → LICENCE CHECK → PROVENANCE RECORD → COMPATIBILITY TEST → ADAPTER/MANIFEST → WORLD OR DEPARTMENT ROUTING → TEST → APPROVE → RELEASE

External repositories are references/dependencies unless their licence explicitly permits incorporation and the specific files pass provenance review.

## Current implementation status
This registry records architecture and integration targets. It does not claim that every external simulator has been cloned, compiled, or connected. Runtime validation remains a separate gate.

## Design objective
One Biupiu World. Many independent simulators. Shared assets and contracts. Minimal duplication. Clear provenance.
