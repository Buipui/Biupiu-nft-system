# Biupiu Official Publisher Resource Harvest — Gate 35

Date: 2026-09-21
Status: HARVESTED / LICENCE-GATED / INTEGRATION DESIGN REGISTERED

## Objective
Harvest official publisher/developer resources before third-party mirrors and treat publisher documentation as authoritative discovery material, while preserving Biupiu's independent implementation boundary.

## Official publisher lanes
- NVIDIA: Isaac Sim, Isaac Lab, Omniverse Physics, Warp/Newton and CUDA-Q. Isaac Sim exposes extensible physics/simulation, OpenUSD workflows, ROS2, SIL/HIL and synthetic-data workflows; Isaac Lab is the robot-learning layer. CUDA-Q supplies C++/Python hybrid quantum programming and multiple simulation backends. 
- Gazebo: official simulation libraries and command-line/runtime documentation.
- Google DeepMind / MuJoCo: physics and learning ecosystem; use official APIs and licences only after compatibility review.
- Microsoft / Azure Digital Twins and related standards documentation: contextual Digital Twin patterns, subject to service/licence boundaries.
- Khronos: OpenUSD/glTF and graphics interoperability standards where applicable.
- ROS/Open Robotics: middleware and simulator integration contracts.
- Qiskit / IBM Quantum, PennyLane, Cirq and QuTiP: quantum-computing/simulation research lanes; adapters remain optional and licence/version gated.
- Official aerospace/marine/agriculture publishers and standards bodies are discovery authorities; vendor/game publisher assets remain rights-gated and are never copied merely because they are searchable.

## Promotion rule
Official publisher status raises source authority, not automatic integration authority. Every resource passes:
DISCOVER -> OFFICIAL-SOURCE CHECK -> LICENCE/TERMS -> SECURITY -> API/ABI REVIEW -> VERSION PIN -> ADAPTER -> TEST -> PROVENANCE -> PROMOTION.

## Current useful integrations
1. Backend-neutral simulation contracts inspired by modular physics APIs.
2. OpenUSD/glTF asset interchange boundary.
3. ROS2/transport adapter boundary.
4. RL/imitation-learning adapter boundary.
5. Quantum simulator adapter boundary.
6. Digital-Twin event/state/provenance contracts.
7. Synthetic-data and replay logging.
8. Federation discovery metadata.

No proprietary publisher binaries, credentials, signing keys, copyrighted game assets or closed datasets are committed by this gate.
