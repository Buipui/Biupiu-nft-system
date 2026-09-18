# EXP-001 — Structured-Light Link Under Atmospheric Turbulence

**Status:** Protocol prepared; execution pending a numerical simulation environment.
**Date:** 2026-09-18
**Claim under test:** Structured light (for example, orbital-angular-momentum modes) can preserve useful information transfer through modeled atmospheric turbulence better than a conventional single-mode baseline under some conditions.

## Hypothesis
H1: At selected turbulence strengths and receiver conditions, a structured-light link has higher measured mode/data recovery than the baseline.
H0: It does not outperform the baseline under the same conditions.

## Required model
- Optical wavelength and aperture sizes
- Propagation distance
- Turbulence strength (e.g., refractive-index structure parameter or equivalent phase-screen parameter)
- Transmit mode set and receiver mode sorter/detector model
- Noise, pointing error, and alignment assumptions

## Baselines
1. Conventional single-mode optical link.
2. Structured-light link with identical optical power, aperture, distance, detector noise, and coding assumptions.

## Metrics
- Symbol or bit error rate
- Mode cross-talk matrix
- Received power / signal-to-noise ratio
- Effective throughput after error correction
- Sensitivity to turbulence and pointing error

## Decision rule
A claim of conditional support requires a statistically meaningful improvement across predefined parameter sweeps and robustness to reasonable changes in assumptions. A failure to outperform is recorded as a result for the tested model, not a universal disproof.

## Current result
**INCONCLUSIVE / NOT EXECUTED.** No numerical output has been generated in this repository execution. The protocol is logged to prevent presenting an unrun simulation as evidence.

## Next execution gate
Implement a reproducible Python or MATLAB-compatible phase-screen simulation, add a conventional baseline, run parameter sweeps, export raw metrics and plots, and independently review the assumptions.
