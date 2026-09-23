# BIUPIU Deep External + Internal Learning Harvest — 2026-09-23

## External literature harvest

### Digital Twin continual learning
- IEEE Transactions on Mobile Computing (2025): continual reinforcement learning for Digital Twin synchronization/resource allocation; reports faster adaptation to changing network capacity and up to 55.2% lower NRMSE in the studied simulation.
- Springer (2026): federated-learning-driven Digital Twin framework for adaptive resource management in heterogeneous edge environments.
- Springer SN Computer Science (2026): energy-aware Digital Twin allocation for adaptive cloud-native resource management.

### Heterogeneous AI software
- ONNX Runtime Execution Providers provide a common hardware-acceleration abstraction and capability-based subgraph placement across CPU/GPU/NPU and other accelerators.
- ONNX Runtime plugin EPs allow hardware providers to be dynamically registered/loaded and versioned independently from ORT core.
- Qualcomm's 2026 Plugin EP demonstrates this model for Snapdragon/Qualcomm AI hardware.
- Unreal Engine 5.8 NNE provides runtime abstraction and can select an appropriate runtime for model and target hardware; Learning Agents remains experimental.

### Quantum / hybrid learning
- 2026 QML survey covers QNN, QCNN and hybrid quantum-classical architectures.
- 2026 Quantum Machine Intelligence research demonstrates hybrid quantum-classical robust optimisation using stochastic-gradient online learning.
- Current Biupiu quantum architecture remains simulator/classical-baseline first; QPU execution remains separately gated.

## Internal literature cross-reference

Cross-linked against:
- federation_protocol.py F01-F25
- learning.py governed learning/failure/drift primitives
- quantum_federation.py and quantum provider boundaries
- Multicore Architecture Federation
- Digital Twin / Universal Simulator federation gates
- native evolution philosophy
- native coding/engineering matrix
- native system catalogue
- AI accelerator + quantum federation harvest
- OS/DMS subsystem master index
- OEM/adapter federation registry
- UE/NNE compatibility baseline

## Adapted architecture

External evidence is converted into capability contracts, not copied blindly.

New loop:
PASSIVE OBSERVATION -> NORMALISE -> COMPARE AGAINST INTERNAL BASELINE -> SCORE INFORMATION/UNCERTAINTY/RESOURCE VALUE -> STORE LEARNING EVIDENCE -> TRIGGER ACTIVE VALIDATION ONLY WHEN JUSTIFIED -> REGRESSION -> PROMOTION GATE.

## Passive continual learning rule

PASSIVE does not mean STATIC.

While a module is passive, low-cost telemetry, dependency changes, version changes, failure signatures, model drift, simulator observations and performance metadata may continue to update the learning corpus. Passive mode must not silently activate expensive hardware or alter authoritative production behaviour.

Learning may therefore improve future scheduling without keeping every subsystem active.

## Quantum service rule

The quantum service now supports passive observations of workloads, classical baselines, simulator outcomes, uncertainty and resource pressure. These observations can identify candidates for later simulator validation.

QPU execution remains disabled unless the existing independent evidence, security, reproducibility, regression and human-promotion gates pass. Learning does not grant execution authority.

## Optimisation rule

Use the learned matrix to select the least-cost execution path that satisfies the required functionality. Escalate from portable CPU/software to vector/GPU/NPU or quantum simulation only when evidence indicates value. De-escalate when demand or resource pressure falls. Preserve fallback paths.

Priority remains:
SECURITY -> CORRECTNESS -> DETERMINISM -> AUTHORITY -> RESOURCE POLICY -> PERFORMANCE.

## Status

REGISTERED/IMPLEMENTED: external literature harvest; internal cross-reference; passive learning API; passive quantum observation API; F23-F25 federation gates.
OPEN: continuous runtime telemetry integration; hardware benchmark validation; QPU validation; local UE/Android/device tests.

## Sources
- https://ieeexplore.ieee.org/document/10906634/
- https://link.springer.com/article/10.1186/s43067-025-00285-y
- https://doi.org/10.1007/s42979-026-05253-5
- https://onnxruntime.ai/docs/execution-providers/
- https://onnxruntime.ai/docs/execution-providers/plugin-ep-libraries/
- https://www.qualcomm.com/developer/blog/2026/05/qualcomm-launches-the-first-onnx-runtime-plugin-execution-provider
- https://dev.epicgames.com/documentation/unreal-engine/neural-network-engine-overview-in-unreal-engine
- https://www.sciencedirect.com/science/article/pii/S0304397526001829
- https://link.springer.com/article/10.1007/s42484-026-00363-y