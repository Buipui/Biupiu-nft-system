# SEPARATION-03 — World Engine Learning Separation and Promotion Gate

**Date:** 19 September 2026  
**Status:** ARCHITECTURE COMMITTED — runtime/CI validation remains separate.

## Objective

Route lessons discovered from external engine research into distinct Biupiu layers without collapsing their responsibilities, then propagate only approved records into the Digital Twin and relevant departments.

## Canonical separation

`External research → Resource Registry → Biupiu Intelligence → AI OS proposal → Main OS validation → approved capability/asset manifest → Digital Twin → department adapters`

### Main OS

Owns authoritative state, contracts, validation, provenance, permissions, lifecycle and promotion. It is the final convergence point.

### Biupiu Intelligence

Owns reusable knowledge: evidence, lessons, failure modes, compatibility observations, dependency impact, patterns and provenance. Intelligence records do not become executable capabilities merely by being learned.

### AI OS

Consumes Intelligence records to plan, retrieve, classify, cross-link and propose implementation. AI OS may generate adapter proposals and test plans but cannot bypass Main OS validation.

### Digital Twin

Consumes only approved manifests, schemas, measured telemetry and validated simulation adapters. It mirrors approved system state; it does not promote research directly.

### Departments

Consume approved capability/asset manifests through their own adapter contracts. Each department keeps local implementation details while preserving source identity and provenance.

## Asset classes

- **REFERENCE:** knowledge only; no runtime dependency.
- **PATTERN:** reusable architectural lesson; requires independent implementation.
- **ADAPTER:** Biupiu-authored interface implementation; requires tests.
- **ASSET:** approved reusable model/material/scene/data artifact; requires provenance.
- **DEPENDENCY:** externally maintained package; requires licence/security/version validation.
- **PROHIBITED:** proprietary/confidential material or unverified inputs; cannot be promoted.

## Promotion rule

No external resource moves directly into Main OS, Digital Twin or a department. Every promotion must carry source identity, licence status, compatibility evidence, deterministic test evidence and a provenance record.

## Conflict rule

When two resources disagree, preserve both records, classify the conflict, identify the authoritative Biupiu contract, and route the resolution through validation. Do not silently overwrite historical evidence.

## Result

The separation is now explicit for World Engine research and is compatible with the existing OS/AI boundary. Host execution, CI results and real simulator/renderer validation remain separate evidence gates.
