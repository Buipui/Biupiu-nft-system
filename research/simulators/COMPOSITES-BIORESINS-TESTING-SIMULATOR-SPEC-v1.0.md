# Biupiu Composite Materials & Bio-Resins Testing Simulator Specification v1.0

**Date:** 20 September 2026  
**Status:** Architecture and validation specification; not a certified engineering solver

## Purpose

Create two linked but separable computational laboratories:

1. **BPU-SIM-CMP-01 — Composite Materials Test Simulator**
2. **BPU-SIM-RES-01 — Bio-Resin Chemistry / Cure / Property Simulator**

The simulators are intended for screening, parameter studies, uncertainty analysis, experimental planning and digital-twin preparation. They must not be used as the sole basis for safety-critical structural certification.

## Solver architecture

- SI units throughout; explicit unit validation.
- Deterministic baseline mode plus Monte Carlo uncertainty mode.
- Material cards with provenance, evidence classification and versioning.
- Analytical models first; numerical FEM/FEA and CFD integrations later.
- Every result includes assumptions, boundary conditions, mesh/time-step information where relevant, convergence status and uncertainty bounds.
- Conventional controls are mandatory: glass/epoxy, carbon/epoxy, petroleum epoxy and untreated-fibre baselines where applicable.

## Composite simulator modules

### CMP-01 Lamina mechanics
- Rule of mixtures for longitudinal modulus and strength as a first estimate.
- Inverse rule of mixtures for transverse properties.
- Halpin–Tsai comparison model.
- Classical Lamination Theory (CLT) for laminate A/B/D matrices.
- Fibre orientation, stacking sequence, fibre volume fraction, void content and waviness as variables.
- Hygro-expansion and temperature-dependent property modifiers.

### CMP-02 Failure and durability screening
- Maximum stress, maximum strain and Tsai–Hill/Tsai–Wu options where input data support them.
- Interlaminar shear and delamination screening.
- Moisture diffusion using Fickian first-order model.
- Thermal expansion and cure-shrinkage mismatch.
- Fatigue S–N curve fitting from measured data only; no invented curves.
- Impact and buckling as later numerical modules.

### CMP-03 Manufacturing model
- Resin content and fibre-volume-fraction estimator.
- Void fraction sensitivity.
- Consolidation-pressure and cure-cycle record.
- Prepreg out-time and storage metadata.
- Process comparison: vacuum bag, compression moulding, infusion and hot-melt prepreg.

## Bio-resin simulator modules

### RES-01 Formulation card
- Resin family: PFA/furan, EVO-derived epoxy, bio-epoxy, bio-polyester and control epoxy.
- Oil feedstock, oxirane content, functionality, hardener, catalyst, diluent, additives and bio-based carbon fraction.
- Viscosity, density, pot life, gel time, cure temperature and post-cure.

### RES-02 Cure kinetics
- Initial model: phenomenological nth-order/autocatalytic cure kinetics.
- Required inputs: DSC-derived conversion/temperature data, kinetic constants, activation energy, reaction order and heat of reaction.
- Outputs: conversion versus time/temperature, estimated gel point, exotherm risk flag and cure-cycle comparison.
- Calibration must use experimental DSC/DEA data; literature constants are labelled provisional.

### RES-03 Thermomechanical and ageing screening
- Tg estimation only when supported by measured or validated correlation data.
- DMA curve ingestion and storage modulus/loss factor plotting.
- Water uptake and diffusion comparison.
- UV, humidity, thermal cycling and chemical ageing test planning.
- Fire screening data fields for LOI, UL-94 or cone calorimetry; do not infer certification from a model.

## Coupled simulation workflow

`Material card → formulation → processing cycle → lamina properties → laminate CLT → moisture/thermal modifiers → failure screen → uncertainty sweep → experimental test plan → measured data ingestion → model calibration → revisioned digital twin`

## Required outputs

- Stress–strain and load–displacement plots.
- Laminate stiffness matrices and engineering constants.
- Failure index maps/tables.
- Cure conversion and temperature curves.
- Moisture uptake versus time.
- Sensitivity ranking for fibre volume, orientation, resin content, voids, moisture and cure conditions.
- Comparison against conventional controls.
- Test matrix with specimen ID, method, replicate count, conditioning and acceptance criteria.
- Machine-readable JSON export plus human-readable Markdown report.

## Validation gates

- **Gate 0:** schema and unit validation.
- **Gate 1:** analytical benchmark cases against hand calculations.
- **Gate 2:** sensitivity and uncertainty tests.
- **Gate 3:** comparison against published experimental datasets.
- **Gate 4:** calibration against Biupiu laboratory results.
- **Gate 5:** independent technical review and version lock.

## Research integrity constraints

Natural fibres are variable and moisture-sensitive. Furan/PFA systems may offer renewable feedstock and useful fire behaviour but require scrutiny of water uptake, acidic degradation products, shrinkage and interface durability. EVO-derived epoxies are often only partly bio-based because hardeners and modifiers may be fossil-derived. The simulator must preserve these limitations and must never convert estimates into certified properties.

## Initial material families

- Flax / low-temperature epoxy.
- Flax / bio-epoxy.
- Flax / PFA-furan.
- Hemp / bio-epoxy.
- Hemp / EVO-epoxy.
- Flax–hemp hybrid / bio-epoxy.
- Flax–hemp hybrid / PFA-furan.
- Basalt hybrid controls.
- Glass/epoxy and carbon/epoxy controls.

## Implementation recommendation

Prototype the analytical layer in Python using NumPy/SciPy/Pandas and Matplotlib, with optional JAX for differentiable parameter sweeps. Use an open-source FEM backend such as CalculiX, Code_Aster or FEniCSx only after the analytical benchmark suite passes. Keep the chemistry model modular so experimental kinetic data can replace provisional equations.
