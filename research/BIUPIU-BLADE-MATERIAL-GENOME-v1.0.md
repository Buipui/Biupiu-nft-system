# Biupiu Blade Material Genome v1.0

**Date:** 18 September 2026  
**Status:** Executable research/qualification gate  
**Scope:** Hemp, flax, hemp/flax, hemp/flax/basalt and secondary plant composites for Biupiu micro-turbines

## Evidence update

ResearchGate evidence confirms several important constraints and opportunities:

- A 2024 structural/environmental assessment found flax and hemp promising for wind-turbine blades when restricted to stiffness-driven biaxial plies; its optimised hemp case reported 8.9% lower blade mass and 13.2% lower total blade-material GWP versus its baseline scenario. These values are study-specific and are not transferable automatically to Biupiu blades. citeturn0search2
- A full-scale 3.5 m, 11 kW small-turbine case study reported a flax/polyester blade 10% lighter than the corresponding E-glass blade. citeturn0search10
- Fatigue research on small-scale natural-fibre turbine blades demonstrates why S-N data and fatigue-specific testing must be part of the qualification gate. citeturn0search7
- Hemp wind-blade composite experiments found a 30% fibre-weight specimen promising, while also reporting moisture and strength limitations and recommending treatment, improved resin systems and full-scale structural analysis. citeturn0search0
- Hybridisation is strongly relevant: flax/basalt research reports improved mechanical behaviour depending on stacking sequence, and 2026 work is explicitly investigating AI-assisted optimisation of flax/basalt laminates. citeturn0search8turn0search11
- A 2026 flax/basalt study reports basalt-rich laminates reaching about 155 MPa tensile strength in its tested configurations and better impact energy absorption for an alternating hybrid; these are coupon-study results, not blade design allowables. citeturn0search1

## Genome record schema

`MATERIAL-ID | FIBRE | MATRIX | TREATMENT | Vf/Wt% | ORIENTATION | STACK | DENSITY | E1/E2 | G12 | XT/XC | YT/YC | SHEAR | FATIGUE | MOISTURE | THERMAL | IMPACT | MANUFACTURING | SOURCE | EVIDENCE | TEST STATUS`

## Initial qualification matrix

| ID | Material candidate | Intended role | Required tests |
|---|---|---|---|
| BMG-H01 | Hemp/epoxy | baseline structural laminate | tensile, compression, flexural, ILSS, fatigue, moisture |
| BMG-F01 | Flax/epoxy | baseline structural laminate | same |
| BMG-HF01 | Hemp/flax/epoxy | hybrid structural laminate | same + dynamic/modal |
| BMG-HFB01 | Hemp/flax/basalt/epoxy | high-load hybrid | same + impact + buckling |
| BMG-B01 | Bamboo/epoxy | secondary structure | tensile, flexural, moisture |
| BMG-KJ01 | Kenaf/jute/epoxy | low-cost comparison | tensile, flexural, moisture |
| BMG-HF-BIO01 | Hemp/flax/bio-based matrix | renewable-matrix track | mechanical + thermal + moisture + ageing |

## Do not invent missing material data

Literature values are stored as **source observations**, not universal material constants. Each value must retain fibre volume fraction, matrix, manufacturing route, conditioning, test standard and source.

The digital twin may use literature values for early sensitivity studies, but any design release must replace them with Biupiu-tested allowables and uncertainty bounds.

## Blade simulation parameter set

For every candidate the twin should sweep:

- fibre volume fraction
- fibre orientation
- laminate stacking sequence
- shell thickness
- spar/shear-web configuration
- core density
- resin properties
- rotor RPM
- aerodynamic load envelope
- centrifugal load
- temperature
- humidity/moisture state
- manufacturing void fraction
- fibre misalignment
- mass balance
- fatigue degradation

## First optimisation experiment

Run four baseline material families through the same geometry and load cases:

**H01 → F01 → HF01 → HFB01**

Compare:

1. mass
2. tip deflection
3. first natural frequency
4. buckling margin
5. maximum strain/stress
6. fatigue damage proxy
7. impact sensitivity
8. moisture sensitivity
9. manufacturing complexity
10. material cost
11. embodied-impact metric

No candidate receives a 'winner' label until the same geometry, load cases, safety factors and test assumptions are applied.

## Digital-twin handoff

`Material Genome → CAD → BEM/CFD → aeroelastic loads → FEA → modal/buckling → fatigue → manufacturing model → sensor model → physical test → parameter update`

## Gate status

**GATE BM-01: OPEN**

Entry criteria:
- candidate materials defined
- source evidence captured
- simulation variables defined
- physical qualification plan defined

Exit criteria:
- coupon data acquired
- model calibration completed
- uncertainty bounds recorded
- rotating-blade subcomponent tested
- results replicated before production claims

## Research provenance

ResearchGate sources currently indexed:
RG-WTB-2024-HF: natural-fibre wind-turbine structural/environmental assessment.  
RG-FLAX-2013: small wind-turbine flax/E-glass blade case study.  
RG-FATIGUE-2012: natural-fibre fatigue characterisation for small turbine blades.  
RG-HEMP-2023: upcycled natural-fibre wind-blade composite experiment.  
RG-HYBRID-2013: basalt/flax/hemp hybrid laminate characterisation.  
RG-HYBRID-2026: flax/basalt mechanical and thermal study.  
RG-AI-HYBRID-2026: AI-assisted flax/basalt optimisation.

Emerald Insight remains a complementary source layer for natural-fibre processing, sustainability and implementation research; no Emerald result is being converted into a quantitative blade property unless its exact test conditions are captured.

## Next executable stage

Create the **Blade Digital Twin parameter schema and simulation runner** so every material candidate can be instantiated against a common blade geometry and common load-case definition without hard-coding unsupported material properties.
