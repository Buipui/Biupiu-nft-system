# BIUPIU EXTERMINATE PROTOCOLS v1.0

**Date:** 19 September 2026  
**Status:** Active — non-destructive code and repository cleanup gate

## Meaning

“Exterminate” means systematically remove defects, stale generated artefacts, accidental duplication and avoidable code debt **without destroying research lineage or third-party material**.

## Mandatory passes

### PASS 01 — Structural integrity
- malformed JSON;
- invalid machine-readable manifests;
- duplicate IDs;
- missing required metadata;
- broken internal file references.

### PASS 02 — Code hygiene
- Python syntax compilation;
- obvious import failures where static checks permit;
- TypeScript/JavaScript syntax/lint checks where project tooling exists;
- Kotlin/Gradle project structure checks;
- TODO/FIXME reporting for first-party code.

### PASS 03 — Duplicate analysis
- exact-content hashes;
- duplicate identifiers;
- repeated registry entries;
- suspicious copies of the same first-party implementation.

**No deletion occurs automatically.**

### PASS 04 — Dependency hygiene
- dependency/version records;
- licence/provenance presence;
- unpinned or ambiguous external resources;
- vendor/source boundaries.

### PASS 05 — Secret/security scan
Detect common accidental secrets and credentials. Never print secret values in reports.

### PASS 06 — Generated/build artefact scan
Identify accidentally tracked build output, caches, temporary files and local IDE artefacts.

### PASS 07 — Index reconciliation
Cross-check department, research, CODEX and release indexes after cleanup.

### PASS 08 — Regression gate
Run repository CI and record failures. A cleanup change cannot be declared verified merely because the cleanup script itself runs.

## Deletion rule

Automatic deletion is prohibited for:
- research records;
- historical experiments;
- negative results;
- vendor code;
- third-party source;
- evidence records;
- IP/provenance records.

Deletion requires explicit supersession evidence or human approval.

## Required report

`snapshot → findings → safe fixes → unresolved findings → regression result → index reconciliation → commit`

## Core principle

**Clean aggressively; delete conservatively.**

The protocol is intended to reduce repository entropy while preserving the cumulative R&D knowledge base.
