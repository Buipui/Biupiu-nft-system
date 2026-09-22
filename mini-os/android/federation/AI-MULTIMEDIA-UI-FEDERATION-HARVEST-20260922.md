# AI / Multimedia / UI Federation Harvest — 2026-09-22

## Scope
External federation harvest for Qualcomm IMSDK 2.0, QAIRT/QNN, ONNX Runtime, LiteRT/TensorFlow Lite, Google AI Edge, Huawei HiAI, Paddle Lite NDK, Apache TVM, Jetpack Compose-first, Material 3, RenderEffect and Navigation 3.

## Internal-first reconciliation
Existing Biupiu Android federation, native coding philosophy/matrix, scientific compute extension, guided fault-finding specification and federation cross-link register were checked before integration.

## Integration matrix
| Capability | Integration decision | State |
|---|---|---|
| Qualcomm IMSDK 2.0 | Platform adapter for Dragonwing/Qualcomm Linux; not a generic Android dependency | PLATFORM_BOUNDARY |
| QAIRT / QNN | Qualcomm provider boundary; external SDK, licence and target-device evidence required | LICENSE_REVIEW |
| ONNX Runtime | Android Maven runtime dependency plus provider boundary | NATIVE_DEPENDENCY |
| LiteRT | Android runtime dependency; CompiledModel is the forward path | NATIVE_DEPENDENCY |
| TensorFlow Lite | Compatibility identifier; do not create a duplicate forward runtime | ADAPTER_ONLY |
| Google AI Edge | Family/namespace federation boundary with LiteRT as concrete Android runtime | ADAPTER_ONLY |
| Huawei HiAI | Vendor/device NPU adapter; generic Android must fail closed | DEVICE_REQUIRED |
| Paddle Lite NDK | Android NDK/provider adapter; no third-party source copied | ADAPTER_ONLY |
| Apache TVM | Cross-compiled runtime/provider adapter | ADAPTER_ONLY |
| Compose-first | Kotlin/Compose build capability added to Mini OS | NATIVE_DEPENDENCY |
| Material 3 | Compose Material 3 dependency added | NATIVE_DEPENDENCY |
| RenderEffect | Android API capability with API 31 runtime guard | DEVICE_REQUIRED |
| Navigation 3 | Stable Compose-first Navigation 3 dependency | NATIVE_DEPENDENCY |

## Version decisions
- AGP 8.7.3 / Gradle 8.9 / JDK 17 remain the repository Android baseline.
- Kotlin 2.0.21 is added for Compose integration.
- Compose runtime/foundation/UI 1.12.1; Material 3 1.4.0.
- Navigation 3 stable 1.1.7; the 1.2.0 release candidate is not promoted.
- LiteRT Android 2.1.0 from Google's current migration documentation.
- ONNX Runtime Android 1.30.0 observed in Maven Central at harvest time.
- QAIRT/IMSDK/HiAI remain external/device-specific boundaries rather than generic dependencies.

## Semantic and fault controls
1. Dependency presence is not runtime verification.
2. Unknown capabilities fail closed.
3. Qualcomm IMSDK 2.0 is not misclassified as a generic Android app dependency.
4. QAIRT/QNN is not authoritative without SDK provenance, licence review and target-device evidence.
5. TensorFlow Lite is retained only as a compatibility lane while LiteRT is the forward runtime.
6. HiAI remains unavailable unless target-device capability is proven.
7. RenderEffect is guarded because the Mini OS minSdk is 29 and the API was added in 31.
8. External executable source and vendor binaries are not copied into the repository.
9. Compose migration is an implementation/build gate, not a runtime claim.
10. Navigation 3 stable is used rather than the current release candidate.

## Source-level verification
- Added AiMultimediaUiFederationRegistry covering all requested module families.
- Added AiMultimediaUiFederationRegistryTest covering registration, fail-closed vendor/platform boundaries and the distinction between source integration and runtime verification.
- Added ONNX Runtime and LiteRT Android dependencies.
- Added Kotlin/Compose/Material 3/Navigation 3 build plugins and dependencies.
- Android build and device/runtime verification remain OPEN because the repository's wrapper integrity/build-environment gate is still unresolved.

## Promotion ladder
REQUIREMENT -> INTERNAL GAP CHECK -> EXTERNAL HARVEST -> PROVENANCE/LICENCE -> ADAPTER/DEPENDENCY -> SEMANTIC TEST -> BUILD -> RUNTIME -> DEVICE -> REGRESSION -> HUMAN PROMOTION.

## External evidence
- Qualcomm IMSDK 2.0: https://www.qualcomm.com/developer/blog/2026/08/introducing-qimsdk2-unified-framework-multmedia-ai
- Qualcomm IMSDK product: https://www.qualcomm.com/developer/software/qualcomm-intelligent-multimedia-sdk
- Qualcomm AI/QAIRT: https://www.qualcomm.com/developer/artificial-intelligence
- LiteRT migration: https://developers.google.com/edge/litert/migration
- LiteRT Android: https://developers.google.com/edge/litert/android
- ONNX Runtime mobile: https://onnxruntime.ai/docs/tutorials/mobile/
- Huawei HiAI: https://developer.huawei.com/consumer/en/hiai
- Paddle Lite Android build: https://github.com/PaddlePaddle/Paddle-Lite/blob/develop/lite/tools/build_android.sh
- Apache TVM Android: https://tvm.apache.org/2017/11/08/android-rpc-introduction
- Android Compose-first: https://developer.android.com/develop/ui/compose/first
- Material 3: https://developer.android.com/jetpack/androidx/releases/compose-material3
- RenderEffect: https://developer.android.com/reference/android/graphics/RenderEffect
- Navigation 3: https://developer.android.com/jetpack/androidx/releases/navigation3

## 2026-09-22 — Foreign-language federation harvest and architecture reconciliation

Foreign-language source checks were performed against Chinese-language mirrors/documentation for LiteRT, ONNX Runtime and Apache TVM, alongside current English upstream documentation. The Chinese ONNX Runtime Android documentation independently confirms NNAPI and QNN build lanes; the Chinese LiteRT documentation confirms the CompiledModel API; Apache TVM Chinese documentation confirms Android deployment through a cross-compiled runtime/RPC path. These sources were used as corroborating implementation evidence, not as substitutes for upstream authority.

### Missing-module findings and fixes
| Missing/under-integrated capability | Finding | Fix |
|---|---|---|
| ONNX Runtime execution-provider lanes | Registry had only generic ONNX Runtime | Added CPU, XNNPACK, NNAPI and QNN provider identities with fail-closed states |
| LiteRT accelerator-first API | Generic LiteRT identity did not expose CompiledModel lane | Added litert.compiledmodel provider identity |
| TVM mobile runtime | TVM was only a broad adapter entry | Added apache.tvm.runtime mobile-runtime boundary |
| Android Mini OS source integration | Federation Java sources lived outside the Gradle Java source set | Added mini-os/android/federation to the Mini OS main Java source set |
| R8/ProGuard protection | ONNX Runtime reflection keep rule was absent | Added mini-os/android/app/proguard-rules.pro |
| Provider selection | Registry described capabilities but had no architecture-neutral selector | Added AiExecutionProvider and fail-closed AiProviderSelector |
| Provider boundary regression | Existing registry test did not exercise concrete provider lanes | Extended AiMultimediaUiFederationRegistryTest |

### Architecture rule
The selector is an orchestration boundary only. It does not claim hardware execution. QAIRT/QNN remains licence/SDK/device gated; NNAPI remains device gated; HiAI remains device gated; Qualcomm IMSDK remains a platform boundary. LiteRT CompiledModel is the forward LiteRT Android lane, while TensorFlow Lite remains compatibility-only.

### External evidence
- Qualcomm AI Engine Direct documents lower-level accelerator APIs and delegation from ONNX Runtime/TFLite. citeturn0search0
- Qualcomm AI Hub documents QAIRT as the overall SDK and QNN as the runtime API layer. citeturn0search1
- LiteRT Android currently documents CompiledModel as the modern API and lists v2.2.0 as latest. citeturn0search5
- ONNX Runtime documents extensible Execution Providers including XNNPACK, NNAPI and Qualcomm QNN. citeturn0search8turn1search0
- Chinese-language ONNX Runtime Android documentation independently confirms NNAPI and QNN build lanes. citeturn1search3
- Chinese-language LiteRT documentation confirms the CompiledModel Android path. citeturn1search1
- Chinese-language Apache TVM documentation confirms Android deployment through cross-compilation/runtime and RPC mechanisms. citeturn1search14turn1search16

**Gate state: ARCHITECTURE INTEGRATION IMPLEMENTED / SEMANTIC BOUNDARIES CHECKED / CI BUILD AND DEVICE RUNTIME VERIFICATION OPEN.**
