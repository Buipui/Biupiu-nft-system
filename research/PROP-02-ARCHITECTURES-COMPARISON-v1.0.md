# PROP-02 — Independent Propulsion Architecture Comparison

## Purpose
Maintain two independently modelled Biupiu propulsion routes for later comparison. Both are concept-stage architectures and require engineering validation.

## Architecture A — Diesel-electric mechanical rear drive + front e-assist

- Rear/mid-mounted turbocharged diesel engine.
- Mechanical rear transaxle drives rear wheels.
- Crankshaft starter-generator supports starting, energy recovery and torque smoothing.
- Two front electric motors provide temporary AWD, launch assistance and torque vectoring.
- Battery is sized for transient electric power; engine remains the principal sustained energy source.
- Optional microturbine is a separate auxiliary generator research branch, not assumed in the base power budget.

**Advantages to investigate:** established diesel technology, mechanical efficiency at sustained load, potentially lower battery energy requirement.

**Risks:** packaging, vibration, clutch/transaxle integration, front-motor unsprung mass if hubs are used, emissions and thermal management.

## Architecture B — Turbine range-extender / series hybrid

- Micro gas turbine or recuperated gas turbine drives a high-speed generator.
- Electric traction motors drive the axles; no direct mechanical connection from turbine to wheels in the base model.
- Battery buffers transient demand and absorbs regenerative energy.
- Turbine operates near selected efficient operating points where practical.
- Separate power electronics, high-speed generator, recuperator, exhaust and acoustic enclosure required.

**Advantages to investigate:** compact rotating core, multi-fuel potential subject to combustor design, flexible generator placement, no conventional multi-speed gearbox required for traction.

**Risks:** low-load and transient efficiency, recuperator durability, hot exhaust, acoustic signature, high shaft speed, generator and power-electronics losses, start-up response, fuel consumption and certification.

## Jaguar C-X75 reference

The original C-X75 concept used two Bladon Jets microturbines as range-extender generators. Jaguar later developed a different production-intent powertrain using a 1.6-litre twin-charged petrol engine and electric motors. Therefore, the turbine concept and later petrol prototype must not be treated as the same configuration.

## Comparison protocol

Compare both architectures using identical vehicle mass, drag, rolling resistance, battery usable energy, ambient conditions, duty cycles and component efficiency maps.

Required outputs:
- Net wheel power versus speed.
- 0–100 km/h and 80–120 km/h estimates only after validated maps are available.
- Fuel energy per kilometre.
- Battery SOC trajectory.
- Continuous thermal load.
- Generator and inverter losses.
- Noise/order-tracking indicators.
- Mass, packaging volume and maintenance assumptions.

## Decision rule

No architecture is selected from peak power alone. Selection requires measured or defensible component maps, safety analysis, thermal validation, lifecycle cost, serviceability, emissions/noise compliance and prototype testing.
