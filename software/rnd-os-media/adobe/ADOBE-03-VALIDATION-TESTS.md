# ADOBE-03 — R&D OS Event Bridge & Schema Validation

## Scope
Connect the Adobe media contracts to the R&D OS lifecycle without coupling the core OS to a specific Adobe application.

## Lifecycle mapping

`PROJECT → RESEARCH OBJECT → SOURCE/CLAIM → MEDIA JOB → VALIDATION → EXPORT → AUDIT EVENT`

Adobe jobs remain subordinate to the R&D OS project, provenance, evidence and IP model.

## Event contract

The adapter emits lifecycle events:
- created
- validated
- started
- completed
- failed
- cancelled
- export verified

Every event carries a stable job/project identity and source commit. Completion additionally requires output hash and provenance.

## Repository-level validation

The contracts are machine-readable JSON and use fixed required fields. Validation must reject:
- missing project/job identity
- missing evidence classification
- missing licence state
- completion without output hash
- completion without provenance
- release of failed/cancelled jobs

## Result

**ADOBE-03 ARCHITECTURE/SCHEMA GATE CLOSED.**

This gate verifies repository contracts, not execution inside Adobe applications. Live end-to-end testing remains a workstation integration gate.
