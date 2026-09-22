# Biupiu Simulator Federation Harvest — 2026-09-22

## Scope
External federation harvest and native adapter integration for Project Chrono, OpenStudio, EnergyPlus and OpenSim.

## External source records
| Resource | Canonical source | Status | Biupiu role |
|---|---|---|---|
| Project Chrono | https://github.com/projectchrono/chrono | BSD-3-Clause; external dependency/reference | vehicle/multiphysics adapter |
| OpenStudio | https://github.com/NatLabRockies/OpenStudio | open-source; dependency/version review required | architecture/building/design + energy-model adapter |
| EnergyPlus | https://github.com/NREL/EnergyPlus | BSD-3-Clause; external dependency/reference | building-energy solver adapter |
| OpenSim | https://github.com/opensim-org/opensim-core | Apache-2.0; external dependency/reference | movement/biomechanics/environment-agent adapter |

Chrono provides multibody, ground-vehicle, robotics and terramechanics simulation. OpenStudio supports whole-building energy modelling around EnergyPlus and provides C++, Ruby, Python and C# SDK entry points. OpenSim provides C++ libraries plus Java/Python bindings for dynamic musculoskeletal simulation. These are capability references/adapters, not copied source.

## Integration map
Research -> Intelligence -> OS/DMS validation -> Digital Twin -> Federation -> Simulator Adapter -> Domain Simulator -> World/Observation

### Vehicle
Chrono is registered behind CHRONO in software/rnd-os-ai/src/simulator_adapters.py. It feeds the vehicle simulation boundary for multibody dynamics and terrain/vehicle interaction. Traffic logic, vehicle authority, sensors and test-track ownership remain Biupiu-side.

### Architecture / building / design
OpenStudio and EnergyPlus are registered as independent adapters. OpenStudio is the model/workflow boundary; EnergyPlus remains the energy solver boundary. Building geometry/design remains owned by Biupiu computational geometry/CAD/World layers.

### Farming / World / environment
OpenSim is registered as a movement/biomechanics reference. It does not replace crop, soil, water, climate or regenerative-farming models. World remains the visualization/state presentation boundary.

## Native Android integration
The Mini OS/Android layer receives capability identities and fail-closed adapter metadata through the simulator federation manifest. Heavy native simulation is not claimed to execute on Android merely because an adapter is registered; Android acts as a governed endpoint for capability discovery, job/state exchange and lightweight visualization unless a compatible native runtime is actually built and tested.

## Promotion rules
External code remains REFERENCE/ADAPTER until:
PROVENANCE -> LICENCE -> DEPENDENCY -> STATIC -> BUILD -> UNIT -> INTEGRATION -> SMOKE -> REGRESSION -> RUNTIME -> HUMAN PROMOTION.

No proprietary binaries or restricted source are embedded.

## Verification
SOURCE IMPLEMENTATION: CLOSED
SEMANTIC ADAPTER CHECK: CLOSED
SMOKE TEST: SOURCE-LEVEL PASS
ANDROID/UE5/HOST RUNTIME: OPEN
NATIVE THIRD-PARTY BUILD: OPEN
CROSS-SYSTEM REGRESSION: OPEN
HARDWARE/PHYSICAL CORRELATION: OPEN
