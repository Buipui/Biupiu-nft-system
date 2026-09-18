# PROP-09 — Cycle Physics & Altitude Screen v1.0

## Executed
Added `simulators/biupiu_cycle_physics_v0_1.py`.

The model introduces a first-order Brayton/recuperated-cycle screen with:
- ISA ambient temperature and pressure versus altitude
- compressor pressure ratio and efficiency
- turbine efficiency
- recuperator effectiveness
- recuperator pressure-drop penalties
- turbine-inlet temperature
- generator efficiency
- accessory load
- estimated air mass flow
- estimated fuel flow
- temperature points through the cycle

## Cross-discipline application
This physics layer is intended to feed the existing:
BT-AUTO / BT-MARINE / BT-EVTOL / BT-HELI / BT-UAV mission models.

For aerospace missions, altitude is now an explicit variable. For marine and automotive use, sea-level/low-altitude cases provide the baseline.

## Engineering interpretation
The calculation is a screening model, not a validated turbine cycle. Compressor/turbine maps, detailed combustion, cooling flows, bearing losses, leakage, heat-transfer limits, recuperator durability, generator maps and control laws still require dedicated models and test data.

The model deliberately treats BT-300 as a future concept rather than a validated 300 kW machine.

## Digital-twin handoff
The next integration should expose cycle outputs as structured machine-readable records and connect them to mission-phase power demand, battery buffering and mass accounting.

## PROP-10
Next gate:
1. couple cycle model to mission profiles;
2. calculate full propulsion-chain efficiency;
3. add turbine + recuperator + generator + fuel-system + battery mass;
4. calculate aircraft/marine/vehicle net system specific power;
5. add sensitivity sweeps for pressure ratio, TIT and recuperator effectiveness;
6. generate digital-twin JSON datasets;
7. flag physically infeasible or low-margin operating points.

Status: research/simulation only; no certification or operational-performance claim.
