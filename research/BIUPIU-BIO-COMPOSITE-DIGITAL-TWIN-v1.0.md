# Biupiu Bio-Composite Digital Twin Integration v1.0

Date: 18 September 2026  
Status: Architecture / simulation integration specification

## Purpose
Connect the plant-material registry, Materials Genome, blade/micro-turbine simulations, manufacturing data and physical tests into one traceable digital-twin loop.

## Twin object model
PLANT → FEEDSTOCK → FIBRE → TREATMENT → MATRIX → LAMINATE → COMPONENT → ROTOR → SYSTEM → VEHICLE / VESSEL / AIRCRAFT

Each object receives: stable ID, provenance, evidence state, material batch, geometry version, manufacturing parameters, environment, sensor channels, simulation model/version, test result, failure mode, uncertainty and IP state.

## Blade twin inputs
air density; temperature; rotor diameter; blade geometry; fibre type; fibre orientation; fibre volume fraction; matrix; laminate stacking; core density; coating; RPM; aerodynamic loads; centrifugal loads; humidity; temperature; erosion assumptions; manufacturing defects.

## Simulation chain
CAD → BEM/CFD → AEROELASTIC LOADS → FEA → MODAL/BUCKLING → FATIGUE → THERMAL/MOISTURE SENSITIVITY → DIGITAL-TWIN STATE

## Experimental feedback
Where applicable: RPM, torque, thrust, electrical output, vibration, strain, temperature, humidity, blade deflection, acoustic signature, mass/balance, erosion and delamination/crack observations.

## Optimisation loop
The AI/optimisation layer can vary plant species, fibre treatment, orientation, hybrid ratio, resin, ply thickness, core, blade geometry and manufacturing parameters.
Objective functions: mass + stiffness + fatigue life + vibration + moisture sensitivity + cost + embodied impact + manufacturability.
Constraints must include required structural load cases and safety factors before promotion.

## Department routing
ENERGY/MICROTURBINE ↔ MATERIALS/COMPOSITES ↔ HEMP/TEXTILES ↔ AERO ↔ MARINE ↔ ADV-MFG ↔ ROBOTICS ↔ AI/COMPUTE ↔ DIGITAL-TWIN

## Evidence states
T0 literature candidate; T1 material coupon; T2 laminate coupon; T3 component test; T4 rotating subassembly; T5 controlled prototype; T6 integrated system test; T7 representative environment; T8 independently replicated/qualified evidence; T9 production-qualified evidence.
These states are separate from technology-readiness claims and certification.

## Immediate test queue
1. Hemp/epoxy baseline. 2. Flax/epoxy baseline. 3. Hemp/flax hybrid. 4. Hemp/flax/basalt hybrid. 5. Bamboo/epoxy secondary laminate. 6. Kenaf/jute comparison. 7. Moisture-conditioned specimens. 8. Thermal cycling. 9. Fatigue coupons. 10. Small rotating demonstrators with strain/vibration instrumentation.

All results feed back into Materials Genome and the blade digital twin.

## Phase 2 component-first implementation

The digital twin now terminates at component/subsystem level rather than treating complete vehicles, vessels, aircraft, eVTOLs or helicopters as twin objects.

**Registry:** `research/BIUPIU-COMPONENT-REGISTRY-v1.0.md`
**Protocol:** `research/BIUPIU-SYSTEM-LOGGING-CROSS-DIVISION-PROTOCOL-v1.0.md`

**Component twin examples:** BPU-CMP-MAT-001 HempCarbon structural panel; BPU-CMP-ENERGY-001 Bioblade recuperated microturbine-generator; BPU-CMP-AERO-001 AeroBrake; BPU-CMP-AERO-002 active diffuser; BPU-CMP-AERO-003 rear air-jet module.

Platform records reference these component twins through assembly/application maps. This prevents duplicated technical records across automotive, marine and aerospace applications while preserving application-specific loads, environments and certification requirements.
