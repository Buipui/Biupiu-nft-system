# Biupiu Intelligence — Machine Learning Subsystem v1.0

Date: 20 September 2026
Status: Foundation implemented; federated/privacy research adapter gate advanced

## Purpose
Add a dedicated ML capability layer to Biupiu Intelligence without making the Core OS model-dependent.

## Pipeline
Multilingual research -> evidence/provenance -> ML task specification -> backend router -> model/experiment -> evaluation/drift -> learning record -> OS validation -> human-controlled promotion.

## Federated/privacy resource findings

### PySyft
The current OpenMined/PySyft repository is a privacy-preserving data-science platform built around datasites, permissions, datasets and jobs. Current repository documentation identifies the modern syft package lineage and distinguishes it from legacy PySyft <=0.9 APIs. The Biupiu adapter therefore targets the modern syft package contract rather than assuming legacy APIs.

Useful integration surfaces:
- datasite-based private data access
- permission-controlled datasets
- remote job/data-science workflows
- privacy-preserving research execution

Status: REGISTERED / RESEARCH-ADAPTER / NOT RUNTIME-ACTIVATED.

### Flower
The current Flower repository exposes federated-learning infrastructure including client/server workflows and secure-aggregation components. Its secure-aggregation implementation includes SecAgg/SecAgg+ workflow and client/server modules.

Useful integration surfaces:
- federated learning
- federated analytics
- simulation
- secure aggregation

Status: REGISTERED / RESEARCH-ADAPTER / NOT RUNTIME-ACTIVATED.

### Selection boundary
PySyft and Flower are complementary rather than substitutes:
- PySyft is routed toward privacy-preserving data access, datasites and controlled remote computation.
- Flower is routed toward federated training/analytics orchestration and secure aggregation.

Neither is permitted to become authoritative OS state. Any runtime promotion still requires provenance, licence review, security review, regression, reproducibility and human approval.

## Existing research inputs
NASA and DARPA material informs staged AI engineering, robustness, autonomy, simulation, evaluation and human oversight. MIT, Harvard and Wits provide ML systems, deep-learning, reinforcement-learning, computer-vision, NLP, signal-processing and resource-constrained ML research references. ResearchGate and Emerald Insight are scholarly discovery layers requiring source-level verification.

## Multilingual integration
Consumes the existing Global Multilingual Research & Intelligence Protocol: native-language discovery, transliteration, technical synonyms, identifier-first deduplication, original-language preservation, translation provenance and language-independent evidence classification.

Priority languages include English, Mandarin, Japanese, Korean, Russian, German, French, Spanish, Portuguese, Arabic, Turkish, Hindi and relevant South African languages.

## Open-source strategy
Suitable candidates registered for optional adapters include scikit-learn, XGBoost, LightGBM, River, TorchRL, Transformers, FAISS, Optuna, ONNX, ONNX Runtime, MLflow, Opacus, PySyft, Flower and Gymnasium. Individual licence, provenance, security and compatibility review remains mandatory before runtime promotion or redistribution.

## OpenBooks / open research
ITMO OpenBooks is retained as a research-source class for mathematical modelling, optimisation, algorithms, verification and control. Open-book discovery is reference-first; no unverified book corpus is imported as a runtime dependency.

## Hard boundaries
ML output is not authoritative OS state. No model is promoted solely because training loss improves. Promoted results require provenance, evaluation and reproducibility. Safety-critical outputs require domain validation and human authority. External code is never imported merely because it is open source. Code, model and dataset licences are tracked separately. Machine translation is not scientific validation.

## Gates
ML-01 registry and deterministic core: implemented.
ML-02 benchmark/evaluation harness: next.
ML-03 isolated framework adapters: REGISTERED; PySyft and Flower research adapters added.
ML-04 physics-informed and surrogate ML: next.
ML-05 edge/federated ML: RESEARCH INTEGRATION PREPARED; RUNTIME VALIDATION PENDING.
ML-06 model registry integration: next.
ML-07 runtime CI and host validation: next.

## Current next gate
Build a dependency-free federated adapter contract/test harness, then probe optional PySyft/Flower installations without importing them into the Core OS. Promotion remains fail-closed.