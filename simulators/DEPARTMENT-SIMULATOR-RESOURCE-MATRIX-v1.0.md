# Biupiu Department Simulator Resource Matrix v1.0

Date: 2026-09-19

| Department | World layer consumed | Primary open-source references | Keep independent |
|---|---|---|---|
| AUTO | terrain, roads, buildings, lighting, weather, materials | CARLA, Project Chrono, SUMO references | vehicle dynamics, traffic logic, sensors, test tracks |
| MARINE | ocean, coast, harbour, weather, lighting, materials | VRX, gz-maritime, VORC, HoloOcean, UNav-Sim | hydrodynamics, vessel dynamics, marine sensors, autonomy |
| AERO | terrain, atmosphere, weather, lighting, materials | JSBSim, FlightGear/SimGear, OpenVSP, AirSim | flight dynamics, avionics, aircraft models, flight tests |
| ROBOTICS | environments, factories, terrain, lighting, materials | Gazebo, MuJoCo, Webots, Genesis, IR-SIM | robot models, controllers, sensors, training |
| AGRICULTURE | terrain, vegetation, water, climate, buildings, roads | open agricultural resources + Farming Simulator as benchmark | crop/farm models, machinery, regenerative workflows |
| ADV-MFG | factories, workshops, materials, lighting | OpenModelica and robotics/physics references | manufacturing process models and machinery |
| AI / DIGITAL TWIN | all approved World scenes | shared simulation interfaces | AI agents, telemetry, state estimation and validation |

## Interlinking contract
All department packages reference World asset IDs instead of copying canonical assets.

A department may create a local derived cache for performance, but the source-of-truth remains in world/.

## Minimum extraction rule
1. retain only components needed by the department;
2. record licence and provenance;
3. create an adapter or manifest rather than copying an entire repository;
4. run compatibility tests before promotion;
5. keep third-party proprietary content outside the Biupiu asset library.

## Validation targets
- deterministic scene loading
- asset provenance validation
- world/department contract validation
- physics adapter smoke tests
- weather/environment parameter propagation
- sensor availability
- cross-platform packaging
- repeatable scenario execution
