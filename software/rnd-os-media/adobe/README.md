# Biupiu Adobe Media Adapter Layer v0.2

This package defines the boundary between the Biupiu R&D OS and Adobe Creative Cloud media applications.

## Architecture

The R&D OS remains authoritative for projects, research objects, provenance, evidence, IP state and audit events. Adobe applications execute application-specific media operations through adapters.

### Adapters

- `premiere-pro/` — Premiere Pro UXP job contract and integration notes.
- `after-effects/` — After Effects composition/render adapter contract.
- `MEDIA-JOB-SCHEMA.json` — portable job/provenance envelope.
- `ADOBE-RDOS-EVENT-BRIDGE-v0.1.json` — event contract connecting media jobs to the R&D OS lifecycle.

## Gate status

- ADOBE-01: architecture/provenance layer — closed
- ADOBE-02: deterministic media-job validation architecture — closed
- ADOBE-03: R&D OS event bridge/schema contract — closed
- Live Adobe application execution — not yet verified

No Adobe executable, proprietary SDK binary or unlicensed third-party asset is bundled here.
