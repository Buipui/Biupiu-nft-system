# Biupiu R&D Research Index

**Version:** 3.5
**Updated:** 19 September 2026
**Repository:** Biupiu NFT / computational-art / personal R&D portfolio

## Flight Simulation / Aerospace Integration — FLIGHT-SIM-01

Added the Flight Simulation integration layer:
- `research/FLIGHT-SIMULATION-INTEGRATION-v1.0.md` — external flight-simulation, dynamics, autonomy, aircraft-design and scenery resource map.
- `research/FLIGHT-SIMULATION-DEPENDENCIES-v1.0.json` — machine-readable dependency/reference registry.
- `docs/FLIGHT-SIM-UE5-ARCHITECTURE-v1.0.md` — UE5 runtime architecture and Digital Twin connection.

Mapped resources:
- JSBSim — 6-DoF flight dynamics, controls and propulsion.
- JSBSim Unreal reference — UE5 flight-model integration.
- FlightGear / SimGear — open simulator and simulation-library reference.
- Microsoft AirSim / Project AirSim — autonomous aircraft, sensors, APIs and robotics simulation.
- OpenVSP — parametric aircraft geometry and engineering workflow.
- Flightmare — high-performance flight/robotics simulation research.
- Orbiter — spaceflight/vehicle simulation reference.
- Ortho4XP — terrain/scenery generation reference.

### Digital Twin integration

`Research → concept → OpenVSP geometry → UE5 asset → JSBSim dynamics → avionics/control → AirSim autonomy/sensors → scenario test → telemetry/results → Digital Twin → provenance/IP gate → showreel`.

The integration is cross-linked to AERO, STEALTH-GEO, MARINE, ROBOTICS, ADV-MFG, AI, COMPUTE, CG-3D, DIGITAL-TWIN and VIDEO-SERIES where technically relevant.

### Licence/IP boundary

Third-party repositories remain external dependencies/references. Their source code, proprietary simulator assets, aircraft models, textures and scenery are not copied into Biupiu. Executable redistribution or source incorporation requires explicit licence/compatibility review.

**FLIGHT-SIM-01 status: EXECUTED — architecture, dependency registry and index integration complete.** Live UE5/JSBSim/AirSim execution remains a separate environment-validation gate.

## Master indexed streams

The flight-simulation stream is now indexed under:
- `AERO` — aircraft, aerodynamics and flight simulation.
- `COMPUTE` — numerical simulation and reproducible engineering.
- `AI` / `ROBOTICS` — autonomy, sensors and intelligent control.
- `DIGITAL-TWIN` — simulation/telemetry/model lineage.
- `CG-3D` / `GEOMETRY` — aircraft geometry and visual assets.
- `VIDEO-SERIES` — simulator-derived research/showcase production.

## Existing repository status

All previously recorded department streams and integration gates remain active. No third-party proprietary simulator assets are represented as Biupiu-owned assets, and no live simulator execution is claimed without a connected/validated host.

## Version

**Biupiu R&D Research Index v3.5 — Flight Simulation Integration**
**Updated:** 19 September 2026

> Index synchronization note: This is the authoritative current index state for the flight-simulation integration. Historical gate records remain in their respective files.
