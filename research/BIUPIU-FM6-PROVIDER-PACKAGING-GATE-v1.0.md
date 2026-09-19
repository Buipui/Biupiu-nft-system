# Biupiu FM6 Provider Packaging Gate v1.0

**Gate:** FM6-04  
**Status:** EXECUTED — environment-gated provider package planning

## Objective
Create renderer-specific package plans from authoritative Biupiu Digital Twin lineage without executing proprietary Forza extraction or assuming local renderer availability.

## Flow
Universal Asset Manifest → Digital Twin Binding → FM6 Reference Preset → Provider Package Plan → Environment Execution → Cross-Renderer Validation

## Supported targets
Unreal Engine 5, Blender, Redshift, V-Ray, Octane, Lumion and KeyShot.

## Controls
- Only CLEARED assets can enter a package plan.
- FM6 remains REFERENCE-ONLY.
- Source asset, version, Digital Twin ID and preset are mandatory.
- The package planner does not copy or extract Forza assets.
- Renderer execution is explicitly marked NOT_EXECUTED until the relevant software environment is available.
- Cross-renderer comparisons must use original Biupiu assets and record renderer/version and output provenance.

## Acceptance
Automated tests verify provenance gating, licence gating and FM6 boundary enforcement.
