# PROP-14 — Experiment-Ready Map Layer v1.0

## Executed
Added a parameterized test-point generator at `simulators/PROP-14-experiment-points-v0_1.py`.

It creates structured screening points across BT-70, BT-140, BT-200 and BT-300; 0/2,000/5,000 m equivalent ambient conditions; pressure ratios 4/5/6; recuperator effectiveness 0.60/0.70/0.80; and module target electrical outputs.

## Purpose
These are data-acquisition points for simulation/test planning, not instructions to build or operate a turbine. Actual hardware limits must come from component ratings, manufacturer limits, laboratory procedures and qualified engineering review.

## Evidence flow
Future measurements should carry operating conditions, sensor/calibration metadata, uncertainty, evidence ID, component configuration and validation status.

## PROP-15
Ingest generated points into a machine-readable dataset, propagate uncertainty, create mission-linked test priorities and connect results to the Blade/microturbine digital twin.

Status: research/test-planning only.
