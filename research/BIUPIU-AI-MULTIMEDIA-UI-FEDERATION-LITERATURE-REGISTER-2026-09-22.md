# Biupiu AI / Multimedia / UI Federation Literature Register — 2026-09-22

## Filing purpose
Canonical literature/provenance filing for the AI, multimedia and UI federation gate. Records upstream documentation used for architecture decisions, implementation reconciliation, semantic checks and missing-module identification. Literature is evidence, not executable authority.

## Evidence classes
- ESTABLISHED: upstream documentation directly describes the capability/API.
- SUPPORTED: corroborating documentation confirms the same implementation path.
- PRELIMINARY: useful implementation lead requiring repository/runtime verification.
- BOUNDARY: vendor, device, licence or platform-specific material requiring independent evidence.

## Primary upstream literature
| Area | Source | Evidence | Repository use |
|---|---|---|---|
| Qualcomm AI Engine Direct / QNN | Qualcomm documentation | ESTABLISHED / BOUNDARY | QNN/QAIRT provider boundary |
| Qualcomm QAIRT | Qualcomm QAIRT documentation | ESTABLISHED / BOUNDARY | SDK provenance and licence gate |
| ONNX Runtime Android | ONNX Runtime Android build documentation | ESTABLISHED | Android dependency, R8, NNAPI/QNN lanes |
| ONNX Runtime EPs | ONNX Runtime EP documentation | ESTABLISHED | CPU/XNNPACK/NNAPI/QNN/TVM provider identities |
| ONNX Runtime mobile | ONNX Runtime mobile documentation | ESTABLISHED | Mobile runtime lifecycle |
| ONNX Runtime Java API | OrtSession.SessionOptions API | ESTABLISHED | Android provider registration contract |
| LiteRT Android | Google AI Edge LiteRT | ESTABLISHED | Forward Android ML runtime |
| LiteRT CompiledModel | Google AI Edge LiteRT v2 | ESTABLISHED | CompiledModel provider lane |
| Apache TVM | Apache TVM Android/runtime docs | ESTABLISHED | Adapter-only mobile runtime |
| Jetpack Compose | Android Developers | ESTABLISHED | Compose-first UI |
| Material 3 | Android Developers | ESTABLISHED | UI design-system dependency |
| RenderEffect | Android API docs | ESTABLISHED | API 31+ guarded rendering |
| Navigation 3 | AndroidX docs | ESTABLISHED | Compose-first navigation |
| Huawei HiAI | Huawei developer docs | BOUNDARY | Device/vendor NPU adapter |
| Paddle Lite | Paddle Lite Android/NDK docs | BOUNDARY | Adapter-only NDK lane |
| Qualcomm IMSDK | Qualcomm IMSDK docs | BOUNDARY | Dragonwing/Qualcomm Linux platform adapter |

## Current source URLs
- Qualcomm AI Engine Direct / QNN: https://docs.qualcomm.com/
- Qualcomm QAIRT: https://docs.qualcomm.com/nav/home/
- ONNX Runtime Android: https://onnxruntime.ai/docs/build/android.html
- ONNX Runtime EPs: https://onnxruntime.ai/docs/execution-providers/
- ONNX Runtime QNN EP: https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
- ONNX Runtime NNAPI EP: https://onnxruntime.ai/docs/execution-providers/NNAPI-ExecutionProvider.html
- ONNX Runtime mobile: https://onnxruntime.ai/docs/tutorials/mobile/
- ONNX Runtime Java API: https://onnxruntime.ai/docs/api/java/ai/onnxruntime/OrtSession.SessionOptions.html
- LiteRT Android: https://ai.google.dev/edge/litert/android
- LiteRT migration: https://ai.google.dev/edge/litert/migration
- Apache TVM Android: https://tvm.apache.org/2017/11/08/android-rpc-introduction
- Compose-first: https://developer.android.com/develop/ui/compose/first
- Material 3: https://developer.android.com/jetpack/androidx/releases/compose-material3
- RenderEffect: https://developer.android.com/reference/android/graphics/RenderEffect
- Navigation 3: https://developer.android.com/jetpack/androidx/releases/navigation3
- Huawei HiAI: https://developer.huawei.com/consumer/en/hiai
- Paddle Lite Android: https://github.com/PaddlePaddle/Paddle-Lite/blob/develop/lite/tools/build_android.sh
- Qualcomm IMSDK: https://www.qualcomm.com/developer/software/qualcomm-intelligent-multimedia-sdk

## Foreign-language corroboration
Chinese-language ONNX Runtime documentation corroborated Android NNAPI/QNN lanes. Chinese-language LiteRT documentation corroborated the Android LiteRT direction. Chinese-language Apache TVM documentation corroborated Android cross-compilation/runtime/RPC deployment. Hindi-language Google AI Edge LiteRT v2 C++ documentation corroborated Android C++/NDK CompiledModel integration. These sources are supporting evidence only; upstream authority remains primary.

## Literature-to-code reconciliation
1. Added ONNX CPU, XNNPACK, NNAPI and QNN provider identities.
2. Added the LiteRT CompiledModel lane.
3. Added the Apache TVM mobile runtime boundary.
4. Added mini-os/android/federation to the Android main Java source set.
5. Added the ONNX Runtime R8 keep rule.
6. Added architecture-neutral AiExecutionProvider and fail-closed AiProviderSelector.
7. Kept vendor/platform providers fail-closed until SDK, licence, device and runtime evidence exists.
8. Copied no proprietary vendor binaries or restricted third-party executable source.

## Version filing
- LiteRT: current Google documentation reviewed in this gate lists 2.2.0; repository dependency was advanced from 2.1.0 to 2.2.0.
- ONNX Runtime Android: repository records 1.30.0; official documentation confirms Android packaging/provider architecture. Dependency resolution remains a build gate.
- QAIRT/QNN: not hard-pinned into the generic Android build because entitlement and device availability are external.
- Navigation 3: repository remains on stable 1.1.7 rather than promoting a release candidate.

## Verification boundary
LITERATURE FILING: COMPLETE
PROVENANCE CLASSIFICATION: COMPLETE
ARCHITECTURE RECONCILIATION: IMPLEMENTED
SEMANTIC / FAIL-CLOSED CHECKS: IMPLEMENTED
ANDROID BUILD: OPEN
CI FRESH RUN: OPEN
REAL ONNX/LiteRT INFERENCE: OPEN
NNAPI/QNN/NPU DEVICE TEST: OPEN
PHYSICAL DEVICE REGRESSION: OPEN

## Canonical related records
- mini-os/android/federation/AI-MULTIMEDIA-UI-FEDERATION-HARVEST-20260922.md
- mini-os/android/federation/AiMultimediaUiFederationRegistry.java
- mini-os/android/federation/AiProviderSelector.java
- mini-os/android/federation/AiExecutionProvider.java
- mini-os/android/federation/AiMultimediaUiFederationRegistryTest.java
- research/BIUPIU-NATIVE-CODING-PHILOSOPHY-AND-ENGINEERING-MATRIX-v1.0.md
- research/INDEX.md

## Gate record
LITERATURE FILED → PROVENANCE CLASSIFIED → MISSING MODULES RECONCILED → IMPLEMENTATION CROSS-LINKED → BUILD/RUNTIME VERIFICATION OPEN.
