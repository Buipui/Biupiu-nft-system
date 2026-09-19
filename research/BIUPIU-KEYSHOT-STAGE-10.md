# Stage 10 — Showcase / Digital Twin Output Bridge

## Purpose
Connect completed KeyShot renders to Biupiu Showcase, Digital Twin and Product Development Showreel records while preserving asset identity and provenance.

## Flow
KeyShot output -> Output Registry -> Showcase Asset -> optional Digital Twin Asset -> optional Showreel Project

## Controls
- Only completed renders can be registered.
- jobId and assetId are mandatory.
- Source-path provenance is mandatory.
- Showcase asset linkage is mandatory.
- Proprietary KeyShot files remain external.

## Acceptance test
A synthetic completed microturbine render record is registered and its original asset/job IDs and Showcase/Digital Twin/Showreel links are preserved.
