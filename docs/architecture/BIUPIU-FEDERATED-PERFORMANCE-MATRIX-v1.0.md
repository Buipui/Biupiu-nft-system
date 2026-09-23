# Biupiu Federated Performance Matrix v1.0

Date: 2026-09-23

## Scheduling rule
Internal modules are reusable matrix participants. They remain PASSIVE until a verified workload requires them. Activation and resource allocation are selected from capability, latency/fidelity, dependency, resource, thermal/power and safety evidence.

| Family | Software/resource layer | Native federation role | Preferred acceleration | Fallback | State policy | Verification |
|---|---|---|---|---|---|---|
| Qualcomm / Snapdragon | Android/edge SDKs, ONNX execution provider, NPU/GPU/CPU | capability adapter | NPU/GPU | CPU/software | passive until workload demand | runtime/device pending |
| Google / Android | LiteRT, MediaPipe, Android AI | platform/ML adapter | device accelerator | portable ML path | demand-driven | Android build/device pending |
| Epic / Unreal | UE 5.8.3, NNE, OpenXR, Chaos/Dataflow | simulator/world adapter | GPU/NNE | CPU/reference | activate per scene/twin workload | local UE runtime pending |
| Apple | Core ML, Metal, Accelerate | Apple capability adapter | Neural Engine/GPU/CPU | CPU/reference | demand/thermal aware | device pending |
| Microsoft / Windows | DirectML, ARM64/ARM64EC | Windows acceleration adapter | GPU/NPU where supported | CPU | demand/resource aware | host benchmark pending |
| AMD / Intel | x86-64 vector/matrix/CPU paths | portable CPU capability providers | SIMD/vector/matrix | generic CPU | topology/load aware | host benchmark pending |
| Khronos / OpenXR | cross-vendor XR contracts | XR endpoint adapter | GPU/multiview | non-XR simulation | active only for XR workloads | device pending |
| ARM / Linux / edge | heterogeneous SoC/runtime | hardware-neutral capability provider | SoC-specific | portable CPU | topology/resource aware | hardware pending |
| ECU / industrial | CAN/CAN-FD/LIN/Ethernet, OPC UA/MQTT | bounded machine adapter | workload-specific | safe degraded path | active only when authoritative data is required | HIL/ECU pending |

## Cross-matrix dimensions
Compute x OS x simulation x AI/ML x XR x industrial x OEM x development resources x evidence/provenance.

## Shared development-resource priority
During OS development, official SDK/API/ABI documentation, compiler/toolchain support, profilers, debuggers, emulators, simulators, HIL resources, execution providers, driver/firmware contracts and version histories are indexed before implementation forks.

## Adaptive resource states
PASSIVE -> READY -> ACTIVE -> DEGRADED -> FAILED.
Hardware may accelerate when capability, eligibility and safety evidence are valid; it may decelerate when resource pressure exceeds policy while latency pressure is low; it may fall back to portable execution when acceleration is unavailable or invalid.

## Native ML feedback
Each decision becomes learning evidence with module, capability, OEM family, software/runtime version, hardware class, workload, selected path, expected/observed performance, resource state, fallback, regression and provenance.

## Verification boundary
This matrix is a registered architecture/performance contract. No unmeasured benchmark is presented as verified. Physical OEM hardware, NPU/GPU execution, local UE 5.8.3 runtime, Android devices and ECU/HIL remain separate verification gates.