# CannaPiu Structural-Integrity Maths Protocol v1.0

**Status:** REGISTERED / SCREENING PROTOCOL / VALIDATION PENDING

## Core calculations

For each load case, calculate and retain:

- tributary area and distributed loads
- dead, live, wind and rain load combinations
- support reactions and global equilibrium residual
- axial, shear, bending and torsional demand
- elastic deflection and serviceability ratio
- stress utilisation: demand / allowable resistance
- Euler or code-appropriate buckling screening where applicable
- connection demand, anchor uplift, sliding and overturning
- uncertainty bounds from material and load inputs

## Minimum checks

1. Dimensional consistency for every equation.
2. Static equilibrium residual within a declared numerical tolerance.
3. Mesh/step refinement or numerical convergence where applicable.
4. Independent simplified hand-calculation comparison.
5. Sensitivity sweep for wind speed, span, ballast, anchor spacing and material modulus.
6. Worst-case partial-deployment and asymmetric-load cases.
7. Fault injection: missing anchor, sensor failure, incorrect material property, excessive wind and loss of support.
8. No design is promoted on a single nominal result.

## Illustrative screening equations

- Pressure force: `F = p A`
- Bending stress: `sigma = M c / I`
- Axial stress: `sigma = N / A`
- Euler screening: `Pcr = pi^2 E I / (K L)^2`
- Overturning factor: `resisting moment / overturning moment`
- Utilisation: `demand / allowable resistance`

These equations are screening relationships only. Applicable structural standards, load combinations, material anisotropy, connection behaviour, membrane mechanics and professional engineering review are required for a deployable structure.

## Promotion gates

- **G0:** input provenance and units verified
- **G1:** geometry/topology validated
- **G2:** material test evidence attached
- **G3:** load cases and combinations reviewed
- **G4:** numerical convergence and independent check passed
- **G5:** connection/anchor and failure-mode review passed
- **G6:** physical prototype test correlated
- **G7:** qualified structural sign-off and jurisdictional compliance

**Current state:** G0-G1 are specification targets; G2-G7 pending evidence.
