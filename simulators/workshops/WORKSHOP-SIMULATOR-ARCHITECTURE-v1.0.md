# Biupiu Workshop Simulator Architecture v1.0

The workshop layer is a reusable simulation shell. Automotive and hangar simulators are the reference implementations; other departments inherit the same lifecycle.

## Shared lifecycle
Asset -> inspect -> diagnose -> disassemble -> service/fabricate -> assemble -> calibrate -> validate -> release -> update digital twin.

## Shared subsystems
- Asset/component graph
- Procedure and tool graph
- Measurements and telemetry
- Fault/failure engine
- Parts/material inventory
- Work-order/job-card engine
- Skill/task progression
- Safety interlocks
- Evidence/provenance
- Digital-twin state
- Test/validation gates
- Cross-department component exchange

## Automotive reference
Engine, drivetrain, suspension, steering, brakes, electrical/ECU, thermal/HVAC, body/composites, tyres/wheels, diagnostics, fabrication and road-test cells.

## Hangar reference
Airframe, engine/APU, landing gear, hydraulics, electrical/avionics, flight controls, fuel, environmental systems, inspection/NDT, component shop and ground-test cells.

## Cross-department simulators
- AGRI-WORKSHOP: tractors/implements, irrigation, pumps, sensors, biochar and farm automation.
- BIO-LAB-WORKSHOP: lab equipment, bioprocess skids, sensors, sample workflows and contamination controls.
- TEXTILE-WORKSHOP: fibre preparation, spinning, weaving, knitting, finishing and QC.
- MATERIALS-WORKSHOP: composites, resins, laminates, panels, adhesives and mechanical testing.
- ENERGY-WORKSHOP: storage cells, power electronics, motors/generators, thermal systems and test benches.
- ROBOTICS-WORKSHOP: actuators, joints, controllers, sensors, end-effectors and calibration.
- MARINE-WORKSHOP: hull systems, propulsion, steering, electrical, pumps and corrosion inspection.
- COMPUTATIONAL-DESIGN-WORKSHOP: parametric geometry, simulation setup, digital fabrication and asset validation.

## UE5 strategy
UE5 is the visual/interactivity layer. Domain calculations should remain modular and testable, with adapters for vehicle/aircraft physics, sensor simulation and digital-twin state. SODA.Sim/CARLA/OAS are research references rather than mandatory dependencies.

## Failure-learning loop
Capture expected state -> observed state -> fault hypothesis -> intervention -> test result -> root cause -> confidence -> reusable diagnostic rule. Never auto-apply an unverified repair to a production branch.
