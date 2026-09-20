# CannaPiu Outdoor Tent Digital-Twin Simulator Specification v1.0

**Status:** REGISTERED / PROTOTYPE SPECIFICATION / EXECUTION PENDING

## Purpose

Simulate modular outdoor tent and awning systems for CannaPiu franchise deployments before physical manufacture. The simulator must support parameter changes, environmental load cases, material alternatives, failure modes and evidence tracking.

## Inputs

- span, bay length, height and roof geometry
- pole/truss/beam cross-sections
- membrane and panel mass per area
- anchor locations and ballast mass
- wind speed, direction and exposure category
- rain ponding assumptions
- occupant/equipment loads
- material density, elastic modulus, yield/ultimate strengths
- connection stiffness and allowable movement
- safety factors and uncertainty bounds

## Outputs

- total mass and centre of gravity
- reaction forces and member forces
- deflection and drift
- stress/strain utilisation ratios
- buckling screening
- anchor uplift/sliding/overturning demand
- membrane tension estimates
- sensitivity and uncertainty results
- failure-mode flags
- design evidence record

## Required modes

1. Baseline conventional structure
2. Hemp-canvas membrane configuration
3. Lightweight composite membrane/panel configuration
4. Hybrid canvas-composite configuration
5. Awning cantilever configuration
6. High-wind and partial-deployment cases
7. Sensor fault and weather-alert cases
8. Assembly error and missing-anchor cases

## Safety boundary

This simulator is for concept screening and prototype development. It is not a substitute for structural engineering calculations, local code compliance, wind-tunnel/field testing, fire testing, anchoring certification or professional sign-off.

## Gate

REGISTERED: simulator requirements  
PENDING: computational implementation  
PENDING: validated material data  
PENDING: independent structural review  
PENDING: physical prototype correlation
