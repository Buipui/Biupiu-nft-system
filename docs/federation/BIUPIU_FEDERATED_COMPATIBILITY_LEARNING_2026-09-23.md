# BIUPIU FEDERATED COMPATIBILITY LEARNING RECORD — 2026-09-23

## Purpose
Record cross-system compatibility findings for the native learning/change-detection layer. This is a governance and training-data record, not proof that every adapter is implemented.

## OEM/system-family compatibility model

| Family | Representative ecosystem | Capability lane | Compatibility strategy | Current state |
|---|---|---|---|---|
| Qualcomm/Snapdragon | Qualcomm AI Stack, QNN, Qualcomm ONNX Runtime Plugin EP | CPU/GPU/NPU, Android/PC/edge | Capability adapter + ONNX EP boundary; versioned runtime contract | HARVESTED / ADAPTER VERIFY |
| Google/Android | Android AI, LiteRT, MediaPipe, Gemini/on-device AI | Android CPU/GPU/NPU, app intelligence | Android capability registry + LiteRT/ML adapter | HARVESTED / ADAPTER VERIFY |
| Unreal/Epic | UE 5.8.3, NNE, OpenXR, Chaos/Dataflow | Desktop/mobile/XR rendering + simulation + AI | UE adapter layer; preserve project-owned Content/Config/Plugins/C++ | HARVESTED / MIGRATION VERIFY |
| Apple | Metal, CoreML, iOS SM6 | Apple GPU/ML | CoreML/NNE adapter; retain legacy Metal path | HARVESTED / PLATFORM VERIFY |
| Microsoft/Windows | DirectML, Windows desktop, ARM64/ARM64EC targets | CPU/GPU/AI acceleration | DirectML/NNE adapter + Windows capability profile | HARVESTED / PLATFORM VERIFY |
| Khronos/XR | OpenXR | Cross-vendor XR runtime | OpenXR capability contract; runtime/vendor extensions isolated | HARVESTED / RUNTIME VERIFY |
| ONNX | ONNX Runtime + external Execution Providers | Portable inference | Stable model contract + provider capability negotiation | HARVESTED / ADAPTER VERIFY |
| ARM/Linux/edge | ARM64 Linux and heterogeneous edge | CPU/GPU/NPU | Hardware-neutral capability registry | ARCHITECTURE / VERIFY |
| Vehicle/ECU | CAN, CAN-FD, LIN, Ethernet | Machine/ECU control and telemetry | Bounded hardware adapters + safety validation gate | ARCHITECTURE / PHYSICAL VERIFY |

## Cross-reference rules learned
1. Prefer capability contracts over OEM-specific application logic.
2. Keep OEM/vendor SDKs behind adapters.
3. Track runtime/API/ABI versions independently from model versions.
4. Separate discovery, implementation and verification.
5. Preserve multilingual terminology and source genealogy.
6. Never treat a harvested vendor component as Biupiu-owned IP.
7. For NPU/GPU acceleration, record fallback order and unsupported operators.
8. Treat Unreal project Content/Config/Plugins/C++ as source evidence; generated caches are non-authoritative.
9. For XR, preserve vendor extensions without making them the authoritative simulation state.
10. Machine/ECU data must pass capability/range/integrity/plausibility gates before trusted simulation/control layers.

## Native learning algorithm input schema
Each learned compatibility fact should carry:
source -> family -> module -> version -> capability -> interface -> dependency -> platform -> evidence -> confidence -> compatibility status -> test -> regression result -> supersedes/superseded-by -> hash.

Training/learning promotion:
DISCOVERED -> NORMALIZED -> CROSS-REFERENCED -> EVIDENCE-CHECKED -> TESTED -> PROMOTED.

A failed or contradictory result remains in the learning corpus and is not silently removed.

## Current priority
1. OEM/system-family identity and adapter boundaries.
2. UE 5.8.3 migration/provenance.
3. Qualcomm/ONNX EP and Android AI stack interoperability.
4. Google LiteRT/MediaPipe capability mapping.
5. NNE/ONNX/DirectML/IREE/CoreML capability matrix.
6. OpenXR/XR device-family compatibility.
7. ECU/CAN/CAN-FD/LIN/Ethernet safety boundary.
8. Desktop/mobile/AR/VR authoritative-state federation.

## Verification boundary
This record does NOT claim physical OEM hardware, local UE installation, Android builds, NPU execution or ECU interfaces have been tested. Those remain local/runtime gates.

## Sources harvested
- Epic UE 5.8 Release Notes: https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-5-8-release-notes
- Qualcomm ONNX Runtime Plugin EP: https://www.qualcomm.com/developer/blog/2026/05/qualcomm-launches-the-first-onnx-runtime-plugin-execution-provider
- Android AI: https://developer.android.com/ai
- Existing Biupiu IP register and federation read-back records.
