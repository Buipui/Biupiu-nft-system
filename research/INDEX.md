# Biupiu R&D Research Index

## RED-07 — Automated round-trip drift testing

Added `research/BIUPIU-ROUNDTRIP-DRIFT-RED-07-v1.0.md`, `packages/biupiu-render-pipeline/src/drift.ts`, the RED-07 round-trip fixture and contract test. The gate compares authoritative source signatures across SOURCE → PROVIDER → INTERCHANGE → PROVIDER → SOURCE, reports geometry/transform/material/metadata drift, and blocks source-identity or provenance drift. Live renderer round-trip acceptance remains gated on connected hosts and measured outputs.

**Version:** 3.7
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

## Graphics / Physics / Upscaling Integration — GPU-SYS-01

Added 19 September 2026:
- `research/GRAPHICS-PHYSICS-UPSCALING-GITHUB-RESOURCE-REGISTRY-v1.0.md` — current GitHub resource map and licence boundary.
- `research/GRAPHICS-PHYSICS-UPSCALING-DEPENDENCIES-v1.0.json` — machine-readable dependency registry.
- `private-rd-centre/docs/GRAPHICS-PHYSICS-UPSCALING-ADAPTER-CONTRACT-v1.0.md` — stable adapter interfaces for graphics, physics and reconstruction.
- `packages/biupiu-graphics-engine/package.json` — graphics abstraction package.
- `packages/biupiu-physics-engine/package.json` — Jolt/PhysX/Bullet abstraction package.
- `packages/biupiu-upscaling/package.json` — FSR/XeSS/research reconstruction abstraction package.

Registered references include Vulkan/DX12/DXR rendering, glTF, Jolt Physics, PhysX, Bullet/PyBullet, AMD FidelityFX/FSR, Intel XeSS, libplacebo and selected research-only upscaling projects.

**GPU-SYS-01 status: EXECUTED — registry, dependency manifest, adapter contracts and package definitions committed. Local compilation, GPU benchmarks and runtime acceptance remain validation gates.**

## Version

**Biupiu R&D Research Index v3.8 — Audit + Flight Simulation + Private Systems Physics + GPU Graphics/Reconstruction**
**Updated:** 19 September 2026

> Index synchronization note: This is the authoritative current index state for the flight-simulation integration. Historical gate records remain in their respective files.


## AI-23 open-resource and fail-closed gate
- `research/BIUPIU-AI-23-OPEN-RESOURCE-INTEGRATION-v1.0.md` — NASA, MIT and open-source resource provenance/licence boundary.
- `software/rnd-os-ai/src/biupiu_ai/open_resource_registry.py` — external resource registry.
- `software/rnd-os-ai/tests/test_ai23.py` — registry validation tests.
- `software/rnd-os-ai/src/biupiu_ai/gateway_service.py` — audit-store readiness and write-failure fail-closed handling.
- **AI-23 status:** resource registry, specification, tests and gateway safety boundary synchronized.


## AI-24 outbox and provenance gate
- `software/rnd-os-ai/src/biupiu_ai/audit_outbox.py` — bounded audit outbox with event deduplication and retry.
- `software/rnd-os-ai/tests/test_ai24.py` — outbox/retry tests.
- `research/BIUPIU-AI-24-OUTBOX-PROVENANCE-v1.0.md` — AI-24 production-boundary specification.
- **AI-24 status:** development outbox and provenance boundary implemented; production durable queue integration remains gated.


## AI-25 transactional audit and provenance gate
- `software/rnd-os-ai/src/biupiu_ai/transactional_audit.py` — transactional audit boundary and resource provenance validation.
- `software/rnd-os-ai/tests/test_ai25.py` — transactional/provenance tests.
- `research/BIUPIU-AI-25-TRANSACTIONAL-AUDIT-PROVENANCE-v1.0.md` — AI-25 specification.
- **AI-25 status:** transactional audit boundary implemented; GatewayService end-to-end integration remains the next gate.


## AI-26 gateway integration gate
- `software/rnd-os-ai/src/biupiu_ai/gateway_service.py` — transactional audit and resource provenance enforcement integrated into GatewayService.
- `software/rnd-os-ai/tests/test_ai26.py` — integration-boundary tests.
- `research/BIUPIU-AI-26-GATEWAY-INTEGRATION-v1.0.md` — AI-26 specification.
- **AI-26 status:** gateway integration committed; end-to-end GatewayService harness remains the next gate.


## OS / AI architecture separation — SEPARATION-01

Registered 19 September 2026:

- `research/BIUPIU-OS-AI-SEPARATION-ARCHITECTURE-v1.0.md` — canonical boundary between the Core OS and Biupiu AI.
- `software/RND-OS-V1.0-IMPLEMENTATION.md` — original R&D OS v1.0 designated as the Core OS Baseline.
- `software/rnd-os-ai/README.md` — intelligence-layer boundary retained separately.

### Canonical model

**Biupiu OS = stable core/integration layer.**

**Biupiu AI = modular intelligence layer.**

The layers remain integrated through explicit interfaces. AI cannot bypass OS validation, provenance or authoritative state controls.

**SEPARATION-01 status: EXECUTED — architecture separation registered and repository index synchronized.**

## Biupiu Intelligence Learning + Blockchain Core — INTEL-LEARN-01

Added the Intelligence learning/provenance foundation:
- `research/BIUPIU-INTELLIGENCE-LEARNING-LAYER-v1.0.md` — persistent learning-loop and knowledge-retention rules.
- `research/BIUPIU-INTELLIGENCE-LEARNING-SCHEMA-v1.0.json` — machine-readable learning record contract.
- `software/rnd-os-ai/src/biupiu_ai/learning.py` — deterministic learning-record hashing and verification primitives.
- `software/rnd-os-ai/tests/test_learning.py` — deterministic integrity and tamper-detection tests.
- `contracts/BiupiuLearningRegistry.sol` — optional on-chain checkpoint registry for approved learning lineage commitments.

### Core maintenance integration
Bug fixes, code updates, technology/dependency updates, security/configuration audits, index repairs, regression evidence and repository changes are now explicitly represented as learning events. Historical/experimental material remains preservable; duplicate-looking content is not automatically deleted.

### Blockchain boundary
Learning data remains off-chain by default. Only approved cryptographic checkpoints/commitments may be anchored on-chain. No private keys, prompts, raw datasets, confidential IP or model payloads are placed on-chain. The registry is not a claim of an independent Biupiu Layer-1.

**INTEL-LEARN-01 status: IMPLEMENTED — learning schema, deterministic provenance primitive, regression tests, AI architecture integration and blockchain checkpoint contract added. Live AI-provider execution, local model training and blockchain deployment remain environment-validation gates.**


## Lumion LUM-06 — unified visualization package

Added a machine-readable unified visualization package schema, example package, and specification. One validated source model plus approved asset manifests can now define coordinated Lumion, Unreal Engine 5, V-Ray and Blender targets, with shared scene/provenance metadata and renderer-specific profiles. **LUM-06 executed.**
