# PROP-04 — Biupiu Turbine Test Matrix v1.0

## Objective
Evaluate the Jaguar-style microturbine architecture independently from the diesel-electric architecture before selecting a vehicle, aerospace, or marine application.

## Baseline reference
The C-X75 turbine architecture is treated as a reference point: two approximately 70 kW microturbine-generator units feeding an electric drivetrain. It is not assumed that its exact hardware is available, production-ready, or suitable for direct reuse.

## Test blocks

### T1 — Turbine core
Measure:
- corrected mass flow
- pressure ratio
- shaft speed
- turbine inlet/exhaust temperature
- compressor outlet temperature
- fuel flow
- vibration
- overspeed response

### T2 — Recuperator
Sweep:
- thermal effectiveness
- pressure loss
- heat rejection
- transient response
- durability

### T3 — Generator
Measure:
- electrical output versus shaft speed
- generator/inverter efficiency
- cooling requirement
- DC-bus stability
- high-speed rotor containment

### T4 — Vehicle range-extender model
Compare:
- turbine-only generation
- turbine + battery
- battery-only
- diesel + battery

Use identical vehicle mass, Cd, frontal area, rolling resistance and motor assumptions.

### T5 — Marine
Evaluate:
- steady-state duty cycles
- propeller load transients
- continuous-duty fuel consumption
- salt-air filtration/corrosion
- exhaust and acoustic constraints
- redundancy

### T6 — Aerospace
Evaluate first as APU/range extender:
- power-to-mass
- altitude derating
- compressor surge margin
- thermal management
- fire containment
- redundancy
- vibration
- EMI/EMC

Do not infer flight readiness from bench performance.

## Decision metrics
Primary:
1. net electrical efficiency
2. specific fuel consumption
3. continuous kW/kg
4. transient response
5. thermal rejection per kW
6. acoustic output
7. maintenance interval
8. manufacturing complexity
9. system cost
10. safety/certification burden

## Gate rule
No claim of production viability until measurements or independently validated supplier data exist. Simulation results must remain labelled as modelled estimates.

## Future branch
A separate harmonic/NVH branch will investigate turbine blade-pass frequency, combustor noise, exhaust resonance, structural-acoustic coupling and optional synthesized vehicle sound. This branch must not alter the propulsion-energy calculations.
