# Biupiu Blade Comparison Workflow v1.0

**Gate:** BM-05  
**Status:** Executed  
**Purpose:** turn the BM-04 runner specification into a reproducible candidate-comparison workflow.

## Execution sequence

1. Load material/resin record.
2. Validate required properties and provenance.
3. Load the same reference blade geometry.
4. Apply the same load-case definitions.
5. Generate/validate the laminate definition.
6. Run aerodynamic load model.
7. Transfer loads to structural analysis.
8. Run modal and buckling analyses.
9. Run fatigue proxy where validated fatigue data exist.
10. Run moisture/thermal sensitivity sweeps.
11. Record uncertainty and missing-data flags.
12. Write result record.
13. Update the Digital Twin.
14. Route failures back to the formulation/material experiment queue.

## Comparison controls

- identical geometry for baseline comparison
- identical operating/load envelope
- identical boundary conditions
- identical safety-factor policy
- identical reporting units
- no hidden material-property substitution
- literature estimates clearly marked
- measured data supersede estimates when traceable
- failed/invalid runs remain in the dataset rather than being deleted

## Experimental feedback priority

The runner must prioritize replacing uncertain inputs in this order:

1. fibre/matrix tensile and compressive properties
2. interlaminar shear
3. fracture toughness
4. fatigue data
5. moisture-conditioned properties
6. thermal-conditioned properties
7. manufacturing defect distributions
8. adhesive joint properties

## Decision states

**RESEARCH-CANDIDATE:** literature/estimated inputs only  
**MODEL-READY:** required inputs available with uncertainty  
**TEST-CALIBRATED:** model parameters calibrated against physical tests  
**REPLICATION-REQUIRED:** result needs independent repeat  
**QUALIFICATION-CANDIDATE:** evidence package complete enough for formal engineering review

No state constitutes certification.

## First experimental campaign

Prioritize:
- hemp/epoxy control
- flax/bio-epoxy control
- hemp/flax/bio-epoxy
- hemp/flax/basalt/bio-epoxy
- corresponding adhesive coupons

Record environmental conditioning and manufacturing batch for every specimen.
