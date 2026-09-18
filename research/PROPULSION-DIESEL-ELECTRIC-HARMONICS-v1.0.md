# Biupiu Propulsion Research Stream v1.0

**Status:** RESEARCH / CONCEPT — not validated for road use
**Related concept:** SF-46 Biupiu AeroBlade GT diesel-electric sports car

## Objective

Develop a robust, testable diesel-electric propulsion architecture targeting **300 kW or greater combined peak system output**, while separating near-term engineering choices from future harmonic/acoustic concepts.

## Baseline architecture — robust-now track

1. Rear/mid-mounted turbocharged compression-ignition engine, mechanically coupled to the rear axle through a conventional reduction gearbox or transaxle.
2. Crankshaft-mounted high-voltage motor-generator for engine starting, torque smoothing, regenerative braking and electrical generation.
3. High-voltage battery sized for transient power, with the engine-generator sustaining average energy demand.
4. Two front high-output electric hub or near-wheel motors for electric AWD and torque vectoring. In production engineering, inboard motors with half-shafts may be preferable for unsprung-mass and durability reasons.
5. Electrically assisted turbocharger or e-turbo-generator as an optional research branch, with thermal and overspeed protection.
6. Biupiu microturbines treated as auxiliary energy-recovery or demonstrator systems until compressor maps, turbine maps, shaft speed limits, thermal loading and net electrical output are measured.
7. AeroBrake and computational-geometry body surfaces remain separate aerodynamic subsystems and require CFD, wind-tunnel and structural validation.

## Power sizing

A 300 kW vehicle target should not be interpreted as 300 kW from the diesel alone. A preliminary architecture can be explored with:

- Engine mechanical peak: 180–240 kW class, subject to selected engine and duty cycle.
- Crankshaft generator contribution: sized for electrical conversion and transient support, not assumed to add net energy.
- Front traction motors: combined peak capability approximately 120–180 kW, subject to battery, inverter, cooling and traction limits.
- Battery: sized by peak current, usable energy, thermal limits and expected duty cycle rather than peak kW alone.

The simulator must calculate net wheel power after generator, inverter, motor, driveline and traction losses. Peak ratings are not continuous ratings.

## Research findings

- Research on diesel hybrid vehicles describes crankshaft and turbocharger motor-generators that can assist transient response, recover excess turbocharger power and manage battery energy flow. See ResearchGate: *Real-Time Energy Management for Diesel Heavy Duty Hybrid Electric Vehicles*.
- A series-hybrid study used a 1.2-litre turbocharged diesel rated around 55 kW as a generator source and modelled a vehicle with approximately 125 kW maximum output, demonstrating that engine sizing depends on duty cycle and battery buffering rather than peak wheel power alone.
- Research on diesel hybrid torque-ripple control shows that a motor-generator can actively counter oscillating engine torque. This is relevant to smoothness and sound-quality work but requires high-bandwidth sensing and control.
- Research on harmonic control of a single-cylinder hybrid powertrain reported reduction of first- and second-order speed ripple through active control. This supports a future harmonic-control stream, not an assumption that sound can be made desirable without NVH testing.
- Research on hybrid-vehicle NVH identifies engine order content, motor/inverter whine, gear rattle, driveline vibration and changing operating modes as interacting sound sources.
- Passive hybrid muffler research indicates that exhaust treatment can reduce selected firing-frequency and high-frequency components, but sound level and character vary with load and enclosure geometry.

## Sound / harmonics split

### Track A — robust-now acoustic engineering

- Use a real multi-cylinder engine with a documented firing order.
- Measure crank position, RPM, cylinder pressure where available, accelerometers, intake pressure, exhaust pressure and microphone channels.
- Create order-tracking plots for engine orders, turbocharger orders, generator electrical orders and gear-mesh orders.
- Use passive exhaust tuning: tuned chambers, absorption sections, resonators, compliant mounts and controlled intake acoustics.
- Avoid deliberately increasing harmful resonance, excessive exhaust backpressure, cabin noise or component fatigue.
- Target a deep, mechanically coherent 1990s-era motorsport-inspired character through measured order balance, not through unverified harmonic claims.

### Track B — future harmonic research

- Active torque-ripple cancellation using the crankshaft motor-generator.
- Active noise cancellation only where latency, sensor placement and actuator authority are demonstrated.
- Digital sound synthesis as an optional interior/showcase layer, clearly distinguished from actual external engine sound.
- Coupled structural-acoustic modelling of engine mounts, exhaust, body panels and diffuser structures.
- Optimization of sound quality against vibration, fatigue, emissions, thermal constraints and legal noise limits.

## Validation gates

1. Engine dyno data acquisition and calibration.
2. Generator efficiency map and inverter loss map.
3. Battery current, SOC, temperature and C-rate constraints.
4. Front-motor torque/speed/thermal limits.
5. Vehicle longitudinal model and traction limits.
6. Exhaust backpressure and thermal model.
7. Order-tracking and acoustic measurement.
8. Hardware-in-the-loop and fault-injection tests.
9. Component-level bench testing before vehicle integration.
10. Independent engineering, braking, crash, EMC, emissions and road-approval review.

## Evidence classification

Documented research is used as design input. Proposed Biupiu layouts are **EXPERIMENTAL / HYPOTHESIS** until measured. The Jaguar C-X75 is a styling and systems reference only; no Jaguar performance or design ownership is implied.
