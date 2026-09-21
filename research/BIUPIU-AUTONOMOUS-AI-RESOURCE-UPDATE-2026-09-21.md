# Biupiu Autonomous AI Resource Update — 2026-09-21

## Official/current candidates
- NVIDIA Isaac Sim: physically based robotics simulation, OpenUSD, ROS2, synthetic data, SIL/HIL.
- NVIDIA Isaac Lab: open-source robot-learning framework supporting reinforcement and imitation learning and multiple physics backends.
- Gazebo Sim: official robotics simulation runtime/library.
- Existing Biupiu ML subsystem: scikit-learn, XGBoost, LightGBM, River, TorchRL, Transformers, FAISS, Optuna, ONNX/ONNX Runtime, MLflow, Opacus, PySyft, Flower and Gymnasium remain adapter candidates.

## New routing priority
1. Simulation-generated data and real telemetry are kept separate.
2. Train/evaluate in Digital Twin environments before any physical deployment.
3. Use deterministic replay and holdout scenarios.
4. Record model version, dataset hash, seed, metrics and environment.
5. Reject autonomous actions outside explicit authority contracts.

## Federated learning
Flower is retained as the federated-learning candidate. Federation aggregates governed model updates, not unrestricted repository content. Secure aggregation and privacy mechanisms require their own implementation and threat-model gates.

## Publisher/resource evidence
NVIDIA's current official documentation describes Isaac Sim's modular physics architecture and Isaac Lab's RL/imitation-learning workflows. These are compatible patterns for the Biupiu adapter architecture, subject to licence and runtime review.
