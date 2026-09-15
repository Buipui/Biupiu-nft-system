# BIUPIU SPEC — Claim-by-Claim Verification Registry

**Version:** 1.0  
**Date:** 15 September 2026  
**Purpose:** Convert the highest-priority speculative-source claims into traceable verification records.

## Evidence rule
Creator ≠ source ≠ original evidence. A repeated claim is not independent corroboration. Speculative records remain hypotheses until primary evidence and reproducible tests support them.

## Priority claim records

### SPEC-CLAIM-001 — Atlantis
**Source family:** Plato / later Atlantis traditions / speculative channels.  
**Current evidence status:** Mythological-Cultural / Unresolved as a historical geographic claim.  
**Primary-source baseline:** Plato's *Timaeus* and *Critias*. Scholarly treatment identifies the Atlantis account as a Platonic myth and notes that *Critias* is unfinished. citeturn0search6turn0search0  
**Testable extraction:** identify every geographic constraint in the texts; map candidate locations; compare chronology, bathymetry, palaeogeography, tectonics and archaeology.  
**Null:** no candidate location satisfies the combined textual/geographic constraints better than alternatives.  
**Alternative:** one or more candidate locations show statistically/archaeologically unusual agreement with independently dated evidence.  
**CODEX:** `CODEX-SPEC-GIS`, `CODEX-PALAEO`, `CODEX-CARTOFORENSICS`, `ALA-ATLANTIS`.

### SPEC-CLAIM-002 — Ancient catastrophe/reset
**Source family:** Sepehr / Atlantean Gardens / Divergent and related traditions.  
**Status:** Regional catastrophe evidence may be established in individual cases; a single global civilisation-reset model is unproven.  
**Test:** construct event-specific timelines and test geological, palaeoclimate and archaeological signatures rather than assuming one global event.  
**Null:** observed destruction layers are temporally/geographically independent events.  
**Alternative:** multiple independently dated sites share a synchronous, physically plausible event signature.  
**CODEX:** `CODEX-RESET`, `ALA-PRE-DISASTER`, `FAILURE`.

### SPEC-CLAIM-003 — European/ancient underground networks
**Source family:** speculative video claims and local traditions.  
**Status:** D / site-specific verification required.  
**Test:** create site records only from named locations; verify historical references, entrances, construction chronology, geology and geophysics; model network connectivity only after individual segments are independently supported.  
**Null:** apparent connections are natural features, unrelated structures or later constructions.  
**Alternative:** independently verified artificial segments form a dated, physically connected network.  
**CODEX:** `CODEX-UNDERGROUND`, `SPEC-UNDERGROUND`, `UNDERGROUND`.

### SPEC-CLAIM-004 — Alternative world maps / hidden lands
**Source family:** VOC and related alternative-cartography channels.  
**Status:** Speculative.  
**Test:** extract exact claimed coordinates, coastlines and elevations; compare with geodetic reference systems, satellite imagery, DEMs and bathymetry. Antarctica is already covered by extensive satellite/remote-sensing datasets, including USGS RAMP and LIMA and ESA CryoSat products. citeturn0search3turn0search14turn0search15  
**Null:** claimed hidden land is absent or explained by known topography/ice/bathymetry/projection effects.  
**Alternative:** a reproducible, independently observed geographic feature exists at the predicted coordinates and is inconsistent with baseline datasets.  
**CODEX:** `CODEX-MOONMAP`, `CODEX-ANTARCTICA`, `CODEX-BATHY`, `CARTOFORENSICS`, `ALA-HIDDEN-LANDS`.

### SPEC-CLAIM-005 — Moon/world-map projection
**Source family:** VOC Plasma Moon material.  
**Status:** Speculative.  
**Test:** identify the source image, determine projection assumptions, perform photogrammetric/geometry reconstruction and compare predicted lunar features against independent lunar imagery.  
**Null:** apparent correspondence is produced by projection, image transformation or coincidental pattern matching.  
**Alternative:** a stable mapping transform predicts multiple independent lunar features without ad-hoc parameter tuning.  
**CODEX:** `CODEX-MOONMAP`, `CG-3D`.

### SPEC-CLAIM-006 — Hyperborea/Thule
**Source family:** ancient/medieval textual traditions plus modern speculative interpretations.  
**Status:** Mythological-Cultural / unresolved geographic identification.  
**Test:** build a source genealogy; distinguish ancient ethnogeographic references from modern continental reconstructions; compare candidate locations against palaeogeography and historical geography.  
**Null:** no uniquely supported geographic location emerges.  
**Alternative:** independent ancient sources converge on a geographically coherent, independently evidenced region.  
**CODEX:** `CODEX-SOURCEGRAPH`, `CODEX-PALAEO`, `ALA-HYPERBOREA`.

### SPEC-CLAIM-007 — Vril / scalar / free-energy mechanisms
**Source family:** historical occult/esoteric traditions and modern speculative engineering claims.  
**Status:** Historical belief may be documented; physical energy-generation claims require reproducible evidence.  
**Test gate:** define an explicit energy source, conservation pathway, input/output measurement and repeatable apparatus before experimentation.  
**Null:** output is explained by stored energy, environmental coupling, measurement error or conventional electromagnetic/thermal/mechanical sources.  
**Alternative:** independently reproduced excess energy remains after all identified inputs and losses are measured.  
**CODEX:** `CODEX-SPEC-GIS` not applicable; use `CODEX` experimental provenance and energy-balance methods.

### SPEC-CLAIM-008 — Alternative human-origins models
**Source family:** modern alternative-history claims.  
**Status:** Speculative where they contradict established fossil/genomic evidence.  
**Test:** compare explicit predictions with primary fossil, archaeological and ancient-DNA datasets; separate valid population-complexity observations from unsupported species/race claims.  
**Null:** model does not improve explanatory power over current population-genetic/archaeological models.  
**Alternative:** model produces independently testable predictions supported by new evidence.  
**CODEX:** `SPEC-HUMAN-ORIGINS`, `ATH-HO-AFRICA`.

### SPEC-CLAIM-009 — Historical architectural anomalies
**Source family:** Divergent/visual-source material.  
**Status:** Unresolved until provenance is established.  
**Test:** reverse-image/source tracing; geolocation; construction-date verification; architectural measurement; historical map/cadastral comparison; ordinary engineering explanation first.  
**Null:** anomaly is explained by known architecture, restoration, perspective, image manipulation or miscaptioning.  
**Alternative:** independently documented construction feature remains unexplained after controls.  
**CODEX:** `CODEX-VIS`, `CARTOFORENSICS`, `LAND-GIS`.

## Execution order
1. Atlantis textual/geographic extraction.
2. Named underground sites only; no network inference before segment verification.
3. Alternative-map coordinate extraction and geodetic comparison.
4. Moon/world-map projection tests.
5. Catastrophe/pre-disaster event matrix.
6. Hyperborea/Thule source genealogy.
7. Human-origins claim separation and evidence audit.
8. Architectural anomaly provenance and measurement.
9. Vril/free-energy mechanism gate.

## Result states
`UNTESTED` → `DATA GATHERING` → `TESTED-POSITIVE` / `TESTED-NEGATIVE` / `INCONCLUSIVE` → evidence-status update.

**Important:** `TESTED-POSITIVE` means the specified prediction was observed; it does not by itself establish the larger speculative interpretation.
