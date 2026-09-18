# Biupiu Material Calibration Loop v1.0

**Gate:** BM-06  
**Status:** Executed  
**Purpose:** establish the controlled pathway from physical tests to calibrated material models.

## Calibration chain

TEST SPECIMEN → RAW DATA → QC → REDUCTION → UNCERTAINTY → MATERIAL RECORD → DIGITAL TWIN → MODEL RUN → PREDICTION/TEST ERROR → CALIBRATION UPDATE

## Rules

1. Raw measurements remain immutable references.
2. Processed values retain calculation method and uncertainty.
3. Every specimen links to material batch and manufacturing route.
4. Conditioning state is mandatory for environmental tests.
5. Literature values are never silently overwritten.
6. A measured property supersedes an estimate only when traceability criteria are met.
7. Failed specimens remain in the record and receive a failure-mode classification.
8. Calibration changes require model-version increment.
9. Independent validation data must remain separate from calibration data.
10. Any extrapolation outside tested temperature, moisture, loading or frequency ranges is flagged.

## Minimum calibration targets

**Material:** density, E1/E2, G12, strengths, fracture toughness, fatigue.  
**Resin:** viscosity, cure, Tg, modulus, fracture toughness, moisture.  
**Adhesive:** lap shear, peel, mode-I/II fracture, fatigue, environmental ageing.  
**Laminate:** tensile/compression, flexure, ILSS, impact, fatigue.  
**Blade component:** deflection, strain, vibration/modal response and failure mode.

## Uncertainty model

Every calibrated parameter carries:
- measured value
- uncertainty
- sample count
- conditioning
- test method
- batch
- confidence/coverage statement
- calibration model version

The system must preserve distributions or intervals where data justify them rather than reducing everything to a single nominal value.

## Digital Twin update

Only traceable calibrated parameters enter the production research twin. Experimental data remain separated from simulation predictions so model validation is not circular.

## Gate exit

BM-06 exits when:
- at least one material has traceable coupon data
- at least one resin/adhesive formulation has traceable cure/mechanical data
- one laminate model is calibrated
- an independent validation set is retained
- discrepancy/error is documented
- model version is frozen for the validation run

No certification is implied.
