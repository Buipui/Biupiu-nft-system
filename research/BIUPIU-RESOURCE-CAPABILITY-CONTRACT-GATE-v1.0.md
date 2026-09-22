# BIUPIU Resource Capability Contract Gate v1.0

Date: 20 September 2026
Status: IMPLEMENTED — contract/schema gate; executable verification pending

## Objective
Convert research resources into explicit, bounded capability contracts before executable promotion.

## Contract schema
RESOURCE_ID | OWNER | VERSION | LICENCE | CAPABILITY | INPUTS | OUTPUTS | INTERFACE | DEPENDENCIES | SECURITY | DIGITAL_TWIN_FIT | DEPARTMENT_ROUTES | SIMULATOR_ROUTES | CONFIGURATOR_ROUTES | ADAPTER | TEST_VECTOR | EVIDENCE | PROMOTION_STATE

## Initial contract register
| Resource | Capability | Main route | Licence boundary | State |
|---|---|---|---|---|
| NASA F´ / FPP | component interfaces, deployment/test architecture | OS/DMS/Aerospace | Apache 2.0; verify component terms | REFERENCE |
| Project Chrono | multibody/multiphysics dynamics | Automotive/Marine/Aerospace | BSD-3 | REFERENCE |
| Eclipse Ditto | Digital Twin state/API/policy | DMS/Smart Farming/Manufacturing | EPL-2.0 project terms | REFERENCE |
| Gazebo | robotics/sensor/physics simulation | Robotics/Automation | Apache 2.0 | ADAPTER-READY |
| Isaac Sim | robotics simulation/synthetic data/OpenUSD | Robotics/AI/World | mixed runtime/component terms | RESTRICTED-REFERENCE |
| OpenUSD | scene composition/interchange | World/Digital Twin | project/component terms per use | REFERENCE |
| FreeCAD/OCCT | parametric CAD/geometry | Configurators/Manufacturing | component licences | REFERENCE |
| OpenFOAM | CFD/transport/thermal modelling | Automotive/Marine/Aerospace/Energy | GPL boundary | ISOLATED-SOLVER-REFERENCE |
| OpenModelica | equation-based modelling/control | Physics/Energy/Machines | GPLv3/project terms | ISOLATED-SOLVER-REFERENCE |
| SUNDIALS | ODE/DAE/nonlinear/time integration | Simulation/Physics | BSD-3-Clause | ADAPTER-READY |
| Elmer | FEM/multiphysics | Materials/Energy/Photonics | mixed GPL/LGPL | ISOLATED-SOLVER-REFERENCE |
| MEEP | FDTD computational photonics | Photonics/EM | GPL | ISOLATED-SOLVER-REFERENCE |
| OpenSim | biomechanical simulation | Biomedical | Apache 2.0 | REFERENCE |
| Open3D | point-cloud/3D geometry | World/Geospatial/Robotics | MIT | ADAPTER-READY |
| Assimp | model import/interchange | World/Configurators | modified BSD | ADAPTER-READY |
| CARLA | autonomous-driving simulation | Automotive/AI/World | mixed code/assets/engine terms | RESTRICTED-REFERENCE |

## Adapter contract
Adapters must:
1. isolate external licence boundaries;
2. expose a stable Biupiu-owned interface;
3. validate units, coordinate frames, schemas and error semantics;
4. prevent external code from acquiring OS authority;
5. emit provenance and version metadata;
6. support deterministic smoke/regression tests;
7. fail closed on unsupported or ambiguous inputs.

## Digital Twin routing
CAPABILITY CONTRACT -> TWIN REQUIREMENTS -> GAP ANALYSIS -> ADAPTER -> TEST SCENARIO -> EVIDENCE

A resource may serve multiple departments, but every route gets its own validation evidence.

## Multi-AI review
Architect: boundary/dependency direction.
Code: minimal adapter design.
Verification: contract/test completeness.
Security: licence/dependency/privilege/data-flow review.
Research: provenance/version/licence evidence.
Integration: cross-department routing/conflict reconciliation.

## Promotion
REFERENCE -> ADAPTER-READY -> SANDBOXED -> INTEGRATED -> VERIFIED -> PROMOTED

Restricted path:
RESTRICTED-REFERENCE -> LICENSED-ACCESS -> SANDBOXED -> VERIFIED

No promotion without executable evidence.

## Current gate
Contract architecture: IMPLEMENTED.
Candidate register: IMPLEMENTED.
Executable adapters: NOT CLAIMED.
Runtime/compiler/CI evidence: PENDING.

## Next gate
Adapter Specification + Test Vector Gate: deterministic machine-readable adapter contracts and tests for SUNDIALS, Open3D/Assimp, Gazebo and Project Chrono.
