# Biupiu Smart Systems Federation — CAN/PLC Intelligence Layer v1.0
Date: 2026-09-21
Status: INTEGRATION BRANCH — ARCHITECTURE HARVESTED; RUNTIME/CI EVIDENCE PENDING

## Priority
Promote modular CAN/CAN-FD, PLC, ISO 11783/ISOBUS, SAE J1939, CANopen and deterministic functional-controller architecture to a first-class Smart Systems knowledge layer.

## Core design rule
One module performs one bounded primary function and exposes explicit inputs, outputs, state, diagnostics, safety state and provenance. Higher-level Intelligence may advise, optimise, simulate and coordinate; deterministic local controllers retain bounded control authority.

## Canonical flow
Sensor/Actuator → Functional ECU/PLC → CAN/CAN-FD or industrial gateway → Site/Farm Node → DMS boundary → Biupiu Intelligence → Digital Twin/Simulation → validated advisory → governed actuation.

## Harvested standards
- ISO 11783: open agricultural equipment interconnect architecture; sensors, actuators, control elements and information/display units communicate through standardized mechanisms.
- ISO 11783-3:2026: current 2026 application/transport/network layer; maps to CAN and includes message priority, arbitration, error detection and transport handling.
- ISO 11783-9: Tractor ECU/gateway concept.
- ISO 11783-10: Task Controller and management-information interchange.
- ISO 11783-12: diagnostics services; 2026 FDIS is under approval.
- ISO 11783-14: sequence control.
- SAE J1939: reference architecture underlying major parts of the agricultural communication model.
- CANopen: reusable higher-layer modular-device patterns.
- IEC 61131-3: PLC programming/control model and interface boundary.

## Functional module catalogue — baseline
SOIL_SENSOR, CLIMATE_SENSOR, WATER_LEVEL, FLOW_METER, PUMP_CONTROL, VALVE_CONTROL, IRRIGATION_CONTROL, NUTRIENT_DOSING, VENTILATION, LIGHTING, WEATHER_INPUT, POWER/BATTERY, FILTRATION, COMPOST/BIOCHAR_PROCESS, LIVESTOCK_WATER, GATEWAY, HMI, DIAGNOSTICS, SAFETY_INTERLOCK, MAINTENANCE.

Each module requires:
1. unique module ID
2. capability declaration
3. input schema
4. output/command schema
5. operating states
6. timeout/fault behavior
7. safe state
8. diagnostics
9. timestamp/source/provenance
10. simulation/test profile
11. firmware/software version
12. promotion state

## Intelligence boundary
The Intelligence layer must not silently replace deterministic safety/control logic. Learning is versioned and evidence-backed. Proposed optimisation is distinguishable from validated control. Actuation requires the existing OS/DMS authorization and validation path.

## Security and assurance
Apply fail-closed authorization, authenticated boundaries, least privilege, replay/timeout protection, diagnostic logging, deterministic fallback and explicit human/operator authority. Learning-enabled behavior must be continuously evaluated rather than treated as inherently correct.

## Evidence status
ESTABLISHED: ISO 11783 architecture and 2026 Part 3 publication; DARPA Assured Autonomy's continual-assurance framing.
SUPPORTED: modular autonomy/control patterns derived from authoritative program descriptions.
PRELIMINARY: direct transfer of these patterns into Biupiu-specific implementations.
HYPOTHESIS: performance gains from any particular Biupiu topology until benchmarked.

No third-party code is copied by this architecture harvest. Implementation must undergo license/provenance review before reuse.
