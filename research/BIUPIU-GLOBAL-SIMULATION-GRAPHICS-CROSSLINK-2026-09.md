# Biupiu Global Simulator & Graphics Cross-Language Crosslink — September 2026

## Scope
Cross-language discovery of simulator, graphics, robotics, Digital Twin, physics and rendering resources in German, Japanese, Chinese, South Korean and Russian sources, cross-linked to the existing global simulator/graphics resource layer.

## High-value findings

### Germany / German
- DLR OOS-SIM: hardware-in-the-loop orbital robotics, multibody/contact dynamics, orbital lighting, stereo vision, LiDAR and IMU. Relevant to AEROSPACE, ROBOTICS, DIGITAL-TWIN and VIRTUAL-HANGAR validation.
- DLR research examples use MuJoCo, Gazebo and PyBullet for simulation/control development.
- Fraunhofer IML demonstrates Isaac Sim + photorealistic rendering + synthetic sensor data + reinforcement learning + Digital Twin + sim-to-real for industrial robot fleets.
- Fraunhofer IOSB-INA demonstrates Isaac Sim/MuJoCo training and ROS2/Gazebo integration for industrial and humanoid robotics.
- University of Stuttgart AeRoShip uses ROS + Gazebo for airship simulation/control, relevant to UAV/AIRSHIP/AEROSPACE.

### Japan / Japanese
- J-GLOBAL/JST record for DISCOVERSE describes an open-source Real2Sim2Real framework using 3D Gaussian Splatting + MuJoCo, supporting existing 3D assets, robot models, ROS plugins, multiple sensors and parallel simulation.
- AIST physical-AI safety work describes a photorealistic mobile-manipulation evaluation framework based on MuJoCo that loads 3D Gaussian Splatting environments, converts 3DGS to voxel representations for collision checking and depth maps for navigation evaluation.
- J-STAGE literature documents simulator architecture involving Gazebo, multiple physics engines, high-quality 3D rendering and simulated sensors.

### China / Chinese
- Chinese Academy of Sciences material describes an end-to-end humanoid-robot simulation development platform combining high-precision physics, real-time rendering, multi-sensor perception, OpenUSD/URDF import, ROS2 APIs, multi-physics, collision detection, distributed/cloud simulation and AI training.
- Shenyang Institute of Automation research demonstrates multi-agent transfer reinforcement learning for wireless cloud robotics and validates control tasks using OpenAI Gym + MuJoCo. Relevant to ROBOTICS, AI, CONTROL, COMMUNICATIONS and DIGITAL-TWIN.
- CAS Robotics Laboratory covers machine vision, autonomous behaviour, brain-inspired computing, flying robots, biomimetic robots and online learning/scene understanding.

### South Korea / Korean
- KAIST SGVR Lab is researching scalable graphics, rendering, ray tracing, neural rendering, vision and robotics.
- KAIST 2026 work integrates actuator thermal models into physics simulation for higher-fidelity sim-to-real transfer. The model estimates rotor temperature and torque degradation inside the simulator and was compared against a real robotic testbed.
- KAIST results include current 2026 work on neural rendering, Gaussian radiance transport and learned multi-agent/robot navigation.

### Russia / Russian
- Math-Net.Ru research provides mathematical foundations relevant to robot optimal control, Lie groups, SE(2)/SO(3), rolling/contact mechanics and optimisation.
- A 2025 Kazan University paper indexed through Math-Net.Ru evaluates ROS/Gazebo navigation and obstacle-avoidance algorithms in virtual environments, including InsertBug/TangentBug.
- Russian mathematical-control literature is routed to MATHEMATICS, COMPUTE, CONTROL, ROBOTICS and GEOMETRY rather than treated merely as background reading.

## Crosslinks to Biupiu architecture

### Virtual Hangar / Aerospace
DLR OOS-SIM + JSBSim + Gazebo + OpenUSD + Isaac Sim.

### Robotics factory
Fraunhofer simulation methodology + Isaac Sim/MuJoCo + ROS2/Gazebo + synthetic data + reinforcement learning + Digital Twin.

### Aerospace / UAV / airship
University of Stuttgart AeRoShip + Gazebo/ROS + JSBSim + Biupiu aerospace models.

### Marine
Existing Stonefish/Chrono layer remains the preferred marine simulation branch; multilingual research should add hydrodynamics, perception and underwater sensor models where validated.

### Graphics / Digital Twin
OpenUSD + Gaussian Splatting + Open3D + Blender + renderer backends. Japanese AIST/DiscoverSE results strengthen the 3DGS-to-physics collision/navigation bridge.

### AI / Intelligence
RL + domain randomisation + synthetic sensor generation + sim-to-real validation. Korean actuator thermal modelling adds a physical degradation channel that can improve realism.

### Mathematics / Computational Geometry
Russian Lie-group, optimal-control and contact/rolling mathematics becomes a validation/research source for robot kinematics, trajectory optimisation and geometry algorithms.

## New cross-language integration rule
LANGUAGE → SOURCE → IDENTIFIER → EVIDENCE → RESOURCE TYPE → DEPARTMENT → SIMULATOR ADAPTER → DIGITAL TWIN → AI TRAINING → VALIDATION → PROVENANCE

No external simulator, model, dataset, code or asset is treated as incorporated merely because it was discovered. Licence, compatibility, security, provenance and technical validation remain mandatory.

## Priority candidate stack
1. OpenUSD — world/asset interchange
2. Isaac Sim / Isaac Lab — high-fidelity robotics and synthetic data
3. MuJoCo — robotics/contact/control research
4. Gazebo — ROS2/system simulation
5. Project Chrono — vehicle/multibody/FEA/FSI
6. JSBSim — aerospace flight dynamics
7. Stonefish — underwater/marine
8. Open3D — geometry/point clouds
9. Gaussian Splatting / DISCOVERSE research — photorealistic Real2Sim2Real
10. Blender/O3DE/Wicked Engine/bgfx/Filament — rendering backends
11. KAIST neural-rendering research — graphics/AI research input
12. Russian mathematical-control literature — optimisation/control foundations

## Status
DISCOVERY: COMPLETE FOR THIS CROSS-LANGUAGE PASS
CROSSLINK: REGISTERED
REPOSITORY ROUTING: REGISTERED
AUTOMATIC INCORPORATION: NOT ASSUMED
LICENCE/SECURITY/COMPATIBILITY VALIDATION: REQUIRED BEFORE CODE OR ASSET MERGE