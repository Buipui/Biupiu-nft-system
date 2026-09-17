# Episode 01 — Digital Workshop Video Test Matrix v1.0

**Episode:** BIU-VID-S1-E01 — From Video Claim to Engineering Test  
**Status:** READY FOR VIRTUAL TESTING  
**Date:** 17 September 2026

## Objective

Use the original Biupiu video as the first demonstration of the Digital Workshop: take a claim or design shown in a source video, convert it into measurable variables, run controlled virtual tests, record uncertainty and define the physical experiment required for validation.

## Test sequence

### DW-E01-001 — Claim decomposition
- Input: selected source-video claim/design.
- Output: engineering question, measurable variables and falsification condition.
- Pass condition: every important claim has a measurable or explicitly non-testable component.

### DW-E01-002 — Baseline digital model
- Input: simplified geometry/model and stated assumptions.
- Output: reproducible baseline simulation.
- Log: geometry version, parameters, solver/tool, boundary conditions and seed where relevant.

### DW-E01-003 — Parameter sweep
- Vary the principal design variables over a defined range.
- Record response curves, failure regions and sensitivity.
- Do not optimise against a single attractive output.

### DW-E01-004 — Video-to-model comparison
- Compare the source-video claim with the virtual model.
- Classify the relationship as consistent, inconsistent, underdetermined or not testable from available information.
- Do not treat visual similarity as validation.

### DW-E01-005 — AI visualisation integrity check
- Generate an original AI visualisation of the proposed test.
- Label it **AI CONCEPT** or **SIMULATION**.
- Confirm that no generated scene is presented as physical footage.

### DW-E01-006 — Physical-test handoff
- Define the instruments, measurements, calibration, safety controls and raw-data format required to test the leading virtual hypothesis physically.
- Disposition: PROTOTYPE QUEUE / MODIFY / DEFER / FALSIFY.

## Video production sequence

1. Introduce the source claim without endorsing it.
2. Show claim decomposition.
3. Show the Biupiu evidence ladder.
4. Enter the Digital Workshop.
5. Display model assumptions and parameters.
6. Run the virtual test and sensitivity sweep.
7. Show what the model can and cannot establish.
8. Show the AI-generated concept visual with status label.
9. Define the physical experiment needed next.
10. Archive the test record in the repository.

## Required evidence labels

`REFERENCE VIDEO` → `AI CONCEPT` → `SIMULATION` → `DIGITAL WORKSHOP TEST` → `PHYSICAL TEST` → `CALIBRATED MODEL / DIGITAL TWIN`

The final two labels require physical evidence; virtual output alone cannot advance to them.

## Release status

This matrix authorises virtual-workshop preparation only. It does not record a physical test, validated performance result, product certification or commercial claim.
