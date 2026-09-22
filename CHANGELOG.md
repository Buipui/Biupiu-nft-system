# Biupiu System Change Log

#
## 2026-09-22 — Gate 36 Universal Simulator Contract Verification

### Fault found
- Cross-checking Gate 36's universal simulator identifiers against the canonical TypeScript federation contract found a provenance-contract gap.
- `FederationObservation` did not explicitly carry the required timestamp or licence state, and the evidence field was named `evidence` rather than the Gate 36 contract's `evidenceClass`.

### Corrective implementation
- Added `timestamp`, `evidenceClass` and `licenceState` to `packages/biupiu-rnd-os/src/federation-contracts.ts`.
- Added `FederationLicenceState` as an explicit bounded state vocabulary.
- Extended `federation-contracts.test.ts` with assertions for the new provenance fields.

### Verification
- Corrected federation contract: **STATIC TYPE CHECK PASS**.
- Environment: TypeScript 5.8.3; strict mode; ES2022; NodeNext module/module-resolution.
- Full monorepo package build and fresh CI remain **OPEN**.
- Simulator-host runtime, UE/Android runtime, cross-simulator execution, hardware/HIL and physical correlation remain **OPEN**.

### Status transition
**CONTRACT GAP FOUND → PATCH IMPLEMENTED → STATIC TYPE CHECK PASS → RUNTIME FEDERATION OPEN.**


#
## 2026-09-22 — Next-Gate Scheduler Fault Check

### Fault found
- Static execution of the federated planner exposed a semantic mismatch in the preferred-class scheduler.
- The planner treated `preferred=(GPU, PERFORMANCE)` as an unordered set and could select PERFORMANCE CPU before GPU when both had zero current load.
- This contradicted the intended ordered preference contract and the existing GPU-selection test.

### Corrective implementation
- Updated `software/rnd-os-ai/src/biupiu_ai/compute_federation.py`.
- Preferred compute classes are now evaluated in declared priority order.
- Once the first available preferred class is found, capacity/load balancing selects within that class.
- `execute()` and `plan()` therefore share consistent preferred-class semantics.
- Minimum compute requirements remain fail-closed.

### Gate execution evidence
- Main federated scheduler smoke test: **PASS**.
- Missing-required-NPU fail-closed test: **PASS**.
- Machine capability range validation: **PASS**.
- Integrated GPU dispatch: **PASS**.
- Mini-OS C++ federation contract: **PASS**.
- The C++ test was compiled with `-std=c++17 -Wall -Wextra -Werror` and executed successfully.
- Repository GitHub Actions workflow has no recorded run for the changelog commit; therefore CI is **NOT** marked verified.
- Rust live execution remains **PENDING** because the available execution environment does not contain `rustc`/Cargo.

### Status transition
**FAULT FOUND → PATCH IMPLEMENTED → LOCAL SMOKE TEST PASS → CI/HARDWARE VERIFICATION OPEN.**


# 2026-09-22 — Federated Compute / Machine / Mini-OS Integration Consolidation

### Implemented

#### Main Biupiu OS / Intelligence
- Integrated `FederatedMachineRuntime`.
- Connected machine-capability validation to heterogeneous compute dispatch.
- Added capability registration and validated machine samples.
- Added workload planning and dispatch through the compute federation.
- Preserved the safety boundary: safety-critical hardware remains behind a separate certified/verified adapter boundary.
- Exported the integrated runtime and federation types through the Biupiu AI package interface.

#### Heterogeneous Compute Federation
- CPU, performance-core, efficiency-core, vector, GPU and NPU workload classes are represented through the federation architecture.
- Runtime topology is capability-driven rather than hard-coded to a fixed processor core count.
- Workloads can express preferred and minimum compute requirements.
- Minimum requirements fail closed when the required compute class is unavailable.
- Preferred compute resources are selected when available.
- Capacity is used as a fallback scheduling signal.
- Execution telemetry records dispatch outcomes.
- Native acceleration contracts cover x86_64, Apple arm64, generic ARM64 and RISC-V64 paths.

#### Machine Capability Architecture
- Added capability-first machine interfaces independent of vendor-specific application code.
- Added transport identifiers for CAN, CAN-FD, LIN, Ethernet, SPI, I2C, GPIO, ADC and virtual sources.
- Capability records include unit/range, update rate, read/write state, safety class, redundancy group and adapter identity.
- Validation is performed before machine data is trusted by higher layers.
- Hardware-specific translation remains isolated behind adapter boundaries.

#### Biupiu Mini-OS
- Added C ABI for federated compute selection.
- Added native C++ federation runtime.
- Added Rust federation implementation mirroring the C++ semantics.
- Added fail-closed minimum-class selection.
- Added preferred-class selection.
- Added capacity fallback.
- Corrected minimum-class semantics so an unrelated accelerator cannot satisfy a required class merely because its enum value is numerically higher.
- Added C++ contract tests and Rust unit tests for GPU selection and unavailable-NPU rejection.

#### Platform / Spatial Architecture
- Extended platform model to Windows, macOS, Linux, Android, iOS and Web.
- Added CPU-family detection for x86_64, ARM64 and RISC-V64.
- Added GPU/NPU/vector accelerator capability categories.
- Established the spatial/VR architecture as an endpoint of the authoritative simulation state rather than the source of truth.
- Heavy simulation may remain on workstation/server federation while desktop/mobile/AR/VR endpoints consume the controlled spatial state.
- GPU is treated as a first-class compute endpoint for rendering, geometry, simulation support, AI and digital-twin visualization.

#### Federation Gate Architecture
- F10 Multicore Compute gate added.
- F11 Machine Capability gate added.
- F12 Spatial/VR Compute gate added.
- F13 Native Platform Federation gate added.
- Additional federation governance gates now represented through the canonical protocol, including design language, digital-twin learning, simulator-learning federation, capability discovery, observability, schema governance, delivery resilience, industrial adapters and World repository boundaries.

#### Verification / CI
- Registered Main OS Python syntax and pytest coverage for compute federation and federated machine runtime.
- Registered Mini-OS C++17 compilation/test path with warnings-as-errors.
- Registered Mini-OS Rust cargo-test path.
- Registered a federation integration CI workflow.
- Registered compute-federation CI and schema validation paths.
- Verification status remains explicitly separated from implementation status.

#### Research / IP Record
- Updated the federated compute + machine runtime test record.
- Maintained the Multicore + Spatial Compute gate as:
  **IMPLEMENTED / STATIC CORE VERIFIED / LIVE HARDWARE PENDING**.
- Maintained Mini-OS G02 as:
  **IMPLEMENTED_NOT_VERIFIED**.
- Recorded the six related compute/machine/spatial IP subjects in the public IP index:
  BIU-IP-2026-021 through BIU-IP-2026-026.
- IP records are provenance/invention records only; novelty, patentability, ownership and FTO remain subject to professional legal review.

### Current verification boundary

**REGISTERED**
- Architecture and interfaces
- Main OS integration
- Mini-OS C++ and Rust implementations
- Test cases
- CI workflows
- Schemas
- Federation gates
- Research/IP records

**IMPLEMENTED**
- Main OS federated machine runtime
- Heterogeneous compute selection
- Machine capability validation
- Mini-OS C++ federation runtime
- Mini-OS Rust federation implementation
- Platform/native acceleration contracts

**STATIC VERIFIED**
- Previously recorded compute-federation syntax and two scheduler/fail-closed tests passed on 2026-09-21.

**NOT YET LIVE VERIFIED**
- Current CI execution result for the newly registered integration workflow
- Physical GPU/NPU discovery
- Real multicore topology/scaling/contention
- Windows/macOS/Linux/Android runtime regression
- ECU/CAN-FD hardware-in-the-loop
- VR frame timing/input validation
- Physical sensor validation
- Fault injection and recovery under live hardware

### Engineering rule carried forward

Biupiu remains **digital-first, then physical**:
1. Define the capability and contract digitally.
2. Validate semantics and failure behaviour.
3. Federate the appropriate compute resources.
4. Test in CI/native runtime.
5. Validate against hardware.
6. Only then promote the implementation into physical machine control or other safety-relevant deployment.

No live hardware or CI result is marked verified unless an execution record exists.
