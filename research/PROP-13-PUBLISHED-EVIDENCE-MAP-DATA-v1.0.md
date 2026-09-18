# PROP-13 — Published Evidence & Map-Ready Dataset Layer v1.0

## Executed
Added a map/evidence interface separating published reference evidence from Biupiu measurements.

### Research integration
ResearchGate evidence shows modern micro-gas-turbine modelling uses compressor/turbine performance maps and interpolation for off-design operation. A 2026 experimental 10 kWe study describes normalized compressor and turbine maps and cubic interpolation, with experimentally calibrated recuperator dynamics. citeturn0search2

Research on recuperators consistently identifies the trade-off between heat-exchanger effectiveness and pressure loss as a core cycle-design constraint. citeturn0search0turn0search10

A range-extender study demonstrates map-based compressor/turbine operating-envelope analysis and identifies pressure-ratio/turbine choking constraints. citeturn0search5

### Repository rule
Published data is labelled `reference`; it is never represented as Biupiu test data.

### Uncertainty
The interface supports nominal/low/high bands so future Biupiu results can carry measurement uncertainty instead of false precision.

## PROP-14
Populate legally usable numeric map datasets, add interpolation, connect map validity to mission phases, model recuperator heat-transfer/pressure-loss coupling, propagate uncertainty through the digital twin, and generate experiment-ready test points.

Status: research/simulation only.