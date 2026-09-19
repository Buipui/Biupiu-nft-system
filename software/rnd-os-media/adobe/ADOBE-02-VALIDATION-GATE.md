# ADOBE-02 — Deterministic Media Job Validation Gate

## Objective
Close the next architecture gate after ADOBE-01 by defining deterministic validation requirements shared by Premiere Pro and After Effects.

## Rules
1. Only registered Biupiu assets may enter an Adobe media job.
2. Every job must identify project, research objects and department.
3. Evidence classification, IP state and licence state are mandatory.
4. Adobe application/version and adapter version must be recorded when execution occurs.
5. Every exported deliverable must produce a SHA-256 hash and provenance record.
6. Failed, cancelled or partial jobs must remain auditable and must not be marked as released.
7. Adobe binaries, proprietary SDKs and third-party assets are not redistributed by the repository.
8. Live execution is not claimed by repository-only validation.

## Current verification
- Media-job schema present.
- Premiere UXP contract present.
- After Effects composition contract present.
- Provenance/licensing boundaries documented.
- Live Adobe application execution: **NOT YET VERIFIED**.

## Gate status
**ADOBE-02 ARCHITECTURE GATE CLOSED.**

Next gate: connect these contracts to the existing R&D OS job/event model and run repository-level schema tests.
