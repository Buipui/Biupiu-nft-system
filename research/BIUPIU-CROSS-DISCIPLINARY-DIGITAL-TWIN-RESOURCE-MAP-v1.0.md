# BIUPIU Cross-Disciplinary Digital Twin Resource Map v1.0

Date: 20 September 2026
Status: IMPLEMENTED — research routing map
Purpose: Use Digital Twin capability matching to identify reusable resources across departments instead of searching each department in isolation.

## Core map

| Resource family | Primary role | Primary departments | Secondary routes | Integration mode |
|---|---|---|---|---|
| NASA F´ / FPP | component architecture, interfaces, modelling, code generation, testing | OS, DMS, Aerospace | Robotics, Marine, HMI | adapter/reference; Apache 2.0 |
| Project Chrono | multibody + multiphysics dynamics | Automotive, Marine, Aerospace | Robotics, Composites | library/service; BSD-3 |
| Eclipse Ditto | IoT Digital Twin state, APIs, policy/access | DMS, Digital Twin, Smart Farming | Energy, Manufacturing, Robotics | backend adapter; EPL 2.0 project licence |
| Gazebo | robot/sensor/physics simulation | Robotics, Automation | Agriculture, Manufacturing, Aerospace | simulator adapter; Apache 2.0 |
| NVIDIA Isaac Sim | robotics simulation + synthetic data | Robotics, AI | Manufacturing, World, Vision | licensed reference/service; Apache 2.0 source + separate component terms |
| OpenUSD | 3D world composition and scene interchange | Biupiu World, Digital Twin | Automotive, Aerospace, Marine, Manufacturing | scene/data standard |
| FreeCAD / OCCT | parametric CAD + geometry kernel | Configurators, Manufacturing | Automotive, Aerospace, Marine, Composites | CAD/kernel adapter; LGPL terms |
| OpenFOAM | CFD + multiphysics capabilities | Energy, Automotive, Aerospace, Marine | Materials, Agriculture | isolated solver/service where GPL constraints matter |
| OpenModelica | equation-based modelling and simulation | MATH/Physics, Energy | Automotive, Agriculture, Machines | external solver/service; GPLv3/OSMC terms |
| SUNDIALS | ODE/DAE + nonlinear solvers | MATH/Physics, Simulation | AI/optimisation, all engineering | library candidate; BSD-3 |
| Elmer | FEM multiphysics incl. structural, fluids, acoustics, electromagnetics | Materials, Energy, Photonics/EM | Aerospace, Marine | solver/service; GPL/LGPL components |
| MEEP | computational photonics / FDTD | Photonics, Electromagnetics | Materials, AI | isolated/reference solver; GPL |
| OpenSim | musculoskeletal dynamics | Biomedical | Human-machine systems, biomechanics | library/simulator; Apache 2.0 |
| Open3D | 3D data, point clouds, geometry processing | World, Vision, Digital Twin | Geospatial, Robotics, Manufacturing | library candidate; MIT |
| Assimp | 3D model import | World, Configurators | Automotive, Robotics, Visualization | library candidate; modified BSD |
| CARLA | autonomous-driving simulation | Automotive, Mobility | World, AI, Robotics | simulator/reference; MIT code + CC-BY assets + UE terms |
| AgriTwin / Smart Droplets DT | crop/field/orchard twin patterns | Agriculture | Water, Climate, AI, Geospatial | research/reference; licence must be checked per repository |

## Twin-fit method

TARGET TWIN -> REQUIRED CAPABILITIES -> CANDIDATE MATCH -> GAP ANALYSIS -> ADAPTER -> TEST VECTOR -> EVIDENCE

Example: Vehicle Twin -> rigid/flexible dynamics + tyre + control + CFD -> Chrono/OpenFOAM/CARLA -> adapter contract -> scenario regression

Example: Farm Twin -> soil/climate/crop state + what-if -> AgriTwin/Smart-Droplets patterns + FIWARE/Ditto -> field-schema adapter -> agronomic validation

Example: Robot Twin -> kinematics + sensors + controls + synthetic data -> Gazebo/Isaac Sim -> ROS/transport adapter -> hardware-in-loop

## Departmental rule

A resource discovered for one department is automatically checked for adjacent uses. Each new use receives its own capability, contract and validation record.

## Status semantics

- REFERENCE: research/architecture only.
- ADAPTER-READY: interface mapping exists; implementation not yet runtime-verified.
- SANDBOXED: executable evaluation permitted in isolation.
- INTEGRATED: repository integration completed.
- VERIFIED: integration has execution evidence.
- PROMOTED: approved for the relevant release boundary.

Current state: resource families and cross-domain routing are registered; most external runtime integrations remain REFERENCE or ADAPTER-READY.