# BIUPIU AI/ML ALGORITHM SUITE v1.0

Status: IMPLEMENTED — dependency-light reference layer restored.

Restored algorithm families: supervised regression/classification, unsupervised clustering, anomaly detection, drift monitoring (EWMA/PSI), federated weighted aggregation (FedAvg), asynchronous/staleness-aware aggregation, and tabular Q-learning.

Existing specialist boundaries remain: DSPy for LM-program optimisation, vLLM for inference/serving, Flower/PySyft for federated/privacy adapters, FAISS/Transformers/Optuna/ONNX as optional infrastructure, and Qiskit/PennyLane for quantum ML.

Policy: these reference implementations provide deterministic baselines for verification and simulation. They do not silently replace specialist runtimes or claim production performance. Promotion remains provenance/licence/security/regression/human-gated.

Research basis: the repository's prior ML upgrade explicitly identified continual adaptation, drift-aware learning, quantum ML, federated/privacy ML, ONNX portability, FAISS/NetworkX/Transformers/Optuna and multilingual query profiles as the usable upgrade set.