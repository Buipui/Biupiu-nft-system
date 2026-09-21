# Biupiu OS Adapter Boundary v0.2

The next gate defines stable contracts for external engines without claiming they are installed or verified.

## Mapped targets
- Unreal Engine MassEntity: data-oriented entities/fragments/processors.
- Unity Entities/DOTS: entity/component-oriented runtime.
- Project Chrono: dynamics, collisions, solvers, vehicle/FSI/sensor modules.
- Gazebo Sim: simulation, sensors, plugins and transport.
- OpenFOAM: CFD solver boundary.
- MQTT/OPC-UA/Modbus: hardware/device gateway.

Each adapter has a health contract and fails closed when its external runtime is unavailable.

## Integration principle
Biupiu owns orchestration, evidence governance, provenance and cross-domain contracts. External engines remain replaceable computational/visual/communications backends.

## Verification
CONTRACT VERIFIED by unit tests when CI passes.
RUNTIME INTEGRATION NOT VERIFIED until the corresponding SDK/runtime is actually built and exercised.
