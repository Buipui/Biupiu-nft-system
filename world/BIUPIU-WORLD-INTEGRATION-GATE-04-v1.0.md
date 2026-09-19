# Biupiu World Integration Gate 04 — Open-Source Simulator Adapter Gate

Date: 2026-09-19
Status: EXECUTED — architecture + resource-routing stage

## Objective
Move from resource discovery to controlled adapter integration without turning Biupiu World into a monolithic simulator.

## Exterminate result
- Duplicate World/development concepts were reconciled conceptually around the existing canonical World asset pipeline.
- Third-party simulator assets remain external until provenance/licence approval.
- Department-specific physics remains outside the World canonical asset layer.
- No unsupported claim of runtime completion was introduced.
- Existing private-R&D separation remains intact.

## Open-source integration priorities
AUTO: CARLA; World supplies terrain, roads, buildings, weather, lighting and materials; AUTO owns vehicles, dynamics, traffic, sensors and scenarios.
MARINE: VRX with gz-maritime/HoloOcean/UNav-Sim; World supplies ocean/coast/harbour/weather/lighting/water; MARINE owns hydrodynamics, vessels, sensors and autonomy.
AERO: JSBSim with FlightGear/SimGear/OpenVSP/AirSim; World supplies terrain/atmosphere/weather/lighting; AERO owns aircraft, 6-DoF dynamics, avionics and tests.
ROBOTICS: MuJoCo + Gazebo/ROS 2 with Webots/Genesis/IR-SIM; World supplies factories/farms/outdoor environments; ROBOTICS owns models, controllers, sensors and training.
AGRICULTURE: Biupiu World terrain/vegetation/water/climate layer; Farming Simulator remains benchmark-only unless a specific licence permits incorporation; AGRICULTURE owns crops, machinery and regenerative workflows.

## Shared interface
World Asset ID -> Scene/Environment Manifest -> Department Adapter -> Simulator -> Telemetry -> Digital Twin -> Validation

## Promotion rule
Only permissively licensed or otherwise explicitly authorised source components may be incorporated. Benchmarks and proprietary assets remain references.

## Runtime gate
The next execution stage requires actual dependency acquisition/build tests on the available development host. Repository documentation alone does not count as runtime validation.
