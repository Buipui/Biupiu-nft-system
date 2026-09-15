# BIUPIU CODEX — Speculative Research Execution Standard

**Version:** 1.0  
**Date:** 15 September 2026  
**Status:** Active

## Purpose

Provide a reproducible computational gate between speculative source material and Biupiu engineering/art outputs.

## Pipeline

`source capture → claim extraction → provenance graph → coordinate/text/material extraction → baseline dataset → hypothesis → null model → simulation/statistics → result → evidence-status update → research/IP output`

## Mandatory record fields

- unique claim/source ID
- exact source title/date
- timestamp or page reference where available
- original source cited by creator
- claim text/paraphrase
- predicted observable
- null hypothesis
- alternative hypothesis
- baseline dataset/source
- method and assumptions
- software/version/dependencies
- reproducibility status
- result state: `UNTESTED | DATA GATHERING | TESTED-POSITIVE | TESTED-NEGATIVE | INCONCLUSIVE`
- evidence status
- IP/licence/provenance status

## Test modules

### CODEX-SOURCEGRAPH
Map creator → cited author → primary source → independent datasets. Repeated lineage is marked as dependent, not independent corroboration.

### CODEX-SPEC-GIS
Convert claimed places into coordinates only when the source provides defensible geographic anchors. Record CRS, transform, uncertainty and confidence.

### CODEX-CARTOFORENSICS
Identify map projection, distortion, source date, scan/image integrity, georeferencing and whether an apparent match survives alternative projections.

### CODEX-PALAEO
Reconstruct palaeogeography using dated coastlines, river courses, lake levels, sea-level histories and sediment/tectonic evidence.

### CODEX-BATHY
Compare predicted submerged features against bathymetric datasets and resolution/uncertainty limits.

### CODEX-ALIGN
Test sacred-site or monument alignments with Monte Carlo/null models before interpreting significance.

### CODEX-UNDERGROUND
Model only individually supported caves/tunnels. Connectivity is a second-stage inference, never the starting assumption.

### CODEX-RESET
Build event-specific before/after timelines. Do not encode a global-reset prior into the model.

### CODEX-VIS
Perform visual provenance, geolocation, scale/perspective and construction-history checks before declaring an architectural anomaly.

### CODEX-ANTARCTICA
Use geodetic, satellite, ice-sheet, topographic and bathymetric baselines for alternative-geography claims.

### CODEX-SACRED-TECH
Translate alleged ancient devices or geometries into measurable dimensions, materials, inputs, outputs and conventional engineering comparators.

### CODEX-NAGA-HIM
Cross-reference named Naga/Himalayan sites against historical surveys, cadastral/topographic maps, geology, hydrology, GPR/resistivity and archaeological documentation.

## Statistical discipline

- Pre-register the observable before selecting the test.
- Report effect size and uncertainty, not only a visual match.
- Distinguish discovery from confirmation.
- Avoid post-hoc parameter tuning without reporting it.
- Use held-out/independent datasets where feasible.
- Treat multiple comparisons explicitly when searching many sites, maps or geometric relationships.

## Engineering discipline

A speculative mechanism can enter physical testing only after the source claim is converted into a falsifiable prediction. Energy claims require a complete input/output/loss balance. Materials claims require composition, processing history and characterisation. Geometric claims require dimensions and tolerances.

## NFT/IP gate

No speculative claim is represented in Biupiu NFT artwork as a historical fact unless independently established. Art may depict hypotheses, but metadata must label them as speculative/cultural/inspirational where appropriate and preserve source provenance. Original Biupiu computations and derived geometry may form proprietary IP subject to prior-art and licence review.
