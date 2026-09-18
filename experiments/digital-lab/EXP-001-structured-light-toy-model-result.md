# EXP-001 — Structured-Light Communications Toy Model

**Date:** 2026-09-18  
**Status:** Executed as a deliberately simplified mathematical model; not physical validation.

## Claim under test
Structured-light transmission may outperform a conventional optical baseline under atmospheric turbulence.

## Model
A turbulence proxy `sigma` is varied from 0.0 to 0.4. Cross-talk is defined as `min(0.95, 2.5*sigma^2)`. The two BER proxies are illustrative equations, not measured or literature-calibrated optical results:

- Conventional proxy: `0.001 + 0.12*cross_talk`
- Structured-light proxy: `0.002 + 0.20*cross_talk + 0.03*sigma`

## Results

| sigma | cross-talk | conventional BER proxy | structured BER proxy |
|---:|---:|---:|---:|
| 0.0 | 0.0000 | 0.00100 | 0.00200 |
| 0.1 | 0.0250 | 0.00400 | 0.01000 |
| 0.2 | 0.1000 | 0.01300 | 0.02800 |
| 0.3 | 0.2250 | 0.02800 | 0.05600 |
| 0.4 | 0.4000 | 0.04900 | 0.09400 |

## Interpretation
Within this toy model, the structured-light proxy has higher BER at every tested turbulence value. Therefore, the claim is **refuted under this specific toy model**, but this does not disprove structured light generally. The result primarily demonstrates that the chosen equations favor the conventional baseline and are not sufficient for an engineering conclusion.

## Limitations
- No wave-optics propagation, phase screens, receiver model, coding, aperture, wavelength, or measured channel data.
- No calibration against Wits or peer-reviewed experimental data.
- No statistical confidence interval or independent replication.

## Next validation gate
Replace the toy equations with a split-step Fourier propagation model, compare equal-power/equal-bandwidth links, include mode detection and error correction, and validate against published experimental benchmarks before making any performance claim.
