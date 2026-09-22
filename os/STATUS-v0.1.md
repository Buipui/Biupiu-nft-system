# Biupiu OS Core v0.1 — Gate Record

**IMPLEMENTED**
- kernel/orchestration boundary
- capability discovery
- evidence-state guard
- deterministic input sanity checks
- physical/living environment state
- audit ledger
- regression tests

**INTEGRATION TARGETS**
UE5 MassEntity; Unity Entities/DOTS; Project Chrono; Gazebo; OpenFOAM; Raspberry Pi/Arduino; MQTT/OPC-UA/Modbus; existing Biupiu simulators.

**NOT YET VERIFIED**
Native external-engine builds, hardware-in-loop, production OS boot/runtime, physical validation.

**LICENSE BOUNDARY**
Open-source engines remain adapters. OpenFOAM v14 is GPLv3; Project Chrono is BSD; Gazebo Sim is Apache-2.0. Do not copy GPL implementation into proprietary modules.
