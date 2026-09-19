# Biupiu Automotive Real-World Research Harvest v1.0

**Date:** 20 September 2026  
**Protocol:** Research Harvest / Evidence Classification / Cross-Department Routing  
**Scope:** Automotive concepts identified in Biupiu historical chats and repository records  
**Purpose:** Harvest usable external research, experimental evidence, engineering references and validation pathways for Biupiu Intelligence and the repository library.

## Executive finding

The harvest confirms that several Biupiu automotive concepts have direct or closely related real-world research. The strongest evidence clusters are:

1. active aerodynamic braking / air-brake systems;
2. active rear diffusers and underbody flow control;
3. rear air-jet active flow control;
4. hemp and hybrid hemp/carbon composites for automotive structures and panels;
5. hemp-derived porous carbon for supercapacitors;
6. recuperated micro-gas-turbine range extenders for electric vehicles.

The air-cushion concept has strong real-world engineering literature for air-cushion vehicles and ground-effect vehicles, but this evidence should NOT be treated as validation of a conventional road car using an air cushion. That specific Biupiu implementation remains a hypothesis requiring dedicated CFD and experimental testing.

## Evidence map

| Biupiu stream | External evidence | Evidence state | Biupiu routing |
|---|---|---|---|
| AeroBrake / aerodynamic braking | Experimental/numerical sports-car study of air-brake placement and movable aero elements; reported changes in drag/lift and braking distance | Supported Research | AERO → BRAKES → CONTROL → CFD |
| Active diffuser | Passenger-car active translating rear diffuser studied with CFD under rotating-wheel/moving-ground conditions | Supported Research | AERO → UNDERBODY → CFD |
| Rear air jets | DrivAer vehicle numerical study reports multi-jet rear flow control with 11.80% drag reduction in the studied configuration | Supported Research | AERO → FLOW-CONTROL → ACTUATION |
| Air-cushion / underbody cushion | Air-cushion vehicle CFD research studies lift, drag, clearance, pressure and wake; WIG/ground-effect literature studies air cushion and lift/drag behaviour | Supported Research for adjacent systems; Biupiu road-car implementation unresolved | AERO → GROUND-EFFECT → CFD |
| Hemp automotive composites | Experimental hemp/glass composites, hemp/carbon/ramie composites, hemp/glass bumper simulations, hemp-based automotive panels and 2026 hemp/coconut epoxy automotive composites | Established/Supported Research at material-test level | MATERIALS → HEMP → COMPOSITES → VEHICLE |
| HempCarbon / energy storage | Hemp-derived activated carbons experimentally demonstrated as supercapacitor electrodes; newer work reports high surface area, capacitance and cycle retention | Supported Research | ENERGY → HEMPCARBON → SUPERCAPACITOR |
| Microturbine range extender | Experimental and numerical recuperated micro-gas-turbine EV range-extender study validates simulation against testing and models REEV operation | Supported Research / Established for studied architecture | ENERGY → MICROTURBINE → EV |
| Computational geometry | Automotive CFD literature supports parametric geometry, wake control and underbody/aero optimisation; geometry itself remains a design method rather than evidence of performance | Supported Research as method | CG-3D → AERO → DIGITAL TWIN |
| Active cooling apertures / thermal airflow | Automotive aerodynamic and thermal-flow research supports controlled airflow and thermal-management modelling; Biupiu geometry remains unvalidated | Supported Research as engineering method | AERO → THERMAL → CFD |
| Hemp/resin metasurface | Metasurface research exists broadly, but no evidence harvested here establishes the claimed Biupiu vehicle coating performance | Research candidate | MATERIALS → MM → SURFACE |
| Bioblade microturbine blade materials | Microturbine research exists; hemp-composite rotating-blade implementation requires component-level validation | Research candidate | MICROTURBINE → COMPOSITES → ROTOR TEST |

## 1. AeroBrake / active aerodynamic braking

A peer-reviewed study investigated aerodynamic configurations for improving sports-car braking. It examined air-brake placement and small movable aerodynamic elements and reported that the studied configurations could substantially increase drag and reduce lift, with the paper reporting a braking-distance reduction of up to 31% under its tested/modelled conditions.

**Use:** This directly supports keeping Biupiu AeroBrake as an engineering research branch rather than treating it as purely artistic.

**Required Biupiu validation:** CFD → transient deployment → structural load analysis → actuator sizing → brake/aero coordination → closed-loop control → wind-tunnel/road testing.

Source:
https://www.sciencedirect.com/science/article/pii/S0020740319319034

## 2. Active diffuser / underbody

Research has investigated actively translating rear diffusers on passenger cars using CFD with rotating wheels and moving-ground conditions. Separate road-car underbody studies document ground effect, diffuser pumping and downforce behaviour.

**Use:** Biupiu's underbody channels, active diffuser and downforce architecture have established engineering precedents.

Sources:
https://trid.trb.org/View/1825483
https://www.mdpi.com/2076-3417/12/8/3763

## 3. Rear air-jet / active-flow control

A recent DrivAer vehicle study numerically investigated rear slot jets for active aerodynamic control. The reported best multi-jet configuration produced an 11.80% drag reduction in the studied configuration.

**Use:** This is particularly relevant to the historical Biupiu air-flow / air-brake direction. It gives the repository a concrete research pathway for controlled air jets rather than relying only on deployable surfaces.

**Important:** The reported percentage is a result for that study's geometry and conditions, not a Biupiu performance claim.

Source:
https://www.mdpi.com/2076-3417/15/22/12334

## 4. Air-cushion / underbody concept

Published CFD work on air-cushion vehicles studies internal/external flow, lift, drag, pressure, wake structures and air-clearance height. Ground-effect vehicle research likewise investigates air cushions between vehicle and surface and their lift/drag consequences.

**Use:** This establishes real engineering science around air-supported vehicles and ground effect.

**Boundary:** It does not establish that a normal road vehicle can obtain the intended Biupiu low-friction/air-cushion behaviour. That remains an explicit Biupiu research hypothesis.

Sources:
https://www.sciencedirect.com/science/article/pii/S016761051300127X
https://www.sciencedirect.com/science/article/abs/pii/S0029801818316433

## 5. Hemp automotive composites

The evidence is unusually strong for this branch.

- Experimental hemp/glass/epoxy automotive composite work measured tensile, impact, hardness and interfacial behaviour.
- Hemp/carbon/ramie sandwich composites have been studied for automobile door panels.
- Hemp/glass epoxy composites have been simulated for automotive bumper beams, including crashworthiness and pedestrian-impact analysis.
- Hybrid hemp/pineapple/glass laminates have been investigated for lightweight automobile panels.
- A 2026 study tested hemp/coconut epoxy composites with carbon black specifically for automotive applications.

Sources:
https://www.sciencedirect.com/science/article/abs/pii/S2214785320384352
https://www.sciencedirect.com/science/article/pii/S2352492824027983
https://www.sciencedirect.com/science/article/pii/S0263822324001314
https://www.sciencedirect.com/science/article/pii/S0141813025099490
https://www.sciencedirect.com/science/article/pii/S2949822826008154

**Use:** HempCarbon and Biupiu bio-composite body-panel research can therefore be linked to real material test literature instead of being treated as an ungrounded concept.

## 6. HempCarbon energy storage

Hemp-derived activated carbon has been experimentally used for supercapacitor electrodes. Earlier research reported 160 F/g specific capacitance, while later work reported substantially higher values depending on activation/electrolyte conditions. A 2025 ACS study reported 2612 m²/g surface area and 594 F/g maximum specific capacitance for a tested aqueous-electrolyte configuration. A 2026 study using hemp biowaste reported 762 F/g under its optimized electrode/electrolyte conditions and 67% retention after 10,000 cycles.

**Use:** This is direct evidence for maintaining the HempCarbon energy-storage research branch.

Sources:
https://www.sciencedirect.com/science/article/pii/S0008622316301798
https://pubs.acs.org/doi/abs/10.1021/acsomega.4c07518
https://www.sciencedirect.com/science/article/pii/S0961953425013133

**Boundary:** These are electrode/material results, not evidence that a complete automotive supercapacitor pack has been demonstrated by Biupiu.

## 7. Microturbine / EV range extender

A peer-reviewed 2020 study performed both numerical and experimental investigation of a recuperated micro-gas turbine used as an electric-vehicle range extender. It reports a systematic design method, simulation, experimental validation and REEV vehicle modelling. The studied configuration reached a simulated thermal efficiency of about 35% under specified operating assumptions.

The Biupiu repository's PROP-06 architecture is therefore consistent with an existing research pathway: turbine → generator → HV bus → battery → electric propulsion.

Source:
https://www.sciencedirect.com/science/article/pii/S1359431119375854

**Boundary:** Published research validates the studied class of architecture, not Biupiu's proposed BT-70/140/200/300 modules.

## 8. Research priority routing

### Directly evidenced technology families
- AeroBrake / aerodynamic braking
- Active diffuser
- Rear air-jet flow control
- Hemp automotive composites
- Hemp-derived supercapacitor carbon
- Recuperated microturbine EV range extenders

### Adjacent evidence requiring adaptation
- Air-cushion road vehicle
- Ground-effect underbody
- Active cooling apertures
- Hemp-composite rotating turbine blades
- Advanced resin/metasurface vehicle surfaces

### Still Biupiu-specific hypotheses
- Exact AeroBrake geometry
- Biupiu distributed air-brake architecture
- Biupiu air-cushion road-car implementation
- Bioblade blade geometry/material stack
- Biupiu resin metasurface performance
- Exact integrated AeroBlade GT performance

## 9. New experimental queue

1. AeroBrake transient CFD against conventional braking baseline.
2. Active diffuser geometry sweep.
3. Rear air-jet geometry/energy-cost sweep.
4. Combined air-jet + AeroBrake control study.
5. Underbody air-cushion feasibility study with pressure/clearance constraints.
6. Hemp/glass/carbon laminate material matrix.
7. HempCarbon supercapacitor literature-to-cell replication pathway.
8. Microturbine range-extender cycle model using published validation points.
9. Combined vehicle energy-management simulation.
10. Bio-composite rotating blade coupon and subscale rotor test.
11. Thermal-management CFD for turbine + battery + motors.
12. Integrated digital-twin evidence chain.

## Evidence promotion rule

No external paper is treated as proof of a Biupiu invention. External research establishes prior art, physical precedent, test methods, parameter ranges and validation pathways. Biupiu-specific claims remain at their repository evidence state until independently tested.

## Repository cross-links

- `SF-46` — Biupiu AeroBlade GT
- `SF-50` — AeroBlade GT World Showroom
- `PROP-06` — Cross-Discipline Microturbine Track
- `BIUPIU-BIO-COMPOSITE-DIGITAL-TWIN-v1.0`
- `BIUPIU-RESEARCH-INNOVATION-CENTRE-OS-v1.0`
- `RESEARCH-INDEX.md`
- `BIUPIU-GLOBAL-MULTILINGUAL-RESEARCH-INTELLIGENCE-PROTOCOL-v1.0`

**Classification:** Intelligence / Research Harvest / Prior-Art & Engineering Evidence  
**Biupiu claim status:** Concepts remain concept/research unless independently validated.
