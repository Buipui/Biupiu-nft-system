# Biupiu Redshift Deterministic Test Scene — RED-03

**Status:** TEST SPECIFICATION IMPLEMENTED — LIVE RENDER REMAINS GATED  
**Date:** 18 September 2026

## Purpose

Provide a renderer-neutral, repeatable scene definition for validating the Redshift adapter without embedding Redshift binaries, proprietary SDKs or licensed project assets.

## Scene identity

- Scene ID: `BIUPIU-RED-TEST-001`
- Geometry: one unit-scale reference object plus three primitive calibration objects
- Camera: fixed transform; no adaptive framing
- Lighting: fixed key/fill/rim arrangement
- Background: neutral, constant environment
- Resolution: 1024 × 1024 for baseline validation
- Frame: 0001 for still validation
- Animation: frames 0001–0010 for sequence validation
- Sampling: fixed values recorded in the render manifest
- Color management: renderer/host configuration must be recorded, never inferred

## Material lanes

1. **Composite appearance** — fibre-like directional pattern and controlled roughness.
2. **Coated metal** — metallic response and clear-coat appearance.
3. **Optical/glass** — transmission/refraction response.
4. **Carbon-fibre-like weave** — visual weave only; not a material-property claim.
5. **Bio-resin appearance** — controlled roughness/transmission variant; not a measured chemistry claim.

The material lanes are visualisation tests only. They do not establish mechanical, optical or chemical properties.

## OSL validation set

Use the repository-indexed official Redshift-compatible examples as references:

- `SpaceTransform.osl`
- `UberConstant.osl`
- `ColorShuffle.osl`
- `TextureNoTile.osl`
- `ThinFilmInterference.osl`

Each shader must have its source URL, commit/version and licence state recorded before inclusion in a distributable asset package.

## Determinism requirements

A validation record must capture:

- host and host version;
- Redshift version;
- device model, VRAM and driver/runtime;
- scene specification version;
- render settings;
- source asset IDs;
- source model version;
- shader source identifiers;
- output format;
- output SHA-256;
- execution timestamp;
- pass/fail/block state.

A repeated run with unchanged inputs should be compared by output hash or an explicitly documented deterministic tolerance policy.

## Acceptance

RED-03 is complete when:

1. the scene is reproduced on a connected Redshift-capable environment;
2. the OSL validation set loads successfully;
3. still and sequence renders complete;
4. output hashes are recorded;
5. provenance survives from source asset to render output;
6. any non-determinism or environment-specific difference is logged rather than hidden.

## Current state

**BLOCKED ON LIVE REDSHIFT ENVIRONMENT.** The repository now contains the adapter contract and deterministic scene specification, but no live Redshift installation or render node has been verified.
