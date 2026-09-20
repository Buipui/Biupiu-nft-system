# Vehicle Parameter Register — Gate 02 v1.0

**Date:** 20 September 2026  
**Scope:** Hypercar and expedition/overlander case studies  
**Status:** EXECUTED — preliminary evidence pass; design conclusions remain OPEN

## Evidence classes
- **A — externally supported:** directly supported by an identified primary, publisher or supplier source in this pass.
- **B — provisional:** user-supplied or secondary information requiring independent verification.
- **C — unknown:** no reliable value established in this pass; do not use as a design input.

## Verified or externally supported findings

| Parameter | Current record | Class | Required next action |
|---|---|---:|---|
| Flax-fibre composite damping | Published studies report approximately 2–3× damping versus CFRP under specific low-frequency/low-strain conditions; results depend on test method, layup and frequency. | A | Extract full test conditions and build material-card ranges. |
| Flax outer plies | An automotive semi-structural study reported damping-ratio increases of approximately 53.6% with one external flax layer and 93.9% with two; it also reported reduced modulus/strength in tested configurations. | A | Do not generalize to all layups; reproduce with coupon testing. |
| Flax/carbon hybrid PA11 | A 2024 study reported a 20% higher damping factor than pure carbon reference in its tested system, while hybridization improved selected tensile and impact measures. | A | Obtain full dataset and define matrix/fibre-volume-specific material cards. |
| BorgWarner HVH250 | BorgWarner public release reports 175 kW peak and 425 Nm per motor at 350 V for a heavy-duty truck application. | A | Verify exact HVH250 variant, continuous rating, mass, dimensions, cooling and duty cycle before packaging. |
| Hypercar mass target | Sub-1,000 kg remains a project target, not a demonstrated result. | B | Produce complete mass budget including battery, cooling, controls, safety systems, fluids and structure. |
| Dual YASA front axle | Proposed architecture remains a concept; motor variant, output, mass, inverter and thermal integration are not verified in this pass. | C | Verify OEM technical data and model torque/traction limits. |
| Audi 4.2 TDI CCFA/CKDA | Exact output, mass, dimensions, accessory layout and packaging differences remain unverified in this pass. | C | Obtain engine-code-specific workshop/OEM documentation. |
| OM606 / 6BT fuel compatibility | Biodiesel and WVO suitability cannot be accepted from general reputation alone; filtration, viscosity, temperature, seals, injection and durability must be validated. | C | Create fuel-system compatibility and endurance test plan. |
| Unimog P2 sandwich | Proposed 254 mm driveline extension and forward engine movement remain unverified. | B | Measure bellhousing, clutch, torque-tube, radiator, steering and cab clearances on a specific chassis. |

## Conservative mass-budget framework

No final mass claim is accepted until each subsystem has a measured or sourced mass. Required line items:

- donor chassis, subframes and retained suspension;
- engine and complete ancillaries;
- transmission, transfer case, differentials and shafts;
- electric motor(s), inverter(s), cabling and cooling;
- battery pack, enclosure, BMS, contactors and protection;
- body panels, bonding, inserts, glazing and closures;
- brakes, steering, wheels and tyres;
- seats, restraints, crash structures and fire protection;
- thermal systems, fluids, exhaust/after-treatment where applicable;
- wiring, control units, sensors and service margins.

## Conservative packaging rules

1. No firewall, chassis rail, suspension pickup or torque-tube modification is approved from nominal dimensions alone.
2. Composite panels are initially treated as non-primary or semi-structural unless validated by load cases, joints, crash requirements, environmental conditioning and repair procedures.
3. Metal-to-composite torque-transfer interfaces require dedicated joint design, fatigue analysis and coupon/subcomponent testing.
4. Torque assist, differential locking and brake-based yaw control are not labelled true wheel-to-wheel torque vectoring without independently controllable wheel torque and a validated control model.
5. All high-voltage architecture requires isolation monitoring, fusing, contactor logic, crash disconnect strategy, service disconnects and thermal runaway controls.

## Gate 02 result
- **Executed:** preliminary evidence classification, parameter register and conservative design constraints.
- **Implemented:** repository record and next-action routing.
- **Verified:** selected material-study findings and public HVH250 application rating only.
- **Open:** engine data, YASA data, donor geometry, complete mass budget, FEA, thermal model, control integration, runtime simulation and physical validation.

## Gate 03 entry criteria
A source-backed, unit-consistent parameter sheet for one selected hypercar donor and one selected overlander donor, followed by transparent mass and clearance calculations with uncertainty ranges.
