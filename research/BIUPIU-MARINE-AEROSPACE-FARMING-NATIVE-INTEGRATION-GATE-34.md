# Gate 34 — Marine / Aerospace-Space / Farming Native Simulator Integration

**Date:** 21 September 2026
**Status:** SOURCE INTEGRATED / LOCAL SOURCE SMOKE-LEVEL VALIDATION PENDING

## Unified path
DOMAIN STATE -> NATIVE PHYSICS/MODEL KERNEL -> SIMULATOR ADAPTER -> DMS -> DIGITAL TWIN -> RENDERER/UE5 -> VALIDATION -> PROVENANCE.

## Marine
Native foundation covers surge/sway/yaw state, propulsion force, water drag and deterministic timestep. External research includes LOTUSim/lxdyn, MSS, PythonVehicleSimulator, MARUSim, Stonefish, Aeolus-Ocean, openMSN, PySeidon and marine FMU workflows.

## Aerospace / space
Native foundation covers thrust, drag, gravity, altitude and velocity timestep. External research includes JSBSim, AeroSim, Basilisk, OpenRocket and PX4/FlightGear bridge patterns. Higher fidelity aerodynamic coefficients, 6-DOF rigid-body dynamics, propulsion, atmosphere, orbital mechanics and attitude propagation remain separate modules.

## Farming
Native foundation covers rainfall, irrigation, infiltration, evapotranspiration, soil-moisture state and water deficit. External research includes farm-twin, Farm-Twin, AgriTwin, Agri-twin, WOFOST/AquaCrop/DSSAT patterns and agricultural robotics.

## Rights / evidence
Open-source code is not copied wholesale merely because it is discoverable. Each dependency requires licence, provenance, security and compatibility checks. Proprietary simulator/game assets remain external.

## Gate state
HARVESTED -> CROSS-LINKED -> NATIVE CONTRACTS INTEGRATED.
Runtime build, integration, Digital Twin, renderer and HIL verification remain separate gates.
