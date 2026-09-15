# BIUPIU SPEC — Sepehr / Atlantean Gardens Claim Extraction Queue

**Version:** 1.0  
**Date:** 15 September 2026  
**Status:** Active extraction layer

## Purpose

Convert selected Robert Sepehr / Atlantean Gardens material from topic-level indexing into auditable claim records. Each record must preserve the distinction between what a video says, what the original evidence says, and what a Biupiu computational or experimental test can actually evaluate.

## Extraction schema

`record_id | source_title | source_date | source_family | claim | claim_type | original_source | evidence_status | prediction | null | alternative | test_method | CODEX | ALA | notes`

## Seed extraction records

### SEP-EX-001 — The Fall of Atlantis
- **Source family:** `SEP-ATL`
- **Archive evidence:** Atlantean Gardens catalogue lists *The Fall of Atlantis* as a dated video entry.
- **Claim capture:** Full claim text and timestamps remain **UNEXTRACTED** until the video itself and its cited sources are reviewed.
- **Status:** `DATA GATHERING`
- **Required source chain:** video → timestamp → cited primary/historical source → Plato and later textual tradition → palaeogeography/bathymetry → archaeology.
- **Prediction gate:** no geographic prediction is accepted until the video supplies explicit coordinates, regional constraints, chronology or material evidence.
- **CODEX:** `CODEX-SOURCEGRAPH`, `CODEX-SPEC-GIS`, `CODEX-PALAEO`, `CODEX-BATHY`.
- **ALA:** `ALA-ATLANTIS`, `ALA-COAST`, `ALA-PRE-DISASTER`.

### SEP-EX-002 — Forgotten Dream of Atlantis
- **Source family:** `SEP-ATL`
- **Archive evidence:** Atlantean Gardens catalogue lists *Forgotten Dream of Atlantis*.
- **Claim capture:** Exact claims/timestamps **UNEXTRACTED**.
- **Status:** `DATA GATHERING`
- **Test gate:** extract any proposed location, chronology, geological event, or cultural continuity claim and test against independent datasets.
- **CODEX:** `CODEX-SOURCEGRAPH`, `CODEX-PALAEO`, `CODEX-SPEC-GIS`.

### SEP-EX-003 — Esoteric Secrets of Atlantis
- **Source family:** `SEP-ATL` / `SEP-TECH`
- **Archive evidence:** Atlantean Gardens catalogue lists *Esoteric Secrets of Atlantis*.
- **Claim capture:** Exact claims/timestamps **UNEXTRACTED**.
- **Status:** `DATA GATHERING`
- **Control:** esoteric symbolism is catalogued as cultural material unless a separate physical or historical proposition is stated.
- **CODEX:** `CODEX-SOURCEGRAPH`, `CODEX-SACRED-TECH` only for explicit engineering claims.

### SEP-EX-004 — Entrances to Inner Earth
- **Source family:** `SEP-UND`
- **Archive evidence:** Atlantean Gardens catalogue lists *Entrances to Inner Earth*.
- **Claim capture:** Exact locations, entrance descriptions, chronology and evidentiary basis **UNEXTRACTED**.
- **Status:** `DATA GATHERING`
- **Test gate:** named site → historical survey/map → geology → surface morphology → geophysics → archaeology.
- **Null:** natural cave, later construction, mislocation or unsupported tradition.
- **CODEX:** `CODEX-UNDERGROUND`, `CODEX-SPEC-GIS`, `LAND-GIS`.

### SEP-EX-005 — Antarctica Disclosure
- **Source family:** `SEP-ANT`
- **Archive evidence:** Atlantean Gardens catalogue lists *Antarctica Disclosure*.
- **Claim capture:** Explicit predicted features/coordinates **UNEXTRACTED**.
- **Status:** `DATA GATHERING`
- **Test gate:** claim coordinate/feature → satellite/geodesy/ice-sheet/topography/bathymetry → historical mapping.
- **Null:** feature is absent or explained by known geography, projection, ice or geology.
- **CODEX:** `CODEX-ANTARCTICA`, `CODEX-BATHY`, `CARTOFORENSICS`.

### SEP-EX-006 — Origins of the First Europeans
- **Source family:** `SEP-HUM`
- **Archive evidence:** Atlantean Gardens catalogue lists *Origins of the First Europeans*.
- **Claim capture:** Exact genomic/fossil/population claim **UNEXTRACTED**.
- **Status:** `DATA GATHERING`
- **Test gate:** claim → primary ancient-DNA/fossil/archaeological source → chronology → population-genetic interpretation.
- **Control:** separate valid population complexity from race/species terminology that is not supported by genetics.
- **CODEX:** `CODEX-SOURCEGRAPH`; cross-link `ATH-HO-AFRICA` and `SPEC-HUMAN-ORIGINS`.

## Current external archive signal

The public Atlantean Gardens catalogue remains active and contains entries across Atlantis, underground traditions, Antarctica, ancient technology and human-origins themes. A current third-party channel audit dated 2 September 2026 also records recent Robert Sepehr uploads, confirming that the source family should remain a live extraction queue rather than a closed archive.

A contemporaneous Divergent Files episode published 9 September 2026, *What If Egypt Didn’t Build the Great Pyramid?*, similarly mixes established evidence with disputed interpretations. It is therefore routed through `SPEC-VIS`, `SPEC-SACRED-TECH` and `ALA` only after its individual claims are extracted and independently checked.

## Execution rule

No claim is promoted from `DATA GATHERING` to `TESTED-POSITIVE` solely because multiple videos repeat it. Repetition is tracked in the source-genealogy graph, while independent archaeological, geological, genomic, geodetic or experimental evidence is tracked separately.

## Provenance references

- Robert Sepehr / Atlantean Gardens public archive: Patreon sitemap/catalogue.
- Robert Sepehr channel activity audit: SPEAKRJ, data updated 2 September 2026.
- Divergent Files current episode record: iHeart, 9 September 2026.

## Next extraction target

`SEP-EX-001` — extract the first explicit Atlantis geographic/chronological predictions and map each to its earliest cited source before creating any convergence score.
