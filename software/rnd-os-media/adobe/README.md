# Biupiu Adobe Media Adapter Layer v0.2

This package defines the boundary between the Biupiu R&D OS and Adobe Creative Cloud media applications.

## Architecture

The R&D OS remains authoritative for projects, research objects, provenance, evidence, IP state and audit events. Adobe applications execute application-specific media operations through adapters.

### Adapters

- `premiere-pro/` — Premiere Pro UXP job contract and integration notes.
- `after-effects/` — After Effects composition/render adapter contract.
- `MEDIA-JOB-SCHEMA.json` — portable job/provenance envelope.
- `ADOBE-RDOS-EVENT-BRIDGE-v0.1.json` — event contract connecting media jobs to the R&D OS lifecycle.
- `../../research/BIUPIU-ADOBE-INTEGRATION-GATE-04-v1.0.md` — current verification matrix and runtime evidence boundary.

## Gate status

- ADOBE-01: architecture/provenance layer — closed
- ADOBE-02: deterministic media-job validation architecture — closed
- ADOBE-03: R&D OS event bridge/schema contract — closed
- ADOBE-04: repository-side cross-application integration matrix — verified
- Firefly live-generation milestone — previously verified and recorded
- Premiere Pro live execution — **pending workstation verification**
- After Effects live execution — **pending workstation verification**
- UE5 → Adobe cinematic finishing E2E — **pending workstation verification**

The repository deliberately does not claim desktop execution until the installed Adobe applications pass the local import/render/export/hash/provenance tests.

No Adobe executable, proprietary SDK binary or unlicensed third-party asset is bundled here.
