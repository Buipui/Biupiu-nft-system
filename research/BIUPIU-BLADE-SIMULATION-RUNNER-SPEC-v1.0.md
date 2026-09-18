# Biupiu Blade Simulation Runner Specification v1.0

**Gate:** BM-04  
**Status:** Executed research architecture  
**Date:** 18 September 2026

## Purpose
Define a reproducible runner that evaluates every material/resin formulation against identical blade geometry, environmental conditions and load cases.

## Pipeline
MATERIAL/RESIN JSON → MATERIAL VALIDATION → GEOMETRY → AERODYNAMIC MODEL → LOAD CASES → STRUCTURAL FEA → MODAL/BUCKLING → FATIGUE PROXY → ENVIRONMENTAL SENSITIVITY → RESULTS → DIGITAL TWIN

## Required inputs
- blade geometry/version
- rotor diameter and RPM range
- air/fluid properties
- operating envelope
- aerodynamic load model
- material formulation ID
- laminate stacking sequence
- fibre orientation/volume fraction
- resin state and uncertainty
- manufacturing defect assumptions
- safety factors
- environmental conditioning

## Required outputs
- mass
- thrust/torque fields where modelled
- tip deflection
- maximum stress/strain
- first natural frequency
- buckling margin
- fatigue damage indicator
- moisture/thermal sensitivity
- manufacturing sensitivity
- uncertainty interval
- provenance and simulation version

## Candidate sweep
H01 conventional epoxy/hemp  
H02 partly bio-epoxy/hemp  
H03 plant-oil epoxy/hemp  
H04 lignin-modified epoxy/hemp  
H05 lignin-derived curing system/hemp  
F01 bio-epoxy/flax  
HF01 bio-epoxy/hemp-flax  
HFB01 bio-epoxy/hemp-flax/basalt

## Reproducibility rule
A result is valid only if geometry, mesh/model version, load cases, material record, boundary conditions and solver settings are recorded. Results using estimated properties must be marked accordingly.

## Safety rule
The runner is for engineering research and comparative modelling. It does not certify a rotor, aircraft, marine craft or vehicle component.
