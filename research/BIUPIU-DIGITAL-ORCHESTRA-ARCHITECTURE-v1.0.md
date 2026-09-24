# BIUPIU DIGITAL ORCHESTRA ARCHITECTURE v1.0

Date: 2026-09-22
Status: SOURCE IMPLEMENTED / RUNTIME VERIFICATION PENDING

A separate, interlinked orchestration system that coordinates Biupiu's increasingly connected software estate without collapsing authority boundaries.

## Layers
1. Conductor — smallest useful route.
2. Workflow graph — declarative steps, dependencies, conditions and recovery.
3. Capability registry — machine-readable modules, interfaces and runtimes.
4. Evidence/provenance bus — source, language, licence, commit, evidence state and validation.
5. Execution journal — append-only event/correlation record.
6. Filing system — canonical placement plus cross-references.
7. Verification gates — L0-L9 aligned to the native coding matrix.
8. Learning bridge — failed/successful patterns become evidence.
9. Federation adapter — governed envelopes; never bypasses OS/DMS authority.

## Canonical flow
RESEARCH / EXTERNAL HARVEST -> CLASSIFY -> CONDUCT -> EXECUTE -> OBSERVE -> VERIFY -> DIGEST -> FILE -> LEARN -> GOVERNED PROMOTION

## Interlinks
Native Coding Matrix; Intelligence; OS/DMS; Digital Twin; Federation; Simulators; Repository; Biupiu World.

## Event envelope
event_id, correlation_id, source, target, schema_version, timestamp, evidence_state, provenance_refs, source_commit, validation_state, payload_hash.

## Failure philosophy
Never silently retry a semantic failure. Distinguish transport, dependency, contract, validation, authority, model and data failures. Quarantine unknown or unlicensed executable material.

Runtime: source seed committed; host execution, package tests, CI integration and cross-system runtime remain separate gates.

## Filing Cabinet + hierarchy/federation integration — Gate 34
Orchestra routes filing, twin and federation workflows but does not absorb their authority.
Digital Filing Cabinet = catalogue authority.
Digital Twin = contextual composition authority.
Federation = inter-system discovery/link/reconciliation authority.
Canonical owner = execution authority for its own subsystem.
Fault-healing orchestration = federated diagnosis + governed local execution.

## 2026-09-24 — Information-Stack Family Orchestra + Resource Split

The Orchestra now allocates work by **software-family tree**, not by superficial module name. A family carries its compatible language/runtime, ABI, dependencies, OEM/provider boundary, hardware target, build/test surface, provenance, optimisation class and learning graph together.

### Family orchestration hierarchy

HUMAN RELEASE AUTHORITY
-> CORE OS / DMS VALIDATION
-> NATIVE BIUPIU INTELLIGENCE
-> DIGITAL ORCHESTRA
-> FEDERATION FOUR AI SLOTS
-> SOFTWARE-FAMILY OWNER
-> DOMAIN/SPECIALIST CAPABILITY
-> OEM / PROVIDER ADAPTER
-> HARDWARE / RUNTIME SURFACE

The canonical four Federation AI identities remain the active slots; their final identity-to-family ownership mapping remains discovery-controlled and is not invented from the eight specialist resource teams.

### Information-stack layers

| Stack | Orchestra responsibility | Primary resource family |
|---|---|---|
| Evidence / provenance | source identity, language, licence, commit, evidence class | RESEARCH-EVIDENCE |
| Intelligence | reasoning, retrieval, task graph, proposal, learning | AI-ORCHESTRATOR |
| Federation | cross-family routing, challenge, reconciliation, evidence exchange | FEDERATION |
| OS / DMS | authority, identity, policy, package/runtime, promotion gate | CORE-OS / DMS |
| Math / Physics | numerical, geometry, simulation and optimisation | MATH-PHYSICS |
| Digital Twin | state/model/event/calibration/replay | SIMULATION-DIGITAL-TWIN |
| Code systems | compiler, ABI, build, semantic and regression surfaces | CODE-SYSTEMS |
| Security | quarantine, secure execution, rollback, fail-closed boundaries | SECURITY-EXTERMINATE |
| Hardware / OEM | CPU/GPU/NPU/DSP, NEON, Vulkan/OpenCL, OEM SDK boundaries | MULTIMODAL-CONFIGURATION |
| Provenance | hashes, manifests, blockchain anchors | BLOCKCHAIN-PROVENANCE |
| Filing | catalogue, canonical placement, cross-reference | DIGITAL-FILING |
| World / presentation | approved assets/contracts/twin state; presentation only | WORLD / UE |

### Family ownership rule

A software family is kept as a **complete stack** when practical:

SOURCE -> BUILD -> TEST -> DEPENDENCY -> ADAPTER -> HARDWARE TARGET -> RUNTIME -> EVIDENCE -> LEARNING

Shared resources are referenced through canonical contracts; they are not cloned into each family.

### Existing family split

- Core / ABI / HAL: C + Rust + C++ boundary, owned by Core OS/DMS.
- Native Intelligence / ML: Python/native AI plus typed contracts; AI-ORCHESTRATOR.
- Federation contracts: TypeScript/domain contracts; FEDERATION.
- Android: Kotlin/Android + native bridge; MULTIMODAL-CONFIGURATION with CODE-SYSTEMS support.
- Physics / geometry / scientific compute: C++ plus C ABI/Rust boundary; MATH-PHYSICS.
- Digital Twin / simulation: model/state/event contracts and simulator adapters; SIMULATION-DIGITAL-TWIN.
- Windows/desktop: WPF/.NET; CODE-SYSTEMS / platform family.
- Digital Orchestra: Python workflow/orchestration; ORCHESTRA itself owns coordination state, not domain execution.
- Digital Filing: filing/index metadata only; DIGITAL-FILING.
- Blockchain/NFT: Solidity/provenance boundary; BLOCKCHAIN-PROVENANCE.
- World/UE: presentation/runtime provider boundary; WORLD / UE.

### Optimisation and learning resources

Optimisers stay attached to the family whose workload they optimise:
- scheduling/routing -> AI-ORCHESTRATOR + Federation;
- NEON/SIMD/GPU/NPU/DSP -> MULTIMODAL-CONFIGURATION + MATH-PHYSICS;
- sparse/geometry/numerical/alignment -> MATH-PHYSICS;
- ML hyperparameter/portable inference -> AI-ORCHESTRATOR;
- compiler/LLVM/Clang/AutoFDO -> CODE-SYSTEMS;
- Digital Twin resource optimisation -> SIMULATION-DIGITAL-TWIN;
- security/rollback optimisation -> SECURITY-EXTERMINATE.

Learning graphs follow the same family boundary and exchange only through the evidence/provenance contract.

### Event/resource envelope

Every family work item should carry:
family_id, software_tree, language, runtime, abi, dependencies, licence_state, oem_provider, hardware_target, optimisation_family, learning_graph, build_surface, test_surface, provenance_refs, authority_owner, evidence_state, promotion_state.

This prevents resource splitting from severing dependencies or learning lineage.

### PC gate

This information-stack allocation is architecture/source state only. PC execution remains deferred until the current non-PC gates are closed.
