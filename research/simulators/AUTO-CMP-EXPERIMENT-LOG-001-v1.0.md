# Biupiu Simulator Experiment Log 001 — Bio-Composite Vehicle Panels

**Date:** 20 September 2026  
**Experiment ID:** `BPU-EXP-AUTO-CMP-001`  
**Status:** Planned / not yet executed in a runtime

## Objective

Assess the structural-integrity screening workflow for flax, hemp and hybrid bio-composite panels while retaining conventional vehicle running gear in the physical demonstrator.

## Material cases

- M1: flax / bio-epoxy baseline
- M2: hemp / bio-epoxy baseline
- M3: flax-hemp hybrid / bio-epoxy
- M4: flax / furan or PFA system
- M5: flax or hemp / EVO-derived epoxy
- C1: glass-fibre epoxy control
- C2: carbon-fibre epoxy control

Exact properties are to be entered from measured coupon data or traceable literature. No placeholder values may be presented as certified properties.

## Input fields

- Fibre type, batch and treatment
- Fabric architecture and areal weight
- Fibre volume fraction and void fraction
- Resin formulation, cure schedule and post-cure
- Lamina E1, E2, G12, nu12 and strengths
- Panel thickness, stacking sequence and boundary conditions
- Temperature, relative humidity and conditioning time
- Fastener, insert, adhesive and edge details

## Planned simulator runs

| Run | Purpose | Output | Closure condition |
|---|---|---|---|
| R001 | CLT baseline | A/B/D matrices | Benchmark against analytical reference |
| R002 | Orientation sweep | Stiffness versus layup | Unit and symmetry checks |
| R003 | Moisture sensitivity | Property reduction envelope | Input source and model assumptions logged |
| R004 | Thermal mismatch | Thermal strain/stress screen | Temperature range and CTE evidence |
| R005 | Damping sensitivity | Frequency/temperature parameter sweep | Experimental damping data required for calibration |
| R006 | Damage screen | Failure indices and delamination flags | Validated strengths and fracture data required |
| R007 | Panel attachment | Local stress and fastener/adhesive sensitivity | Subcomponent test plan approved |
| R008 | Monte Carlo | Uncertainty and sensitivity ranking | Distribution provenance documented |

## Acceptance rules

- All units SI; no hidden unit conversions.
- Every input has provenance and evidence classification.
- Outputs are labelled screening, not certification.
- No fatigue life is claimed without measured S-N or equivalent data.
- No crashworthiness claim is made from static CLT alone.
- Model calibration is separated from validation data.

## Physical correlation plan

1. Produce flat coupons from each material case.
2. Record mass, thickness, fibre volume fraction and void content.
3. Conduct tensile, flexural, interlaminar, impact and moisture-conditioning tests.
4. Record failure modes using microscopy/SEM, CT or acoustic emission where available.
5. Compare measured stiffness, strength, damping and failure location against model predictions.
6. Update the material card with revision, uncertainty and calibration status.

## Current result

No numerical run was executed in this log. This record defines the reproducible experiment plan and prevents unverified simulator output from being treated as physical evidence.
