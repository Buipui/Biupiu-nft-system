# Biupiu Simulator Experiment Log 001 — Bio-Composite Vehicle Panels

**Date:** 20 September 2026  
**Experiment ID:** BPU-EXP-AUTO-CMP-001  
**Status:** Screening regression executed / material correlation pending

## Objective

Assess the structural-integrity screening workflow for flax, hemp and hybrid bio-composite panels while retaining conventional vehicle running gear in the physical demonstrator.

## Executed software regression

| Check | Result |
|---|---|
| Reduced stiffness symmetry / positive diagonal | PASS |
| 0° transformed-Q identity | PASS |
| 90° transformed-Q axis swap | PASS |
| Symmetric layup B-matrix near zero | PASS |
| ABD thickness scaling | PASS |
| Cure increment bounded / monotonic | PASS |

**Runtime result:** 6/6 checks passed.

**Numerical check:** symmetric-layup maximum absolute B-matrix term = 2.22e-16.

These are mathematical/software regression checks only. They do not establish material properties, fatigue life, crashworthiness, or roadworthiness.

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
- Conventional/OEM-qualified running gear remains the default for the first physical vehicle demonstrators.

## Physical correlation plan

1. Produce flat coupons from each material case.
2. Record mass, thickness, fibre volume fraction and void content.
3. Conduct tensile, flexural, interlaminar, impact and moisture-conditioning tests.
4. Record failure modes using microscopy/SEM, CT or acoustic emission where available.
5. Compare measured stiffness, strength, damping and failure location against model predictions.
6. Update the material card with revision, uncertainty and calibration status.

## Current result

Software regression completed successfully. Physical material correlation and full simulator runs remain pending.
