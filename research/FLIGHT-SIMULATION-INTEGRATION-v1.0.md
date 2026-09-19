# Biupiu Flight Simulation Integration v1.0

## Purpose

Integrate open-source flight-simulation, flight-dynamics, aircraft-design, autonomous-systems and scenery resources into the Biupiu R&D OS without copying third-party source code into the repository.

## Integration map

- **Unreal Engine 5** — primary visual/interactive simulation host.
- **JSBSim** — flight-dynamics/6-DoF physics layer and aircraft-system definitions.
- **FlightGear / SimGear** — open flight-simulation reference stack, visualization/reference integration and simulation interoperability.
- **AirSim / Project AirSim** — autonomous vehicle simulation, sensors, APIs and AI/robotics experimentation.
- **OpenVSP** — parametric aircraft geometry/design and engineering workflow.
- **Flightmare** — high-performance robotics/flight simulation research reference.
- **Orbiter** — spaceflight/vehicle simulation reference where relevant.
- **Ortho4XP / geospatial tooling** — terrain/world-generation research reference.

## Biupiu pipeline

Research → aircraft/vehicle concept → OpenVSP geometry → export/asset preparation → UE5 visual model → JSBSim FDM → avionics/control interfaces → AirSim/autonomy/sensor tests → scenario validation → showreel/render pipeline → provenance record.

## Repository boundary

Third-party repositories remain external dependencies/references. This repository stores integration manifests, adapters, configuration, provenance and original Biupiu work only. Do not vendor third-party code or proprietary simulator assets without licence permission.

## Initial resource registry

| Resource | Role | Integration status |
|---|---|---|
| JSBSim | Flight dynamics / controls | Mapped |
| JSBSim Unreal reference application | UE5 FDM bridge | Mapped |
| FlightGear | Flight simulator/reference | Mapped |
| SimGear | FlightGear simulation libraries | Mapped |
| AirSim | Autonomous vehicle simulation | Mapped |
| Project AirSim | Current autonomous-simulation reference | Mapped |
| OpenVSP | Aircraft geometry/design | Mapped |
| Flightmare | Robotics/flight simulation | Research reference |
| Orbiter | Spaceflight simulation | Research reference |
| Ortho4XP | Terrain/scenery generation | Research reference |

## Licensing gate

Before executable redistribution, commercial deployment, or source incorporation, record the upstream repository, commit/tag, licence, intended use and compatibility review in the dependency manifest.

## Safety/validation gate

Simulation output is a research/engineering aid and must not be treated as flight certification. Real-world aircraft, propulsion, control or autonomous-system decisions require appropriate engineering verification and regulatory processes.

## Source references

- https://github.com/JSBSim-Team/jsbsim
- https://github.com/FlightGear/flightgear
- https://github.com/FlightGear/simgear
- https://github.com/microsoft/AirSim
- https://github.com/iamaisim/ProjectAirSim
- https://github.com/OpenVSP/OpenVSP
- https://github.com/uzh-rpg/flightmare
- https://github.com/orbitersim/orbiter
- https://github.com/oscarpilote/Ortho4XP
