# Biupiu AI / Accelerator / Quantum Federation Harvest — 22 September 2026

Status: SOURCE INTEGRATED / RUNTIME VERIFICATION PENDING

## Scope

Federation harvest covered:
- Android AI Core / NNAPI
- Qualcomm AI Engine Direct QNN / SNPE
- MediaTek NeuroPilot / Neuron Runtime
- Huawei HiAI
- STM32Cube.AI
- NXP eIQ
- Intel OpenVINO
- NVIDIA Jetson / TensorRT
- Jittor / Jittor-LLM research boundary
- Ray
- Apache TVM
- FlashAttention
- CRFM/Centaur research boundary
- FastNLP
- IBM Quantum / Qiskit Machine Learning
- Xanadu / PennyLane
- D-Wave Leap / Ocean
- AWS Braket
- Azure Quantum
- TKET / Quantinuum
- TensorFlow / TensorFlow Lite
- QPU / QML / QNN / quantum compiler and IR practices

## Integration rule

Third-party SDKs and proprietary vendor runtimes are NOT copied into the repository. Biupiu receives capability contracts, optional adapters, provenance records, dependency declarations and routing boundaries. Vendor SDK installation remains target-device/license/environment dependent.

This is especially important for Android: NNAPI remains a compatibility boundary, but Android documentation marks NNAPI deprecated in Android 15 and recommends migration to alternatives such as the TensorFlow Lite GPU runtime. Therefore the native architecture retains NNAPI as a compatibility adapter rather than treating it as the sole future AI execution path.

## Native AI adapter layer

Added optional backend registrations for:
- Android AI Core / Android platform AI
- NNAPI
- Qualcomm QNN / SNPE
- MediaTek Neuron
- Huawei HiAI
- STM32Cube.AI
- NXP eIQ
- Intel OpenVINO
- NVIDIA TensorRT / Jetson
- Apache TVM
- Jittor
- Ray
- FastNLP
- FlashAttention
- TensorFlow / TensorFlow Lite
- CRFM/Centaur research adapter

The adapter registry remains dependency-light and fail-closed. Availability is probed only when explicitly requested; registration does not imply that a package is installed or that hardware acceleration is available.

## Quantum federation extension

Added provider boundaries for:
- Qiskit / Qiskit Machine Learning
- PennyLane
- QIR
- OpenQASM 3
- AWS Braket
- Azure Quantum
- D-Wave Leap / Ocean
- pytket / TKET

The quantum layer remains simulator-first and hardware-disabled by default.

QIR is treated as an LLVM-based interoperability boundary. OpenQASM 3 is treated as a quantum program/circuit IR boundary. Provider-specific hardware execution requires separate provenance, security, reproducibility, calibration, regression and human-approval evidence.

## QPU/QML/QNN implementation practices harvested

The federation now records these reusable engineering patterns:
1. Separate high-level quantum algorithms from hardware-specific compilation.
2. Preserve an explicit intermediate representation boundary.
3. Inspect target capabilities before execution.
4. Track circuit depth, shots, supported/native gates and target backend.
5. Keep classical baselines beside QML/QNN experiments.
6. Treat simulator output and hardware output as different evidence classes.
7. Record provenance, provider, backend, calibration/context and result metadata.
8. Never infer quantum advantage from simulation alone.
9. Keep QPU submission behind a fail-closed execution contract.
10. Reuse LLVM/QIR and compiler concepts for quantum/classical interoperability.

## Evidence references

- Android NNAPI documentation: https://developer.android.com/ndk/guides/neuralnetworks
- Intel OpenVINO: https://docs.openvino.ai/
- NXP eIQ: https://www.nxp.com/design/design-center/software/eiq-ai-development-environment.html
- Apache TVM: https://tvm.apache.org/
- Jittor: https://github.com/Jittor/jittor
- Amazon Braket QPU execution and device-capability documentation: https://docs.aws.amazon.com/braket/
- OpenQASM specification: https://openqasm.com/
- QIR Alliance: https://www.qir-alliance.org/

## Verification result

Source integration completed for the governed adapter/registry layer.

Not yet verified in this environment:
- actual Android NDK/AOSP build
- vendor SDK compilation
- target NPU/GPU/DSP execution
- live QPU submission
- cloud-provider credentials
- hardware calibration-dependent results
- full end-to-end simulator/device smoke tests

Promotion remains fail-closed until those runtime gates produce evidence.

## Learning update

New learning is routed into the existing evidence-first ML layer rather than silently rewriting authoritative behavior. The existing ML engine and learning-record pathway remain the promotion boundary.

## Housekeeping

- Existing federation architecture retained.
- Proprietary SDKs remain external.
- Optional dependencies remain opt-in.
- Quantum hardware remains disabled by default.
- Source/runtime distinction preserved.
- Index/digest update recorded in this harvest entry.
