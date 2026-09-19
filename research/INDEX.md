# Biupiu R&D Research Index

## OPENAI-INTEL-01 — OpenAI Intelligence Architecture Integration

Added 19 September 2026:
- `research/BIUPIU-OPENAI-INTELLIGENCE-INTEGRATION-v1.0.md`
- `research/BIUPIU-OPENAI-RESOURCE-MANIFEST-v1.0.json`
- `software/rnd-os-ai/src/biupiu_ai/intelligence_core.py` — bounded agent task routing and fail-closed result validation.
- `software/rnd-os-ai/tests/test_openai_integration.py` — routing, approval, provenance and dependency-closure tests.

### Integrated patterns
OpenAI Agents SDK patterns: bounded agents, tools, handoffs/routing, guardrails, human approval, sessions and tracing.

OpenAI Evals patterns: evaluation-first development, regression testing, grounding, contradiction handling and reproducibility.

OpenAI Codex/Cookbook patterns: repository-aware planning, persistent project guidance, sandbox/workspace boundaries and iterative change verification.

### Biupiu algorithm update
`INTAKE → CLASSIFY → ROUTE → RETRIEVE → CHECK PROVENANCE → CONSTRAIN → EXECUTE/PROPOSE → TRACE → EVALUATE → REGRESS → LEARN → PROMOTE`

Core rule: **AI proposes; Core OS validates; evidence grounds; tests verify; humans control irreversible release.**

### Separation
**Biupiu OS = authoritative core/integration layer.**  
**Biupiu AI = modular intelligence layer.**

Third-party OpenAI source remains external until licence/security/compatibility/provenance/regression gates pass.

**OPENAI-INTEL-01 status: EXECUTED — architecture knowledge and compatible deterministic primitives integrated. Live provider execution remains an environment-validation gate.**

---

# Biupiu R&D Research Index

## RED-08 — Multi-provider asset equivalence matrix

Added `research/BIUPIU-PROVIDER-EQUIVALENCE-RED-08-v1.0.md`, `packages/biupiu-render-pipeline/src/equivalence.ts`, the RED-08 provider matrix fixture and contract test. The gate compares geometry, transforms, materials, metadata and provenance against one authoritative baseline across all registered render providers. Source identity/provenance variance blocks acceptance; other asset variance is classified as drift. Live provider equivalence remains gated on connected hosts and measured outputs.


## RED-07 — Automated round-trip drift testing

Added `research/BIUPIU-ROUNDTRIP-DRIFT-RED-07-v1.0.md`, `packages/biupiu-render-pipeline/src/drift.ts`, the RED-07 round-trip fixture and contract test. The gate compares authoritative source signatures across SOURCE → PROVIDER → INTERCHANGE → PROVIDER → SOURCE, reports geometry/transform/material/metadata drift, and blocks source-identity or provenance drift. Live renderer round-trip acceptance remains gated on connected hosts and measured outputs.

**Version:** 4.1
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

### PHYS-SYS-01 validation gate

- `private-rd-centre/tests/test_physics_kernel.py` — deterministic smoke tests for rigid-body, thermal and rotating-machine primitives.
- `.github/workflows/phys-sys-smoke.yml` — repeatable GitHub Actions smoke-test workflow triggered by private-R&D changes or manually.
- Current state: **TEST HARNESS REGISTERED**. The connector reports no commit status checks yet, so CI execution is not claimed as passed until GitHub Actions produces a run result.

### PHYS-SYS-02 numerical validation

- `private-rd-centre/tests/test_physics_benchmarks.py` — constant-force, zero-torque, thermal-equilibrium and rotating-machine equilibrium benchmarks.
- `.github/workflows/phys-sys-smoke.yml` now executes both the kernel smoke suite and numerical benchmark suite.
- Connector verification currently shows no GitHub Actions run for the relevant commits, so CI execution remains **unverified** until a workflow run is observed.

**PHYS-SYS-02 status: IMPLEMENTED — benchmark suite and CI registration complete; external/physical validation remains separate.**

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


## AERO-HANGAR-01 — Virtual Hangar + Digital Twin

Added `research/BIUPIU-AEROSPACE-VIRTUAL-HANGAR-DIGITAL-TWIN-v1.0.md`. The private Virtual Hangar provides a multi-vehicle simulation architecture for eVTOL, helicopters, UAVs, drones, fixed-wing aircraft and jets. NASA, public DARPA research, ResearchGate and Emerald research patterns are mapped into Aerospace, Physics Systems, Compute, AI, Robotics, Avionics, CG-3D, Materials, Manufacturing, Energy, HMI, CODEX, Digital Twin and Testing. Existing FS2002/MSFS 2024 simulator tracks feed the Hangar. **AERO-HANGAR-01: ARCHITECTURE REGISTERED.**


## OS/AI Interface Contract — SEPARATION-02

Added 19 September 2026:
- `research/BIUPIU-OS-AI-INTERFACE-CONTRACT-v1.0.md` — explicit boundary for OS context, AI proposals, validation, audit and authoritative state.
- `software/rnd-os-ai/README.md` — updated to Biupiu AI Intelligence Layer v1.1.

**SEPARATION-02 status: EXECUTED — interface contract registered and AI boundary implementation documentation synchronized. Runtime end-to-end execution remains a separate validation gate.**


## Lumion LUM-07 — automated package build and validation

Added `.github/workflows/visualization-package-validation.yml` plus `research/visual-assets/VISUALIZATION-PACKAGE-BUILD-v1.0.md`. The repository now has a read-only CI validation workflow for visual-asset JSON syntax, JSON Schema 2020-12 metadata, validator-script syntax and package integrity reporting. **LUM-07 executed.**


## Global Intelligence Architecture Resource Audit — INTEL-GLOBAL-01

**Date:** 19 September 2026  
**Status:** IMPLEMENTED — research audit, architecture extension and deterministic core primitives registered.

### Sources reviewed
- NASA Open Source Software and NASA-IMPACT scientific-AI/orchestration projects.
- MIT OpenCourseWare AI/ML/deep-learning material.
- Wits AI/ML/reinforcement-learning research references.
- Open GitHub knowledge-graph, grounded-RAG, literature-provenance and knowledge-management projects.
- Open educational/book resources including Harvard CS249r Machine Learning Systems.

### Core changes
- Hybrid lexical + semantic + graph retrieval contract.
- Typed evidence graph with SUPPORTS / CONTRADICTS / REFINES / BUILDS_ON / DERIVED_FROM / TESTS / PRODUCES / DEPENDS_ON relations.
- Explicit UNSUPPORTED evidence state and fail-closed grounding primitive.
- Dependency-impact closure primitive for change analysis.
- Evaluation requirements expanded to grounding, contradiction detection, unsupported-claim refusal, regression and reproducibility.
- External-resource provenance/licence registry.
- Scientific lifecycle orchestration linked to the learning layer.

**Files:**
- `research/BIUPIU-INTELLIGENCE-RESOURCE-AUDIT-2026-09-19.md`
- `research/BIUPIU-INTELLIGENCE-ARCHITECTURE-v1.2.md`
- `research/BIUPIU-INTELLIGENCE-RESOURCE-REGISTRY-v1.0.json`
- `software/rnd-os-ai/src/biupiu_ai/intelligence_core.py`
- `software/rnd-os-ai/tests/test_intelligence_core.py`

**Boundary:** third-party projects are references until individual licence, provenance, security and compatibility review. No third-party code is represented as Biupiu-owned merely because it was discovered.


## AI Consciousness / Self-Awareness Boundary — CONSCIOUSNESS-BOUNDARY-01

Added 19 September 2026:
- `research/BIUPIU-AI-CONSCIOUSNESS-BOUNDARY-v1.0.md` — hard-core architectural and human-factors boundary.

### Protected distinction
Biupiu must distinguish intelligence/capability, learning, memory, self-monitoring and permissioned autonomy from subjective consciousness or sentience. Behaviour that appears self-aware is not to be presented as proof of consciousness.

### Real-world deployment rule
Factory, robotics, laboratory, vehicle and other physical deployments must communicate this distinction plainly. AI remains permissioned, logged and revocable; physical safety controls remain independently enforceable; AI is not treated as a person or substitute for human authority.

### Governance
The boundary cannot be silently changed by an AI learning loop, agent, model update or automated repository process. Any future consciousness-related claim requires explicit human review plus scientific evidence and reproducible testing.

**CONSCIOUSNESS-BOUNDARY-01 status: HARD CORE — REGISTERED AND COMMITTED.**


## 3D Open Engineering Resource Integration — 3D-OPEN-01

Added:
- `research/BIUPIU-3D-OPEN-RESOURCE-INTEGRATION-v1.0.md`
- `research/BIUPIU-3D-OPEN-RESOURCE-MANIFEST-v1.0.json`
- `packages/biupiu-3d-engine/`

Integrated external references include OpenSCAD, FreeCAD, Blender, build123d, BelfrySCAD, CADAM and PythonSCAD, plus open engineering-mechanics references. Third-party repositories remain external references; only Biupiu-authored adapter/generator code and concept templates are committed.

Reusable code now covers:
- validated renderer-neutral 3D model manifests;
- OpenSCAD generation;
- bounding-radius scale checks;
- micro-turbine, marine-propulsor and eVTOL conceptual blockouts.

Routing: **GEOMETRY, COMPUTE, AERO, MARINE, ENERGY, COMPOSITES, MATERIALS, ADV-MFG, ROBOTICS, DIGITAL-TWIN, AI, NFT-ART and NFT-PROV**.

**3D-OPEN-01 status: EXECUTED — repository integration committed. Runtime CAD-host compilation and physical/engineering validation remain separate gates.**


## FARM-SIM-01 — Farming Simulator / Smart Farming Integration

Added 19 September 2026:
- `research/BIUPIU-FARMING-SIMULATOR-RESOURCE-REGISTRY-v1.0.md` — Farming Simulator/FS25 external resource and open-access knowledge registry.
- `smart-farming/online-platform/SF37-FARMING-SIMULATOR-DIGITAL-TWIN-BRIDGE-v1.0.md` — normalised telemetry/control boundary and Digital Twin adapter architecture.
- `smart-farming/online-platform/SF38-FARMING-SIMULATOR-RESOURCE-MAP.md` — source-to-function mapping.
- `world/environments/BIUPIU-FARMING-SIMULATION-ARCHITECTURE-v1.0.md` — simulator-agnostic World farming architecture and agricultural virtual test tracks.

Mapped reference classes include FS25 tooling, telemetry, field automation, precision agriculture, harvesting, logistics, farm management and map-building. Open-access/educational references cover crop/soil modelling, sensing, irrigation, UAV/ML and intelligent machinery.

The integration is **adapter-first**: third-party code/assets remain external until licence, security and compatibility review passes. Farming Simulator is not made a hard dependency of Biupiu World.

**FARM-SIM-01 status: EXECUTED — research/resource registry, Digital Twin bridge, World architecture and resource map committed. Live simulator/adapter execution remains a host-validation gate.**


## MARINE-SIM-01 — Marine Simulation + Virtual Boatyard / Sea-Test Integration

Added 19 September 2026:
- `research/BIUPIU-MARINE-SIMULATION-RESOURCE-REGISTRY-v1.0.md` — NVIDIA WaveWorks and open marine-simulation resource map.
- Virtual boatyard/workshop architecture: CAD/design, hull Digital Twin, materials/composites, propulsion, electrical/automation, fabrication, inspection, work orders and showreel workflows.
- Virtual sea-testing architecture: calm water, coastal conditions, wind/current/wave matrices, maneuvering, propulsion, sensor/autonomy and deterministic telemetry scenarios.

Mapped references include NVIDIA WaveWorks (external/proprietary reference), HonuRobotics/gz-maritime, LSTS/gazebo-sim/asv_wave_sim, Naval Group LOTUSim, MARSIM, Plankton and VRX/Gazebo marine simulation. Professional ship simulators and Seafarer: The Ship Sim are observational/reference products only; proprietary code and assets are not represented as Biupiu-owned.

Routing: **MARINE, PHYS-SYS, DIGITAL-TWIN, ROBOTICS, AI, COMPUTE, CG-3D, GEOMETRY, ADV-MFG, MATERIALS, COMPOSITES, ENERGY, VIDEO-SERIES and BIUPIU-WORLD**.

**MARINE-SIM-01 status: ARCHITECTURE + RESOURCE INDEX REGISTERED.** Runtime compilation, wave/dynamics calibration and physical sea-trial validation remain separate gates. Third-party code/assets remain external pending licence, security and compatibility review.


## FARM-SIM-02 — Adapter Contract + Scenario Validation Gate

Added 19 September 2026:
- `smart-farming/online-platform/SF39-FARMING-SIMULATOR-ADAPTER-CONTRACT-v1.0.md` — simulator-neutral interfaces and fail-closed integration rules.
- `smart-farming/online-platform/SF40-FARMING-SIMULATOR-SCENARIO-SUITE-v1.0.json` — deterministic scenario definitions for soil regeneration, irrigation, autonomous navigation, harvesting, greenhouse automation, drought stress, logistics and historical farming.
- `research/BIUPIU-FARM-SIM-VALIDATION-GATE-v1.0.md` — G1–G7 validation framework from resource identity/licence through Digital Twin and World promotion.

**FARM-SIM-02 status: ARCHITECTURE EXECUTED.** Runtime-connected validation remains open because no connected Farming Simulator host/telemetry endpoint was executed in this gate.


## MARINE-SIM-02 — Virtual Boatyard / Sea-Test Adapter Contract

Added 19 September 2026:
- `research/BIUPIU-MARINE-SIM-02-BOATYARD-SEATEST-ADAPTER-CONTRACT-v1.0.md` — adapter-first contract for vessel models, ocean/waves, hydrodynamics, sensors, workshop state, deterministic sea tests and Digital Twin provenance.
- Virtual boatyard zones: CAD review, dry dock/slipway, fabrication, composites, propulsion, electrical/automation, finishing, crane/lift, QA and launch/recovery.
- Virtual sea-test zones: harbour, coastal, deep-water, wave/current/wind matrices, maneuvering, propulsion endurance, sensor/autonomy proving and recovery scenarios.

The contract explicitly separates third-party references from Biupiu-owned implementation and requires model/environment/scenario/configuration/telemetry provenance for accepted simulation results.

**MARINE-SIM-02 status: EXECUTED — adapter contract and virtual boatyard/sea-test architecture registered and verified in repository. Runtime host compilation, solver calibration and physical validation remain open gates.**


## Intelligence Core Test Gate — INTEL-TEST-01

Added `.github/workflows/intelligence-core-tests.yml`.

The workflow installs pytest in a clean Python 3.13 runner and executes the learning/intelligence regression suite plus AI-23 through AI-27 tests. The workflow is intentionally read-only and has `contents: read` permission.

**INTEL-TEST-01 status: TEST WORKFLOW REGISTERED.** Repository connector read-back confirms the workflow commit exists, but no GitHub Actions run has yet been returned for that commit, so CI PASS is not claimed.

## AI-27 end-to-end gateway test gate
- `software/rnd-os-ai/tests/test_ai27.py` — deterministic authentication, provenance, provider-execution, replay/idempotency and audit-failure harness.
- `research/BIUPIU-AI-27-GATEWAY-E2E-HARNESS-v1.0.md` — AI-27 scope and production boundary.
- **AI-27 status:** IMPLEMENTED — harness committed and read back. Test execution remains unverified until CI or a connected Python runner reports a pass.

## AERO-HANGAR-02 — Environment validation gate

The Virtual Hangar now has explicit pre-simulation validation requirements covering the vehicle Digital Twin schema, L0–L5 fidelity transitions, simulator-version isolation, telemetry/provenance records, simulation-only AI/robotics outputs, replayable test scenarios and authoritative department cross-links. **AERO-HANGAR-02: EXECUTED.**

## MATH-01 — Problem-Solving + Formal Verification Layer

Added 19 September 2026:
- research/BIUPIU-MATH-PROBLEM-SOLVING-FORMAL-VERIFICATION-v1.0.md
- software/rnd-os-ai/src/biupiu_ai/math_problem_solver.py
- software/rnd-os-ai/tests/test_math_problem_solver.py
- .github/workflows/math-problem-solver-validation.yml

The MATH layer provides deterministic problem classification, invariant checks and numerical residual verification, with an explicit adapter boundary for formal theorem proving and downstream simulation. It is routed through AI, COMPUTE, GEOMETRY, ROBOTICS, DIGITAL-TWIN, AERO, MARINE, ENERGY, MATERIALS, PHOTONICS, AGRI, WATER and BIOMED as applicable.

**MATH-01 status: IMPLEMENTED — core primitives and CI validation registered. External formal-prover execution and domain-specific validation remain separate gates.**


## INTEL-LEARN-02 — Repeated Gate Learning + Conflict Resolution Matrix

Added 19 September 2026:
- `research/BIUPIU-GATE-LEARNING-ARCHITECTURE-v1.0.md`
- `research/BIUPIU-GATE-LEARNING-MATRIX-v1.0.json`
- `research/BIUPIU-OPEN-RESOURCE-AUDIT-2026-09-19-v2.0.md`

Repeated execution is now treated as structured evidence collection rather than repetition alone. Gates capture state, expected/observed outcomes, conflict class, root-cause evidence, fix/version, tests, regression scope, dependency impact, provenance and promotion status. Repeating a gate without new evidence is classified as a stalled loop.

### New learning matrix
G0 PLAN → G1 EXECUTE → G2 DIAGNOSE → G3 FIX → G4 VERIFY → G5 REGRESS → G6 LEARN → G7 PROMOTE.

Learning maturity: L0 logged, L1 classified, L2 fix verified, L3 regression covered, L4 reusable pattern, L5 preventative test generated.

### Intelligence architecture integration
Biupiu Intelligence now treats bug-fix and regression evidence as reusable diagnostic knowledge. Dependency-impact closure can route changes across OS, AI, COMPUTE, MATH, GEOMETRY, ROBOTICS, PHYS-SYS, DIGITAL-TWIN, CG-3D, AERO, MARINE, ADV-MFG, MATERIALS, BLOCKCHAIN, NFT/IP and relevant domain systems.

### New open-source research radar
The audit records candidate references including memory services, AI evaluation/observability, agent orchestration, knowledge/RAG and Digital Twin/autonomous-system simulation projects. They remain reference-only until licence, security, dependency and compatibility gates pass.

**INTEL-LEARN-02 status: ARCHITECTURE + MATRIX + RESOURCE AUDIT COMMITTED.** Runtime execution, third-party import, CI pass and physical validation remain separately verified gates.

## Index synchronization
**Research Index v4.0 — Gate Learning / Conflict Resolution / Open Resource Audit**  
**Updated:** 19 September 2026


## WORLD-HUB-01 — Main Hub Runtime Resource Gate

Added 19 September 2026:
- `world/client/` — executable Babylon.js Main Hub prototype client.
- `world/client/src/routeManifest.ts` — route manifest aligned to the canonical Main Hub scene and destination-gate policy.
- `world/client/src/destinationLoader.ts` — fail-closed destination routing boundary; it returns route intent/metadata and does not bypass authorization.
- `world/client/src/main.ts` — updated scene bootstrap with gate-selection routing hooks.
- `world/environments/BIUPIU-MAIN-HUB-RUNTIME-RESOURCE-MANIFEST-v1.0.json` — runtime resource and provenance manifest.
- `research/BIUPIU-EXTERMINATE-PROTOCOL-MAIN-HUB-v1.0.md` — non-destructive defect/conflict cleanup record.

Current external runtime check: Babylon.js `@babylonjs/core` and `@babylonjs/loaders` 9.27.1 are current package releases observed during this gate. citeturn0search2turn0search4

**WORLD-HUB-01 status: EXECUTED — dependency refresh, fail-closed route boundary, runtime manifest and index synchronization committed. Local npm install/build and browser execution remain host-validation gates.**

## Index synchronization
**Research Index v4.2 — Main Hub Runtime / Exterminate Gate**  
**Updated:** 19 September 2026


## MICROSOFT-DISCOVERY-INTEL-01 — Discovery Architecture Integration
Added 19 September 2026:
- `research/BIUPIU-MICROSOFT-DISCOVERY-INTEGRATION-v1.0.md`
- `research/BIUPIU-MICROSOFT-DISCOVERY-RESOURCE-MANIFEST-v1.0.json`
- `research/BIUPIU-INTELLIGENCE-ARCHITECTURE-v1.3.md`
- `software/rnd-os-ai/src/biupiu_ai/discovery_architecture.py`
- `software/rnd-os-ai/src/biupiu_ai/intelligence_core.py`
- `software/rnd-os-ai/tests/test_discovery_architecture.py`

Integrated architecture patterns: research task DAGs, dependency-aware execution, explicit task lifecycle, specialist agent routing, tool capability registry, autonomy/approval gates, evidence/provenance control, failure preservation and governed promotion.

**Exterminate result:** malformed intermediate Intelligence-core edit was detected during repository inspection and replaced with a clean deterministic implementation. No Microsoft source code was copied.

**Current gate:** architecture integrated; source-level repair complete; runtime CI and full licence/security validation remain environment gates.

**Next gate:** execute local/runtime regression, then expand the task graph into the AI OS/Main OS/Biupiu OS adapter contracts and perform full repository-wide integration verification.


## DISCOVERY-FLOW-02 — Unified Research Orchestration Gate
Added 19 September 2026.

The Microsoft Discovery-compatible task graph is now treated as a reusable orchestration pattern across Biupiu Intelligence rather than a standalone research feature. It connects task decomposition, dependency closure, evidence retrieval, specialist routing, simulation/experiment branches, evaluation, learning and governed promotion.

### Fluid protocol rule
Protocols are **composable stages**, not rigid linear scripts. A task may branch, loop back, spawn dependent tasks, become stale, be contradicted, or return to retrieval/evaluation without losing provenance. The authoritative OS boundary remains the convergence point.

### Canonical flow
INTAKE → CLASSIFY → DECOMPOSE → TASK GRAPH → RETRIEVE → CROSS-LINK → PROVENANCE → ROUTE → EXECUTE/SIMULATE → EVALUATE → REGRESS → LEARN → PROMOTE

### Gate status
ARCH-FLOW-02: ARCHITECTURE INTEGRATED. Runtime execution and platform CI remain validation gates.


## WORLD-ENGINE-02 / SEPARATION-03 — World Engine Learning Separation + Digital Twin Promotion
Added 19 September 2026:
- `research/BIUPIU-WORLD-ENGINE-SEPARATION-03.md` — canonical separation of external research, Biupiu Intelligence, AI OS, Main OS, Digital Twin and department promotion.
- `research/BIUPIU-DIGITAL-TWIN-PROMOTION-CONTRACT-v1.0.md` — release-manifest and Digital Twin acceptance boundary.
- `research/BIUPIU-WORLD-ENGINE-PROMOTION-MATRIX-v1.0.json` — machine-readable classification, routing and promotion matrix.
- `research/BIUPIU-WORLD-ENGINE-RESOURCE-MANIFEST-v1.0.json` — expanded engine-resource separation routes.

### Canonical flow
RESEARCH → INTELLIGENCE → AI OS PROPOSAL → MAIN OS VALIDATION → RELEASE MANIFEST → DIGITAL TWIN → RELEVANT DEPARTMENT ADAPTERS

External resources are classified as REFERENCE, PATTERN, ADAPTER, ASSET, DEPENDENCY or PROHIBITED. No external resource is promoted directly into authoritative state. Licence/IP, security, compatibility, deterministic tests, provenance and human release authority remain mandatory promotion gates.

Routing now explicitly covers CG-3D, RENDER, PHYS-SYS, NAVIGATION, ROBOTICS, AI, COMPUTE, AERO, MARINE, ADV-MFG, MATERIALS, AGRI, WATER, PHOTONICS and VIDEO-SERIES where relevant. Revoked manifests must be blocked by the Main OS boundary and removed from downstream consumption.

**SEPARATION-03 status: ARCHITECTURE COMMITTED.** Repository integration is complete; runtime/CI, connected-host and Digital Twin execution evidence remain separate validation gates.

## Index synchronization
**Research Index v4.3 — World Engine Separation / Digital Twin Promotion**  
**Updated:** 19 September 2026
