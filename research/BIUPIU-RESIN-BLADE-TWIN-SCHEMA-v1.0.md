# Biupiu Resin-to-Blade Digital Twin Schema v1.0

**Gate:** BM-03  
**Date:** 18 September 2026  
**Status:** Executable research architecture

## Purpose
Connect resin chemistry and fibre/interface properties directly to laminate, blade and rotor simulations.

## Data chain
`FEEDSTOCK → RESIN → HARDENER → CURE → FIBRE TREATMENT → INTERFACE → LAMINATE → BLADE → ROTOR → SYSTEM`

## Required state variables
- resin viscosity and cure state
- degree of cure
- Tg and temperature-dependent modulus
- fracture toughness
- moisture diffusion and conditioning state
- fibre/matrix interface strength
- fibre volume fraction and orientation
- laminate stacking sequence
- void fraction and manufacturing defects
- blade geometry
- RPM and centrifugal load
- aerodynamic load cases
- thermal/environmental conditions

## Common simulation sweep
Run identical blade geometry and load cases across:
**H01 conventional epoxy; H02 partly bio-epoxy; H03 plant-oil epoxy; H04 lignin-modified epoxy; H05 lignin-derived curing system; F01 bio-epoxy/flax; HF01 bio-epoxy/hemp-flax; HFB01 bio-epoxy/hemp-flax/basalt.**

## Outputs
Mass; tip deflection; strain/stress; first natural frequency; buckling margin; fatigue damage indicator; moisture sensitivity; thermal sensitivity; manufacturing sensitivity; cost and embodied-impact fields.

## Gate rule
A formulation can progress only when its required inputs are measured or explicitly marked as estimated with uncertainty. No missing property may silently become a zero or assumed universal constant.

## Experimental feedback
Coupon → laminate → adhesive joint → component → rotating subassembly → integrated prototype. Each result updates the formulation and material records.

## Safety boundary
This architecture supports research and comparison. It does not certify a blade, aircraft, marine system or turbine for operational use.
