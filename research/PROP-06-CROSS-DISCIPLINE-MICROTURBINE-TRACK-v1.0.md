# PROP-06 — Cross-Discipline Microturbine Cycle & Application Track v1.0

## Scope
This gate connects the Biupiu Blade/Microturbine stream across automotive, marine, eVTOL, helicopter/turboshaft and unmanned-aircraft applications while keeping each application independently modelled.

## Research findings
A 2025 ResearchGate paper on a modular recuperated micro-gas turbine reports 15–150 kW electrical output, a pressure ratio near 5 for its high-power scheme, 37.3% thermal efficiency at 150 kW, and experimental recuperator/combustor results. These are published research results, not Biupiu performance claims.

A 2026 Energy paper indexed on ResearchGate specifically studies a recuperated micro-gas-turbine hybrid system for eVTOL endurance enhancement.

A 2019 rotorcraft study assessed simple and recuperated gas-turbine thermo-electric systems for a twin-engine medium helicopter mission and reported fuel-economy potential while noting added heat-exchanger weight and transient/surge-margin penalties.

A 2025 Journal of Aircraft study models battery + ICE/generator/rectifier hybrid powertrains for 100 kg multicopters and tailsitters.

## Cross-discipline architecture

### 1. Automotive BT-AUTO
Turbine -> generator -> HV DC bus -> battery -> traction motors.
Primary research role: range extender and high-power demonstrator.
Battery handles launch/transient demand; turbine is not assumed to supply instantaneous peak wheel power.

### 2. Marine BT-MARINE
Turbine -> generator -> DC bus -> battery -> electric motor(s) -> propeller.
Priority metrics: continuous efficiency, corrosion resistance, filtration, acoustic signature, exhaust routing, maintainability and sea-state load response.
Potential roles: auxiliary generation, series hybrid propulsion and high-speed research craft.

### 3. eVTOL BT-EVTOL
Turbine -> generator -> HV DC bus -> distributed electric motors.
Primary role: endurance/range extender rather than direct rotor drive.
Design focus: hover power, transition, cruise, reserve energy, thermal management, redundancy, fault containment and battery peak-power support.
The 2026 eVTOL research specifically supports studying recuperated microturbines at system level rather than treating turbine nameplate power as aircraft propulsion power.

### 4. Helicopter BT-HELI
Two branches:
A. Turbine-generator + electric rotor drive (future hybrid-electric turboshaft).
B. Turbine-generator as auxiliary electrical source/boost system.
Do not assume a microturbine sized for a UAV can directly replace a certified turboshaft. Rotorcraft demands much higher continuous specific power, transient response, containment and certification maturity.

### 5. UAV / VTOL BT-UAV
Small modular turbine-generator range extender.
Research evidence shows microturbine-electric systems can be used to extend endurance, with battery operation reserved for quiet/peak-power portions of a mission.

## Initial cycle-model equations

Fuel energy rate:
P_fuel = mdot_fuel * LHV

Gross turbine-generator electrical output:
P_e,gross = P_fuel * eta_cycle

Net electrical output:
P_e,net = P_e,gross - P_aux - P_cooling

Battery-to-motor wheel/propulsor power:
P_prop = P_batt * eta_inverter * eta_motor

For a series hybrid:
P_batt_dot = P_e,net - P_prop_demand

For a mechanically coupled hybrid:
P_prop = P_mechanical + P_batt * eta_electric_path

These definitions prevent generator output from being counted as free additional engine power.

## Initial module targets

BT-70:
- 70 kW net electrical target
- recuperated
- generator and inverter losses explicitly modelled

BT-140:
- 2 x BT-70
- staged operation and redundancy study

BT-200:
- independent high-power architecture study

BT-300:
- future 300 kW net electrical architecture
- requires independent cycle, turbomachinery, thermal and containment design

## Cross-domain comparison metrics
Every branch will report:
- net electrical kW
- fuel flow
- thermal efficiency
- specific fuel consumption
- kg/kW
- continuous vs peak power
- transient response
- thermal rejection
- acoustic output
- maintenance burden
- redundancy
- certification complexity

## Biupiu Blade integration
The Biupiu Blade and Microturbines stream now includes:
- Jaguar/C-X75 architecture reference
- recuperated microturbine research
- high-speed generator research
- automotive range extender
- marine series hybrid
- eVTOL range extender
- helicopter hybrid/turboshaft research
- UAV endurance/range-extender research
- turbine harmonics/NVH branch
- digital-twin and controls branch

The Blade stream remains a research/design repository. No blade geometry, rotor speed, thrust, aircraft performance, road performance or marine certification claim is considered validated without component or independent test evidence.

## Next validation gate
PROP-07 should implement the numerical cycle model and application mission cases:
- automotive 200/300 kW vehicle
- marine steady cruise + transient duty
- eVTOL hover/transition/cruise
- helicopter representative mission
- UAV endurance mission

The same turbine module must not be assumed optimal across all missions; the comparison engine will identify where scaling or a different architecture is required.


## Phase 2 component registry implementation

The microturbine is now treated as a reusable component, not as a vehicle/aircraft/ship twin.

**Component:** `BPU-CMP-ENERGY-001` — Bioblade recuperated microturbine-generator.
**Simulation:** `BPU-SIM-ENERGY-001` — recuperated microturbine cycle model.
**Cross-divisions:** ENERGY ↔ AUTO ↔ MARINE ↔ AEROSPACE ↔ MATERIALS ↔ ELECTRICAL ↔ AI/COMPUTE.

BT-AUTO, BT-MARINE, BT-EVTOL, BT-HELI and BT-UAV remain application/assembly contexts. Their mission models must reference the component twin and retain application-specific loads, thermal conditions, controls, safety and certification requirements.
