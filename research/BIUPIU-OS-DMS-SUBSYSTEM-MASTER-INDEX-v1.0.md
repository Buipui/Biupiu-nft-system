# Biupiu OS / DMS / Subsystems Master Index v1.0

**Date:** 19 September 2026  
**Status:** Integrated architecture registry — implementation and runtime gates remain distinct

## Purpose

Canonical registry for the **Biupiu OS**, **Biupiu DMS**, Digital Twin services and the major subsystem families that depend on them. This index prevents OS, DMS, enterprise, simulation and departmental components from becoming disconnected architecture records.

## Master system position

`BIUPIU OS CORE -> DMS CONTROL PLANE -> ENTERPRISE CONTROL -> DIGITAL TWIN / CONTEXT -> AI / SIMULATION / COMPUTE -> DOMAIN SUBSYSTEMS -> APPLICATIONS / WORLD -> CONTROLLED ACTUATION`

The NFT repository remains the current architecture/reference repository; this registry does not claim that a production OS, production DMS or physical-control system is already deployed.

## 1. Biupiu OS

### Core
- Kernel / boot foundation
- HAL and architecture abstraction
- memory and process/runtime contracts
- device/firmware boundaries
- filesystem/storage abstraction
- networking and IPC boundaries
- security and identity boundary
- package/runtime services
- cross-platform compatibility

### Platform targets
- x86_64
- ARM64
- RISC-V64
- legacy x86 adapter
- Linux / Unix / POSIX
- Ubuntu
- Windows compatibility boundary
- Darwin/macOS compatibility boundary
- Android / Web client boundaries

### Compatibility contracts
- ELF/Linux
- Mach-O/Darwin
- PE/Windows
- POSIX/Unix APIs
- platform-neutral Biupiu SDK interfaces

## 2. Biupiu DMS

**DMS = Digital Management System / control plane for Biupiu's governed digital systems.**

### DMS subsystems
1. Identity & access
2. Organisation / user / role registry
3. Entitlement and policy
4. Project / workspace management
5. Research and evidence registry
6. Asset registry
7. Digital Twin registry
8. Twin state/event management
9. Dataset and provenance registry
10. Model/version registry
11. Device/site registry
12. Telemetry/context gateway
13. Simulation job registry
14. AI/algorithm service registry
15. Workflow / gate orchestration
16. Manufacturing / production records
17. Inventory / supply-chain interfaces
18. Quality / maintenance interfaces
19. IP / prior-art / licence records
20. Financial/commercial records
21. Audit / security logs
22. Notification/event bus
23. API / adapter gateway
24. Repository and release metadata

## 3. Digital Twin subsystem

Canonical contracts:
- DigitalTwinRef
- TwinEvent
- observed / desired / computed / simulated / validated / actuated state separation
- model version
- evidence state T0-T9
- provenance lineage
- calibration and validation records

The Digital Twin is an integration service, not a replacement for the OS or DMS.

## 4. Intelligence subsystem

- retrieval
- evidence graph
- research orchestration
- AI/ML services
- mathematical reasoning
- optimisation
- uncertainty handling
- bounded agents
- learning/gate records
- governed promotion

AI remains modular and replaceable.

## 5. Simulation / engineering subsystem

- physics
- mathematics
- computational geometry
- CAD
- CFD/FEA
- robotics
- agriculture
- automotive
- marine
- aerospace
- manufacturing
- visual/3D
- Biupiu World
- simulator-specific adapters

## 6. Departmental subsystem registry

Department services remain independently deployable where practical and integrate through contracts/events:

BIO, BIO-GEN, AGRI, HEMP, BIOCARBON, BIOCHEM, TEXTILES, COAT, COMPOSITES, MATERIALS, WATER, ENERGY, ELECTROMAG, PHOTONICS, PH-QPM, CRM, METAMATERIALS, AERO, MARINE, COMPUTE, MATH, AI, GEOMETRY, DIGITAL-TWIN, ROBOTICS, ADV-MFG, BIOMED, GEOARCH, LAND-GIS, ALA, AAT, AAT-H, PALAEO-COAST, EMPIRE-CULTURE, NAGA-HIM, OLMEC-AMR, PRE-DISASTER, GEO-MAG, SPEC, IP, NFT-ART and NFT-PROV.

## 7. Cross-system contracts

`OS -> DMS`  
Runtime identity, storage, process, network and device services.

`DMS -> Digital Twin`  
Identity, asset ownership, state, event, model and provenance references.

`DMS -> Departments`  
Authorisation, project context, data access, workflow and provenance.

`Digital Twin -> Simulators`  
Versioned model/state/event interfaces.

`MATH/COMPUTE/AI -> Domain systems`  
Deterministic, numerical, optimisation and AI services with explicit evidence class.

`Repository -> DMS`  
Source/version/provenance metadata; repository contents are not automatically promoted to validated knowledge.

## 8. Security / provenance rule

Unknown permissions fail closed. Secrets and private keys remain outside public research records. External open-source projects are references/adapters until dependency, licence, security and compatibility gates pass.

## 9. Extermination gate

`DISCOVER -> DEPENDENCY/LICENSE -> SCHEMA -> CONTRACT -> SECURITY/PROVENANCE -> STATIC/UNIT -> INTEGRATION -> INDEX -> COMMIT -> RELEASE GATE`

A passed architecture gate does not imply runtime deployment.

## 10. Canonical repository references

- `research/BIUPIU-OS-INDEX-v1.1.md`
- `enterprise/BIUPIU-ENTERPRISE-INDEX-v1.0.md`
- `enterprise/BIUPIU-ENTERPRISE-DIGITAL-TWIN-SYSTEM-v1.0.md`
- `dms/ARCHITECTURE-v1.0.md`
- `packages/biupiu-rnd-os/DIGITAL-TWIN-DMS-ADAPTER-v1.0.md`
- `research/BIUPIU-DEPARTMENT-INDEX.md`
- `research/BIUPIU-R&D-OS-SOFTWARE-ARCHITECTURE-v1.0.md`

## Status

**OS, DMS and subsystem architecture are now registered as one linked system-of-systems.** Implementation, CI, VM boot, authenticated transport, live telemetry, production security, database migration and physical-actuation validation remain separate gates.


## 11. Machine Intelligence & Capability Layer — Gate 20 September 2026

Canonical architecture: `research/BIUPIU-MACHINE-INTELLIGENCE-ARCHITECTURE-v1.0.md`.

Biupiu OS is explicitly defined as a new machine-capable software architecture, not as a Windows clone. Its core differentiator is the combination of machine-readable capabilities, governed learning, machine communication, Digital Twins, mathematics, physics and simulation.

### Machine capability lifecycle

`DISCOVER -> IDENTIFY -> DESCRIBE -> TWIN -> VALIDATE -> CONNECT -> OPERATE -> OBSERVE -> LEARN -> UPDATE`

### Intelligence authority lifecycle

`OBSERVE -> LEARN -> PROPOSE -> SIMULATE -> VALIDATE -> AUTHORISE -> EXECUTE`

### Machine-readable abstraction

Applications consume capability contracts rather than depending directly on vendor-specific hardware assumptions. Transport-specific adapters may remain beneath the abstraction for USB, Ethernet/IP, serial, CAN/CAN-FD, Modbus, OPC UA, MQTT, Bluetooth, Wi-Fi, GPIO and robotics/industrial interfaces.

### Semantic system graph

`Machine -> Sensor -> Actuator -> Algorithm -> Digital Twin -> Physics Model -> Mathematics Model -> Dataset -> Provenance -> Product`

### Recursive Digital Twin

Canonical architecture: `research/BIUPIU-RECURSIVE-DIGITAL-TWIN-ARCHITECTURE-v1.0.md`.

Twins may contain child twins and participate in higher-order twins while preserving stable identity, parent/child relationships, model versions, state separation, provenance and validation boundaries. Twin-of-Twin composition is treated as a governed system graph, not uncontrolled duplication.

### Self-development / System Builder

The OS development environment is intended to assist in constructing and validating the OS itself:

`NEW CAPABILITY -> DEPENDENCY ANALYSIS -> ARCHITECTURE IMPACT -> IMPLEMENTATION -> TEST GENERATION -> SIMULATION -> VALIDATION -> HUMAN APPROVAL -> INTEGRATION`

### Maths / Physics integration

Existing MATH and physics/simulation engines are first-class system resources. Their outputs feed geometry, Digital Twins, validation and governed learning records.

### Architecture boundary

The system may innovate within the specification; it may not forget the specification. Simulated, desired or inferred state must never silently become observed physical state, and physical actuation remains subject to independent authority and safety gates.

**Gate status:** Architecture integrated; implementation, conformance, security, hardware-in-the-loop and production validation remain separate gates.


## 12. Instrumentation / Automation / Robotics / AI Integration

Instrumentation is now a first-class OS/DMS subsystem input. Machine telemetry is normalised through the Machine Capability contract and associated with Digital Twin identity, mathematical/physics models and AI services.

Protocol/adaptor research includes OPC UA, MQTT, Modbus, ROS/ROS 2 and vendor-specific industrial interfaces. Siemens and Fujitsu are research/benchmark sources; they do not define Biupiu OS.

Foreign-language routing prioritises Italian and German technical material, especially industrial robotics, PLC/SPS, OPC UA, Industrie 4.0, instrumentation and mechatronics.

Canonical records:
- research/BIUPIU-INSTRUMENTATION-MACHINE-INTERFACE-RESEARCH-v1.0.md
- research/BIUPIU-FOREIGN-LANGUAGE-AUTOMATION-ROBOTICS-REGISTER-v1.0.md
- research/BIUPIU-INSTRUMENTATION-AUTOMATION-ROBOTICS-AI-GATE-v1.0.md

Integration loop:
INSTRUMENT -> CAPABILITY -> EDGE/PROTOCOL -> DIGITAL TWIN -> MATH/PHYSICS -> AI -> VALIDATION -> AUTHORISATION -> ACTUATION

**Gate status:** Research and architecture integration complete; implementation, licence, security, simulation, hardware-in-loop and safety gates remain mandatory.


## P0 C/C++/Rust Core Integration — 20 September 2026

The multi-language kernel architecture is now a first-class extension of the OS contract. C is the durable ABI/HAL boundary; Rust is preferred for new memory/concurrency/security-sensitive core services; C++ is the primary native layer for simulation, geometry, graphics and high-performance scientific subsystems. This allocation is consistent with the Rust Embedded guidance that C ABI boundaries are the stable interoperability mechanism for Rust/C/C++ systems. NASA F´ also demonstrates componentized C++ embedded architecture with defined interfaces and unit/integration testing. 

Canonical contract: Hardware -> C ABI/HAL -> Rust/C++ services -> OS validation -> DMS -> Intelligence -> applications/subsystems.

Rules:
- No language may bypass OS authority.
- No C++ ABI/STL object crosses a durable system boundary.
- Cross-language interfaces require explicit ownership, lifetime, error, alignment, serialization, version and concurrency contracts.
- Third-party source remains external until licence, security, build, smoke and regression gates pass.
- Resource documentation can enrich Intelligence but cannot itself promote executable code.
- Failed builds, failed translations and rejected dependencies remain learning evidence.

Canonical architecture record: `research/BIUPIU-MULTILANGUAGE-KERNEL-ARCHITECTURE-v1.0.md`.
Canonical resource registry: `research/BIUPIU-C-CPP-RUST-RESOURCE-MANIFEST-v1.0.json`.

Status: ARCHITECTURE INTEGRATED / HOST RUNTIME VALIDATION PENDING.


## P0 Executable Multi-Language Core Seed — 20 September 2026

`core/multilang/` is registered as a Core OS boundary package. C defines the durable ABI, Rust supplies the initial safety-oriented kernel boundary implementation, and C++ supplies the native subsystem contract. DMS and subsystem services consume these through OS contracts; they do not bypass the Core OS.

Verification state: SOURCE IMPLEMENTED / BUILD AND RUNTIME PENDING.


## 13. Unified Premium Neutral Design System — Gate 26, 21 September 2026

Canonical design authority: docs/architecture/BIUPIU-OS-UNIFIED-DESIGN-PHILOSOPHY-v1.0.md.

Biupiu OS and all subsystems now share a neutral-premium visual principle: **NEUTRAL BASE -> MATERIAL FINISH -> RESTRAINED NATURE ACCENT -> CLEAR INFORMATION**.

Pagani and Ferrari are reference points for craftsmanship, curated configuration, neutral foundations and material quality only; they are not templates and no proprietary assets or branding are copied.

Canonical rules: premium through restraint; neutral-first surfaces; material finish for character; nature as an accent family; semantic colours protected; one visual language across OS/DMS/Intelligence/simulators/configurators; simple and reversible interaction; legibility over ornament; no false claims of physical material accuracy.

Canonical digest: intelligence/BIUPIU-OS-DESIGN-DIGEST-2026-09-21.md.

Status: **IMPLEMENTED / SOURCE UPDATED / RUNTIME VISUAL VERIFICATION PENDING**.


## 14. Shared Material Language — Gate 27, 21 September 2026

Biupiu OS now has a lightweight shared material-surface abstraction for Android. Material finishes remain visual approximations and are deliberately restrained. The abstraction covers anodised aluminium, brushed titanium, bio-composite, recycled glass, carbon weave and living stone.

The material layer is subordinate to information hierarchy and semantic state. It is not a replacement for a future physically based rendering engine in simulators or Digital Twin environments.

Status: **SOURCE IMPLEMENTED / BUILD AND DEVICE VERIFICATION PENDING**.


## 15. Foreign/OEM Resource Harvest — Gate 28, 21 September 2026

Foreign-language discovery is now registered as a governed resource lane. Search lanes cover Chinese, Korean, Japanese, German, Italian, French, Spanish, Portuguese and Russian material, with language treated as discovery metadata rather than a trust signal.

Cross-reference authorities: AOSP/OEM/open-device sources first; LineageOS/GitHub for reproducible implementation patterns; XDA for discovery only; OpenBooks only where the specific project and licence/scope are relevant.

Integrated source-level module: apps/android/app/src/main/java/com/biupiu/rndos/ForeignResourceRegistry.kt.
Canonical harvest record: docs/architecture/BIUPIU-FOREIGN-OEM-RESOURCE-HARVEST-GATE-28.md.

Promoted patterns: Treble/VINTF boundary, partition-aware device model, common/target device-tree separation, proprietary extraction provenance, mainline portability, multilingual/localisation and auditable/idempotent workflow concepts. No proprietary blobs, dumps, signing keys, GMS packages or copied third-party implementations are integrated.

**Gate status: IMPLEMENTED / SOURCE TESTS ADDED / BUILD-EMULATOR RUNTIME VERIFICATION PENDING.**


## 16. OS Resource Consolidation & Housekeeping — Gate 29, 21 September 2026

Deep repository/history reconciliation identified substantial reusable architecture already present across `core/multilang`, `apps/android`, `apps/shared/runtime`, `intelligence`, `packages`, `world` and governed research manifests. Gate 29 establishes consolidation-first housekeeping: extend existing contracts, avoid parallel authorities, preserve historical/open research, and never promote implementation to runtime verification without evidence.

Canonical consolidation record: `research/BIUPIU-OS-RESOURCE-CONSOLIDATION-GATE-29.md` and `.json`. Smoke/CI: `intelligence/BIUPIU-OS-RESOURCE-CONSOLIDATION-SMOKE.py` and `.github/workflows/biupiu-os-resource-consolidation.yml`.

**Gate status: IMPLEMENTED / CONSOLIDATION REGISTERED / EXECUTION EVIDENCE PENDING.**


## 17. Unified Gradle Toolchain & Android Build Harvest — Gate 30, 21 September 2026

Repository audit found three independent Android Gradle systems: `apps/android`, `smart-farming/android`, and `software/rnd-os-mobile`. Gate 30 registers them as separate application boundaries and establishes a shared toolchain matrix rather than merging source trees.

Canonical record: `research/BIUPIU-GRADLE-SYSTEM-HARVEST-GATE-30.md` and `research/BIUPIU-GRADLE-SYSTEM-MANIFEST-v1.0.json`.

AGP 8.7.3 systems are pinned to Gradle 8.9; the AGP 8.13.0 mobile system is pinned to Gradle 8.13; JDK 17 is the common execution baseline. Wrapper distribution checksums are recorded. Wrapper JAR/scripts remain explicitly open until official binaries can be retrieved/generated and verified.

CI matrix: `.github/workflows/biupiu-gradle-toolchain-gate.yml`.

**Gate status: TOOLCHAIN REGISTERED / CI EXECUTION ENABLED / WRAPPER COMPLETION PENDING.**

## 18. JDK Lifecycle + GitHub Signing Boundary — Gate 31, 21 September 2026
JDK 17 is the explicit Android CI baseline with major-version assertions and controlled upgrade gates. GitHub Actions signing is fail-closed and secret-only; keystore/private signing material is never committed. Required secret names and lifecycle policy are registered in `research/BIUPIU-JDK-LIFECYCLE-MANIFEST-v1.0.json`. Actual secret configuration and signed-release verification remain open.
