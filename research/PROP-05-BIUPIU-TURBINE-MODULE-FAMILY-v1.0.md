# PROP-05 — Biupiu Turbine Module Family v1.0

## Evidence anchor
Jaguar's C-X75 became a working prototype using advanced hybrid-electric technology; the production programme was cancelled. The C-X75 is a historical architecture reference, not a directly reusable production component.

A 2025 Case Studies in Thermal Engineering paper hosted on ResearchGate reports a modular recuperated micro-gas-turbine concept spanning about 15–150 kW electrical output, with a reported 37.3% fuel-electric efficiency at its 150 kW design point. These are research results, not certification claims.

## Independent Biupiu modules

| Module | Electrical target | Role | Status |
|---|---:|---|---|
| BT-30 | 30 kW | bench/APU/UAV research | concept |
| BT-70 | 70 kW | C-X75-scale demonstrator | concept |
| BT-140 | 140 kW | twin-module vehicle/marine demonstrator | concept |
| BT-200 | 200 kW | high-performance range extender | future |
| BT-300 | 300 kW | large propulsion generator | future |

These are design targets, not measured outputs.

## Common architecture
Air intake -> compressor -> recuperator -> combustor -> turbine -> generator -> power electronics -> HV DC bus.

Recuperation can improve cycle efficiency but adds mass, pressure loss, thermal stress and packaging complexity.

## BT-70 baseline
Target 70 kW electrical with a high-speed permanent-magnet generator, recuperated cycle, modular hot section, independent control electronics and instrumentation for pressure, temperature, shaft speed, fuel flow and vibration.

Do not fix final rpm, turbine inlet temperature, compressor pressure ratio or blade geometry until cycle analysis and component maps exist.

## BT-140
Two BT-70 modules operate independently on a common DC bus. Potential advantages are redundancy, staged operation, improved low-load operation and modular maintenance. The penalty is duplicated balance-of-plant hardware.

## BT-200 / BT-300
Do not scale BT-70 linearly. Turbomachinery, recuperator, generator, bearings, thermal management and containment require separate designs.

## Application derivatives
### Automotive
Use the turbine primarily as a range extender/generator. Battery and electric motors provide transient power.

### Marine
Prioritize continuous-duty operation, corrosion protection, filtration, maintainability, exhaust routing and load transients.

### Aerospace
Initial target is APU/range-extender research. High-altitude distributed-propulsion studies demonstrate the importance of off-design modelling and altitude effects. Flight use requires separate structural, thermal, propulsion, fire, redundancy and certification work.

## Gate criteria
1. Compressor/turbine maps available.
2. Cycle model closes mass and energy balances.
3. Generator and inverter losses included.
4. Recuperator pressure loss and effectiveness modelled.
5. Battery transient buffering modelled.
6. Thermal rejection sized.
7. Overspeed/containment concept reviewed.
8. Independent engineering review completed.

All Biupiu performance figures are targets unless explicitly identified as published research data.
