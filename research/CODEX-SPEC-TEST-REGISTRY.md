# BIUPIU CODEX — Speculative Claim Test Registry

**Version:** 1.1  
**Date:** 15 September 2026

## Purpose
Convert speculative video/source claims into explicit, reproducible tests. This registry does not endorse the claims.

## Test matrix

| ID | Claim family | Test | Baseline | Status |
|---|---|---|---|---|
| TEST-VOC-001 | Plasma Moon/world-map projection | Reconstruct image geometry and projection; compare against known lunar/geodetic geometry | NASA/public lunar imagery + geodesy | Data gathering |
| TEST-VOC-002 | Pangaia/alternative continents | Extract predicted coordinates and compare with satellite/bathymetry/palaeogeography | GEBCO/authoritative mapping | Planned |
| TEST-VOC-003 | Lands beyond Antarctica | Convert claim into coordinates/area/elevation predictions and test against Antarctic mapping | Satellite + DEM + bathymetry | Data gathering |
| TEST-VOC-004 | Magnetic North/great-circle claims | Compare claimed alignments with magnetic-field models and randomised controls | Geomagnetic reference models | Planned |
| TEST-SEP-001 | Atlantis | Convert textual/geographic claims into predicted sites and environmental signatures | Plato/textual scholarship + palaeogeography + archaeology | Data gathering |
| TEST-SEP-002 | Hyperborea/Thule | Trace historical place-name genealogy and test candidate geography | Historical sources + palaeogeography | Planned |
| TEST-SEP-003 | Antediluvian catastrophe | Build event-specific chronology; test geological/archaeological evidence | Palaeoclimate + archaeology + geology | Planned |
| TEST-SEP-004 | Underground tunnel networks | Map verified sites, date structures and test connectivity | Archaeology + geophysics + GIS | Planned |
| TEST-SEP-005 | Vril/free energy | Define measurable energy mechanism and compare output against controls | Reproducible electrical/thermal/mechanical experiment | Gate: mechanism required |
| TEST-SEP-006 | Alternative human origins | Compare proposed model against fossils, ancient genomes and population genetics | Primary genomic/archaeological literature | Planned |
| TEST-DIV-001 | Architectural reset anomalies | Geolocate images; establish construction date and ordinary explanations | Historical maps/cadastral/architectural records | Data gathering |
| TEST-DIV-002 | Landscape reset | Identify proposed event and compare pre/post survey evidence | ALA-PRE-DISASTER | Planned |
| TEST-DIV-003 | Alternative Moon/Antarctica claims | Separate visual claim from measurable geographic prediction | Lunar/Antarctic authoritative datasets | Data gathering |

## Immediate claim registry
Detailed claim records are maintained in `research/SPEC-CLAIM-REGISTRY.md`. Current priority records are `SPEC-CLAIM-001` through `SPEC-CLAIM-009` covering Atlantis, catastrophe/reset, underground networks, alternative maps, Moon/world-map projection, Hyperborea/Thule, Vril/free-energy, alternative human origins and architectural anomalies.

## Test protocol
1. Preserve the original claim and source.
2. Record creator, date and source genealogy.
3. Extract the strongest falsifiable interpretation.
4. Define null and alternative hypotheses.
5. Identify independent baseline datasets.
6. Pre-register variables and acceptance criteria where practical.
7. Run the GIS/statistical/computational test.
8. Record positive, negative and inconclusive results.
9. Update evidence status.
10. Never upgrade a claim merely because it is repeated by multiple channels.

## Primary-baseline controls
- **Atlantis:** Plato's *Timaeus*/*Critias* and current classical scholarship. The Atlantis narrative is treated as a Platonic mythological/philosophical account until independent historical evidence demonstrates otherwise. citeturn0search6turn0search1
- **Antarctica:** authoritative satellite/DEM baselines including USGS RAMP/LIMA and ESA CryoSat-derived elevation products. citeturn0search3turn0search14turn0search15
- **Geography:** use geodetic coordinates and documented projections before comparing alternative maps.
- **Underground archaeology:** require site-specific physical/geophysical/archaeological evidence before network inference.
- **Human origins:** require primary fossil/genomic/archaeological evidence and explicit model predictions.

## CODEX implementation targets
- Python notebooks for reproducible analysis.
- GIS layers with uncertainty metadata.
- Projection/georeferencing tools.
- Monte Carlo alignment testing.
- Source-genealogy graphs.
- Palaeogeographic and bathymetric comparison.
- Image/architecture measurement tools.
- Digital-twin links where a physical mechanism is proposed.

## Evidence gate
A speculative claim becomes a Biupiu engineering candidate only when it produces a measurable prediction. A technology/IP candidate additionally requires reproducibility, prior-art review, licensing/provenance review and a plausible engineering mechanism.

**Status:** Registry expanded to v1.1; claim-by-claim verification is now formally linked to the execution pipeline.