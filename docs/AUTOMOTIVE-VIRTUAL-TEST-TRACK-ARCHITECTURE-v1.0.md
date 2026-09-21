# Biupiu Automotive Virtual Test Track Architecture v1.0

## Runtime layers
1. Biupiu vehicle model
2. Biupiu parameterised test-track model
3. PHYS-SYS physics adapter
4. Assetto Corsa runtime adapter
5. Common telemetry bus
6. Engineering analysis layer
7. Digital Twin and provenance
8. Biupiu World release layer

## Pipeline
Track data -> procedural/original geometry -> collision/NAV -> runtime adapter -> telemetry -> analysis -> Digital Twin.

## Scenario classes
Acceleration/top-speed, braking/ABS, constant-radius cornering, transient lane change, slalom, wet/low-mu, rough-road, grade/towing, aero stability, EV/hybrid energy, autonomy and endurance.

## Boundary
This is a research/development simulator, not certified brake, crash, tyre, structural, emissions or road-approval testing.
