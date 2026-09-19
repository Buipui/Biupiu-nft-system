# Biupiu R&D Research Index

**Version:** 3.6
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

## AI × Blockchain × Algorithm Integration — AI-BLOCKCHAIN-01

Added 19 September 2026:
- `research/BIUPIU-AI-BLOCKCHAIN-ALGORITHM-INTEGRATION-v1.0.md` — cross-department integration architecture.
- `research/BIUPIU-AI-BLOCKCHAIN-RESOURCE-MANIFEST-v1.0.json` — machine-readable reusable-resource manifest.

Mapped streams:
- AI / Buipiu Intelligence — persistent memory, agents, policy, verification and efficient orchestration.
- COMPUTE / Algorithms — hard constraints, optimization, zkVM and reproducible execution.
- ROBOTICS / PHYS-SYS — constrained control and simulation-before-physical execution.
- PRIVATE-RD / DIGITAL-TWIN / CG-3D — simulation-ready scene generation and model lineage.
- AERO / MARINE / ADV-MFG / MATERIALS — constrained design, CAD reconstruction and scientific optimization.
- AGRICULTURE / WATER / CONSERVATION / CLIMATE — NASA geospatial and weather foundation-model references.
- BLOCKCHAIN / NFT / IP — provenance, hash anchoring, verification and controlled agent transaction research.

**AI-BLOCKCHAIN-01 status: EXECUTED — research resources isolated, indexed and cross-linked. Third-party code remains external pending licence/security review.**

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

## Private Biupiu World R&D Centre — PHYS-SYS-01

A private owner-only research layer has been added at `private-rd-centre/`. It is intentionally separated from the customer-facing Biupiu World product layer.

- `private-rd-centre/README.md` — isolation, lifecycle and operating rules.
- `private-rd-centre/engine/physics_kernel.py` — dependency-free prototype physics kernel for rigid-body, thermal and rotating-machine models.
- `private-rd-centre/models/model-registry.json` — cross-domain physics model registry.
- `private-rd-centre/models/rigid-body-6dof.json` — reusable 6-DoF model contract.
- `private-rd-centre/models/thermal-lumped.json` — reusable thermal model contract.
- `private-rd-centre/models/rotating-machine.json` — rotating machinery model contract.
- `private-rd-centre/docs/PHYS-SYS-01-ARCHITECTURE-v1.0.md` — systems physics and Digital Twin architecture.
- `private-rd-centre/promotion/WORLD-PROMOTION-GATE-v1.0.md` — explicit owner-controlled promotion gate.

### Physics-system scope

The physics layer is intended to support aerospace/eVTOL, automotive, marine, robotics, energy, manufacturing, water/agriculture and advanced-material systems. Flight simulation is an adapter/application, not the whole engine.

### Privacy/product boundary

The repository records this as a private R&D namespace, but GitHub directory naming alone does not provide access control. Confidential or unpublished IP should be stored in a genuinely private repository/storage location. Customer builds must consume only explicit `WORLD` release manifests; no automatic promotion is permitted.

**PHYS-SYS-01 status: IMPLEMENTED — architecture, prototype kernel, model contracts and promotion gate committed. Domain validation and integration with full external solvers remain future validation gates.**

## Version

**Biupiu R&D Research Index v3.8 — Audit + Flight Simulation + Private Systems Physics Centre**
**Updated:** 19 September 2026

> Index synchronization note: This is the authoritative current index state for the flight-simulation integration. Historical gate records remain in their respective files.


## AUTO-CUSTOM-03 — NEXT GATE EXECUTION
**Executed:** 19 September 2026

Production integration gate prepared: modular Unreal/Blender pipeline, attachment-point validation, Digital Twin runtime binding, and original Biupiu parametric component generation are now the next implementation targets. Third-party NFSU2/Forza assets remain excluded unless separately licensed.
