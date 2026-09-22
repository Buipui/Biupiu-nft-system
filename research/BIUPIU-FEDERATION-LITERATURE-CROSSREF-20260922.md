# Biupiu Federation Literature & Cross-Reference — 2026-09-22

## Purpose
Canonical literature/evidence layer for the deep external federation harvest. This records source identity, architectural role, and integration constraints. It does not vendor third-party code or model weights.

## Primary source set
1. Android AppFunctions — https://developer.android.com/ai/appfunctions
   Experimental Android platform API plus Jetpack library for local MCP-style tool exposure; Android 16+ documented baseline; EXECUTE_APP_FUNCTIONS permission for callers. Mini OS must feature-detect it behind a platform adapter.
2. Android AppFunctions samples — https://github.com/android/appfunctions
   Official samples/testing agent; SDK 36+ and Android 16+ device/emulator documented. Reference/test material, not embedded runtime.
3. Android AppFunctions engineering guidance — https://android.googlesource.com/platform/frameworks/support/+/main/appfunctions/AGENTS.md
   Formatting, API-update and local-test discipline. Adopt this verification discipline.
4. Android AICore — https://support.google.com/android/answer/17065362
   System AI service; Android 14+ baseline documented, with availability varying by device/manufacturer. Runtime detection required.
5. Android AGSL — https://developer.android.com/develop/ui/views/graphics/agsl/using-agsl
   RuntimeShader/AGSL graphics boundary. Android adapter only.
6. Tencent ncnn — https://github.com/Tencent/ncnn
   Mobile/embedded inference with ARM NEON, FP16/int8 paths and Vulkan. Android ARM build paths documented. Provider adapter; driver support must be detected.
7. Tencent ncnn Vulkan — https://github.com/Tencent/ncnn/wiki/FAQ-ncnn-vulkan
   Android Vulkan support has API/NDK/runtime requirements. Library presence alone does not prove Vulkan capability.
8. Alibaba TinyNeuralNetwork — https://github.com/alibaba/TinyNeuralNetwork
   Graph capture, pruning, quantization, QAT and model conversion. Host/model-preparation provider, not Mini OS kernel code.
9. Rockchip RKNN Toolkit2 — https://github.com/airockchip/rknn-toolkit2
   Toolkit, Lite2, Runtime and kernel-driver stack. Model conversion and runtime are separate gates; device/HIL required.
10. Megvii MegEngine — https://github.com/MegEngine/MegEngine
    External ML/inference framework; provider adapter and target/runtime verification required.
11. MegCC — https://github.com/MegEngine/MegCC
    External model compiler; compiler/preparation lane.
12. PyTorch — https://pytorch.org/
    Authoring/training ecosystem; OS research/authoring lane rather than Mini OS kernel dependency.
13. ExecuTorch — https://pytorch.org/executorch/
    Edge inference runtime; provider adapter with backend/device verification.
14. STM32Cube.AI — https://www.st.com/en/embedded-software/x-cube-ai.html
    STM32 deployment ecosystem; MCU/HIL lane, separate from Android runtime.
15. CatBoost — https://catboost.ai/
    ML ecosystem; target artifact must be independently verified before promotion.
16. DaCe — https://github.com/spcl/dace
    Data-centric SDFG compiler targeting CPU/GPU/FPGA and capable of producing C-ABI-compatible shared libraries. Host optimisation/compiler lane.
17. Menpo — https://www.menpo.org/
    Computer-vision research ecosystem; host/research lane.
18. CuPy — https://cupy.dev/
    NumPy-compatible GPU array ecosystem; host/research GPU lane.
19. fastNLP — https://github.com/fastnlp/fastNLP
    NLP research/training framework; host/model-preparation lane.
20. Google AQT — https://github.com/google/aqt
    Accurate Quantized Training; upstream states AQT is reaching end-of-life and Qwix replaces it. Historical reference only.
21. IQM — https://www.meetiqm.com/
    Quantum provider/service/device adapter.
22. RIKEN — https://riken.jp/en/
    Quantum research/simulation provider lane.
23. Fujitsu quantum computing — https://www.fujitsu.com/global/services/business-services/quantum-computing/
    Quantum computing/simulation provider lane.
24. Arm architecture — https://developer.arm.com/architectures/cpu-architecture
    ARMv8.2-A FP16/NEON are ISA/CPU capability concerns; runtime CPU feature detection required.
25. Qwen — https://qwenlm.github.io/
26. DeepSeek — https://www.deepseek.com/
27. Meta Llama — https://www.llama.com/
28. Google Gemma — https://ai.google.dev/gemma
    Model families, not interchangeable OS libraries. Exact weights, tokenizer assets and licences remain separate provenance gates.
29. OpenDroid UI Engine
    No sufficiently authoritative, uniquely identifiable project was established. Remains UNRESOLVED and fail-closed.

## Cross-reference matrix
| Domain | Main OS | Mini OS | Provider class | Promotion gate |
|---|---|---|---|---|
| ARM FP16/NEON | Yes | Yes | CPU capability | CPU feature test |
| OpenCL | Yes | Adapter boundary | GPU API | device/driver test |
| Qwen/DeepSeek/Llama/Gemma | Yes | Metadata/adapter | Model family | model + licence + regression |
| ncnn | Yes | Yes | Edge inference | ABI + device benchmark |
| MegCC/MegEngine | Yes | Adapter | Compiler/runtime | target build |
| TinyNN | Yes | Preparation boundary | Model optimisation | conversion regression |
| Kirin NPU | Yes | Yes | Vendor NPU | licence + device HIL |
| RKNN | Yes | Yes | Vendor NPU | runtime + NPU HIL |
| AppFunctions/MCP | Yes | Yes | Android platform | API 36+ device test |
| AICore | Yes | Yes | Android system service | API/device feature test |
| ExecuTorch/PyTorch | Yes | Yes | ML/edge runtime | backend build + numerical regression |
| STM32Cube.AI | Yes | MCU target | MCU deployment | licence + hardware HIL |
| CatBoost | Yes | Adapter | ML provider | target artifact + regression |
| DaCe | Yes | No kernel dependency | Compiler | host compile |
| Menpo/CuPy | Yes | No kernel dependency | Research | host environment |
| fastNLP | Yes | No kernel dependency | NLP research | host environment |
| AQT | Historical | No runtime dependency | Quantization reference | successor evaluation |
| IQM | Yes | No kernel dependency | Quantum provider | service/device test |
| RIKEN/Fujitsu | Yes | No kernel dependency | Simulation | simulator test |
| AGSL | Yes | Yes | Android graphics | API/device test |
| OpenDroid | Pending | Pending | Unresolved | identity/provenance first |

## Corrected conflicts
1. vulkan.validation was incorrectly marked ADAPTER_ONLY while the test required non-usable. It is now classified DEVICE_REQUIRED so isUsable() fails closed.
2. The registry separates ADAPTER_ONLY, DEVICE_REQUIRED, LICENSE_REVIEW, HISTORICAL_REFERENCE and UNRESOLVED.
3. AppFunctions is not treated as a generic MCP server runtime; it is an Android platform/Jetpack integration and is experimental.
4. AICore is not assumed present merely because Android is present; availability varies by device/manufacturer.
5. OpenCL is not treated as a universal Android runtime; it remains a provider/API boundary requiring device/driver validation.
6. AQT is no longer represented as a production quantization dependency.
7. OpenDroid is not implemented until identity/provenance is established.
8. Model-family registration does not imply model weights are bundled, licensed, or executable on every target.

## Evidence rule
Literature/source registration -> provenance/licence review -> adapter normalisation -> semantic test -> build -> numerical/AI regression -> device/HIL -> promotion.
A source citation or successful source-level compilation is never sufficient to mark hardware/runtime capability VERIFIED.

## OpenDroid correction and deep harvest — 2026-09-22

The external evidence resolves the prior ambiguity: OpenDroid is documented as an autonomous Android AI agent with a Compose UI layer, accessibility automation, action dispatch, agent/planning, LLM routing, memory, Keystore security, Android services/voice, Room/DataStore, Hilt and presentation ViewModels. It is not treated as a standalone authoritative UI engine. See `research/BIUPIU-OPENDROID-DEEP-EXTERNAL-FEDERATION-HARVEST-20260922.md`. The exact legacy `opendroid.ui-engine` identity remains UNRESOLVED/blocked; supported agent and module identities are adapter-only until independent build/device verification.
