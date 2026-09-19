# Biupiu Intelligence — Machine Learning Subsystem v1.0

Date: 19 September 2026
Status: Foundation implemented on isolated branch feat/ml-subsystem-v1

## Purpose
Add a dedicated ML capability layer to Biupiu Intelligence without making the Core OS model-dependent.

## Pipeline
Multilingual research -> evidence/provenance -> ML task specification -> backend router -> model/experiment -> evaluation/drift -> learning record -> OS validation -> human-controlled promotion.

## Capability domains
Classical ML, gradient boosting, online/streaming ML, deep learning, reinforcement learning, retrieval/embeddings, optimisation, portable/edge inference, privacy/federated research, and scientific/physics-aware surrogate modelling.

## Research inputs
NASA and DARPA material informs staged AI engineering, robustness, autonomy, simulation, evaluation and human oversight. MIT, Harvard and Wits provide ML systems, deep-learning, reinforcement-learning, computer-vision, NLP, signal-processing and resource-constrained ML research references. ResearchGate and Emerald Insight are scholarly discovery layers requiring source-level verification. Popular Mechanics is a technology/science context layer, not a substitute for primary evidence.

## Multilingual integration
Consumes the existing Global Multilingual Research & Intelligence Protocol: native-language discovery, transliteration, technical synonyms, identifier-first deduplication, original-language preservation, translation provenance and language-independent evidence classification.

Priority languages include English, Mandarin, Japanese, Korean, Russian, German, French, Spanish, Portuguese, Arabic, Turkish, Hindi and relevant South African languages.

## Open-source strategy
Suitable candidates registered for optional adapters include scikit-learn (BSD-3-Clause), XGBoost (Apache-2.0), LightGBM (MIT), River (BSD-3-Clause), TorchRL (MIT), Transformers (Apache-2.0), FAISS (MIT), Optuna (MIT), ONNX (Apache-2.0), ONNX Runtime (MIT), MLflow (Apache-2.0), Opacus (Apache-2.0), PySyft (Apache-2.0) and Gymnasium (MIT). PyTorch, NetworkX and mixed-license/model-checkpoint ecosystems remain subject to individual licence-file and notice review before redistribution.

No external package is installed or copied by this gate.

## Cross-department routing
AGRI/WATER: yield, irrigation, soil, weather and anomaly detection.
BIO/BIO-GEN/MEDICAL: classification and scientific-data analysis.
MATERIALS/COMPOSITES/ADV-MFG: property prediction and optimisation.
ENERGY: forecasting, optimisation and fault detection.
PHOTONICS: signal processing and optical communications.
ROBOTICS: perception, control and reinforcement learning.
AERO/MARINE/AUTOMOTIVE: simulation, autonomy, telemetry and predictive maintenance.
TEXTILES/FOOD/CONSERVATION: quality, process and ecological modelling.
DIGITAL-TWIN/COMPUTE: surrogate models, retrieval and simulation acceleration.

## Hard boundaries
ML output is not authoritative OS state. No model is promoted solely because training loss improves. Promoted results require provenance, evaluation and reproducibility. Safety-critical outputs require domain validation and human authority. External code is never imported merely because it is open source. Code, model and dataset licences are tracked separately. Machine translation is not scientific validation.

## Gates
ML-01 registry and deterministic core: implemented.
ML-02 benchmark/evaluation harness: next.
ML-03 isolated framework adapters: next.
ML-04 physics-informed and surrogate ML: next.
ML-05 edge/federated ML: next.
ML-06 model registry integration: next.
ML-07 runtime CI and host validation: next.
