# MARINE-SIM-02 — Virtual Boatyard / Sea-Test Adapter Contract v1.0

**Date:** 19 September 2026  
**Status:** Architecture gate executed; runtime host validation pending.

## Objective
Turn MARINE-SIM-01 into an adapter-first virtual engineering environment without importing third-party proprietary assets.

## External references verified
- NVIDIA WaveWorks — external/proprietary ocean-wave reference.
- HonuRobotics/gz-maritime — Gazebo maritime buoyancy/thruster reference.
- srmainwaring/asv_wave_sim — Gazebo waves and surface-vessel simulation reference.
- VRX/Gazebo ecosystem — marine robotics scenario reference.
- Naval Group LOTUSim — maritime multi-agent simulation reference.

GitHub search evidence confirms gz-maritime provides buoyancy and thruster functionality and that asv_wave_sim contains wave/surface-vessel simulation plugins.

## Adapter layers
1. **Vessel Model Adapter:** hull geometry, mass, inertia, displacement and propulsion interfaces.
2. **Ocean Adapter:** wave spectrum, amplitude, direction, period, wind, current and surface state.
3. **Hydrodynamics Adapter:** 6-DoF forces/moments, drag, buoyancy and actuator effects.
4. **Sensor Adapter:** GPS/INS, depth, lidar/radar/sonar-style simulation, cameras and telemetry.
5. **Workshop Adapter:** fabrication state, components, work orders, inspections and configuration revisions.
6. **Sea-Test Adapter:** deterministic scenarios, seeds, test objectives, telemetry and pass/fail evidence.
7. **Digital-Twin Adapter:** model version, scenario version, configuration hash and result provenance.

## Virtual boatyard scene
- Design office / CAD review
- Dry dock and slipway
- Hull fabrication bay
- Composite/materials bay
- Mechanical/propulsion bay
- Electrical/automation bay
- Paint/coating/finish area
- Crane/lift zone
- QA and inspection station
- Launch/recovery area

## Sea-test scene
- Protected harbour basin
- Open coastal test zone
- Deep-water test zone
- Variable wind/current/wave profiles
- Maneuvering route
- Acceleration/deceleration route
- Energy/propulsion endurance route
- Sensor/autonomy proving area
- Emergency/recovery scenario area

## Acceptance contract
A simulation result is only accepted when vessel revision, environment revision, scenario seed, solver/configuration metadata and telemetry provenance are recorded together.

Third-party code/assets remain external until licence, security and compatibility review passes. Simulation output is not physical certification.

## Next validation gates
- Host installation and dependency resolution
- Compile/run smoke test
- Baseline vessel buoyancy test
- Baseline wave test
- Propulsion/thruster test
- Sensor telemetry test
- Digital-Twin round-trip test
- Reproducibility comparison
