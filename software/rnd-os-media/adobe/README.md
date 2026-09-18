# Biupiu Adobe Media Adapter Layer v0.1

This package defines the boundary between the Biupiu R&D OS and Adobe Creative Cloud media applications.

## Adapters

- `premiere-pro/` — Premiere Pro UXP job contract and integration notes.
- `after-effects/` — After Effects composition/render adapter contract.
- `MEDIA-JOB-SCHEMA.json` — portable job/provenance envelope.

## Design rule

The R&D OS owns research objects, provenance, evidence, IP state and job orchestration. Adobe applications own application-specific editing/compositing/render execution.

No Adobe executable or proprietary SDK binary is bundled here.

## Current status

Architecture only. Live application execution is gated on local Adobe installation, developer mode/UXP tooling where applicable, and end-to-end validation.
