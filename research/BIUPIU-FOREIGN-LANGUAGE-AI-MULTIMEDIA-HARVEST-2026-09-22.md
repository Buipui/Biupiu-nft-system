# BIUPIU FOREIGN-LANGUAGE AI / MULTIMEDIA HARVEST & INTEGRATION RECORD — 2026-09-22

## Scope
External documentation harvest was cross-referenced against the existing Biupiu Intelligence / Biupiu OS / Mini-OS federation architecture. The harvest is evidence for adapter registration and gap identification; it does not promote any provider to native authority.

## Sources harvested
### Chinese-language / China mirror
- ONNX Runtime Android build documentation: https://runtime.onnx.org.cn/docs/build/android.html
- Google AI Edge / LiteRT Qualcomm NPU documentation mirror: https://developers.google.cn/edge/litert/android/npu/qualcomm

### Global vendor / upstream documentation
- Qualcomm AI Engine Direct SDK: https://www.qualcomm.com/developer/software/qualcomm-ai-engine-direct-sdk
- Qualcomm AI Hub: https://dev.aihub.qualcomm.com/docs/
- ONNX Runtime QNN Execution Provider: https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
- ONNX Runtime Android build: https://onnxruntime.ai/docs/build/android.html
- ONNX Runtime Qualcomm Plugin EP repository: https://github.com/onnxruntime/onnxruntime-qnn
- LiteRT Qualcomm integration: https://github.com/google-ai-edge/LiteRT/tree/main/litert/vendors/qualcomm
- LiteRT NPU vendor matrix: https://developers.google.cn/edge/litert/next/npu
- Android CameraX modern APIs: https://github.com/android/skills/blob/main/camera/camerax/references/modern-apis.md

## Missing-module findings
1. ONNX Runtime Qualcomm Plugin EP was missing as a distinct provider boundary. Added onnxruntime.qnn-plugin.
2. LiteRT Qualcomm AI Engine Direct/QNN delegate path was missing as a distinct provider boundary. Added litert.qualcomm-qnn.
3. ExecuTorch Hexagon/Qualcomm path was missing. Added executorch.hexagon as an adapter-only provider pending licence/build/device/runtime evidence.
4. LiteRT's current NPU vendor matrix exposes MediaTek NeuroPilot, Samsung Exynos AI LiteCore, Google Tensor and Intel OpenVINO lanes. MediaTek, Samsung and Google Tensor were added as fail-closed provider boundaries. Intel OpenVINO remains a follow-up because it belongs to the cross-platform/desktop lane rather than the immediate Android Mini-OS accelerator path.
5. Android multimedia input/output boundaries were underrepresented. Added android.camerax, android.media3, and google.mlkit as platform-provider adapters.
6. Qualcomm's current architecture separates higher-level model parsing/partitioning from accelerator-specific QNN backends. Biupiu therefore keeps provider-specific SDKs behind the federation/capability boundary instead of embedding vendor authority into Core OS.

## Integration rules
- Native authority remains Biupiu Core OS/DMS validation and release gates.
- Provider SDKs are replaceable adapters.
- Unknown device/provider capability fails closed.
- A registered provider is not a runtime claim.
- Qualcomm QNN context binaries remain SoC-specific; do not promote a context asset without matching device/SoC evidence.
- Android R8/ProGuard rules must be part of the ONNX Runtime Android integration gate.
- LiteRT Qualcomm AOT/JIT paths require separate build/runtime evidence.
- CameraX advanced capabilities require capability probing rather than hard-coded assumptions.
- Multimedia effects remain below OS authority and cannot bypass DMS validation.
- External code remains reference/adapter material until provenance, licence, security, build and regression gates pass.

## Evidenced remediation
- Mini-OS Rust native build failed on cargo fmt --check; the failure was formatting-only. mini-os/rust/src/federation.rs and mini-os/rust/src/lib.rs were formatted without changing the public contract.
- Cross-link manifest was expanded and its source-level tests now cover the harvested accelerator and multimedia boundaries.

## Verification boundary
SOURCE-LEVEL: UPDATED
CI: PENDING FRESH RUN AFTER THE LATEST COMMITS
ANDROID DEVICE/RUNTIME: OPEN
NPU/GPU HARDWARE EXECUTION: OPEN
FINAL HUMAN PROMOTION: OPEN

## Gate rule
Do not mark the harvested providers as runtime verified until the corresponding build, device, inference, telemetry and regression evidence exists.
