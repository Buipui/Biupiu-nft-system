# Biupiu Adobe Integration Gate — ADOBE-04

**Date:** 2026-09-22  
**Status:** REPOSITORY INTEGRATION VERIFIED / DESKTOP EXECUTION PENDING

## Purpose

Close the repository-side Adobe integration work without falsely claiming that Premiere Pro or After Effects have executed on the Windows workstation.

## Verified integration surface

- Biupiu R&D OS remains authoritative for project, research, evidence, IP, provenance and audit state.
- Adobe applications remain external execution providers behind adapter boundaries.
- Premiere Pro uses the UXP-first integration contract.
- After Effects uses the composition/render adapter contract.
- Firefly has a credential-free contract layer and a previously recorded live-generation verification.
- Media jobs use registered assets, project/research identifiers, evidence classification, licence/IP state and output hashing.
- Event bridge covers creation, validation, start, completion, failure, cancellation, asset registration and export verification.
- Render pipeline coordinates Adobe/Firefly with Unreal Engine 5, Blender, Twinmotion, KeyShot and Runway without embedding proprietary source trees.
- Source assets remain authoritative; generated/rendered outputs are derivative records.

## Verification boundaries

### VERIFIED
1. Adobe adapter architecture exists.
2. Deterministic media-job validation contract exists.
3. R&D OS event bridge exists.
4. Premiere Pro UXP contract exists.
5. After Effects composition contract exists.
6. Firefly integration contract and API client exist.
7. Firefly live generation was previously recorded as successful in the repository.
8. Provenance/IP/licensing boundaries are defined.
9. Cross-engine render-pipeline boundary is defined.

### OPEN — requires target Windows workstation
10. Premiere Pro UXP Developer Tool/import → sequence → export → SHA-256 verification.
11. After Effects project/composition → render → export → SHA-256 verification.
12. End-to-end R&D OS job/event bridge against live Premiere/After Effects.
13. UE5 → Adobe cinematic finishing ingestion/export test.
14. Final production regression across the complete media pipeline.

## Required evidence for ADOBE-04 runtime closure

A gate may only be marked runtime-verified after actual workstation evidence shows:

`REGISTERED ASSET → VALIDATED JOB → ADOBE EXECUTION → OUTPUT → SHA-256 → PROVENANCE → RELEASE STATE`

Failed/cancelled/partial jobs remain auditable and unreleasable.

## Security and licensing

- No Adobe credentials in source control.
- No Adobe proprietary binaries or SDK binaries redistributed.
- No credentials in Android/browser clients.
- Third-party examples remain reference material subject to their licences.
- Legacy CEP/ExtendScript remains behind compatibility adapters and is not the primary architecture.

## Result

**ADOBE-04 repository-side integration: VERIFIED.**

The remaining Adobe desktop gates are intentionally OPEN because the repository cannot substitute for execution on the user's installed Premiere Pro/After Effects environment.

