# BIUPIU CODEX DEPARTMENT SIMULATION QUEUES

**Version:** 1.3  
**Date:** 19 September 2026  
**Status:** Active — source-integrated computational backlog

## P0 execution activation

Activated P0 queues: `Q-CODEX-001`, `Q-IP-001`, `Q-AGRI-001`, `Q-HEMP-001`, and `Q-PHO-001`. Activation means the test definition, inputs and validation gate are ready; it does not mean a simulation result exists.

## New source-routing rule

All new CODEX queues inherit `research/SOURCE-TO-DEPARTMENT-CROSSWALK.md` and `research/BIUPIU-RESEARCH-OPERATING-PROTOCOL-v2.0.md`. Ancient-technology queues use AnthroSource alongside primary archaeology/JSTOR; scientific/engineering discovery uses ResearchGate with publisher/DOI verification; systems/implementation questions use Emerald where relevant; implementation/IP questions use patents/public declassified records; code and computational methods must be versioned and licensed.

## Next-gate activation — Ancient Technology Computational Archaeology

The AnthroSource register now supplies concrete computational/experimental archaeology inputs. The following queues are activated as **P1 research gates**:

| Queue ID | Department | Model / method | First executable test | Dataset required | Validation | Priority | Status |
|---|---|---|---|---|---|---|---|
| Q-BLOMBOS-001 | AAT/AAT-H/GEOMETRY | image vectorisation + topology/statistics | scale-calibrated engraving geometry baseline | high-resolution public imagery + documented scale | independent vectorisation + null/alternative comparison | P1 | READY |
| Q-BOKONI-001 | AAT-H/AGRI/GEOARCH | LiDAR/GIS + landscape reconstruction | terraced-field candidate map | LiDAR/DEM/aerial imagery + archaeological controls | archaeological verification + temporal/environmental cross-check | P1 | READY |
| Q-GEOAI-001 | GEOARCH/LAND-GIS/AI | remote sensing + GeoAI | stone-wall candidate detection benchmark | LiDAR/aerial imagery + verified archaeological labels | held-out spatial test + human archaeological verification | P1 | READY |
| Q-PHOTO-ARCH-001 | GEOARCH/ALA/DIGITAL-TWIN | retrospective photogrammetry | archival-photo 3D reconstruction baseline | historical excavation photographs + control points | coordinate/geometry consistency | P1 | READY |

### Q-BLOMBOS-001 — controlled functional-reconstruction gate

Workflow:

`archaeological image → scale calibration → vectorisation → orientation/spacing/topology metrics → competing functional hypotheses → null/alternative models → statistical comparison → experimental reconstruction → independent replication`

No functional interpretation is promoted to historical fact solely from geometric similarity.

### Q-BOKONI-001 — Southern African ancient-agriculture gate

Workflow:

`LiDAR/DEM/aerial imagery → georeference → terrace/field segmentation → environmental variables → chronology/archaeological controls → landscape reconstruction → modern regenerative-agriculture hypothesis → field test`

The historical Bokoni record and modern regenerative-farming engineering question remain separate evidence objects.

### Q-GEOAI-001 — archaeological discovery gate

Workflow:

`public remote sensing → preprocessing → labelled archaeological/non-archaeological examples → model training → spatially held-out evaluation → human archaeological verification → provenance record`

The model may identify candidates; it does not independently establish archaeological interpretation.

### Q-PHOTO-ARCH-001 — Digital Ancient Technology Atlas gate

Workflow:

`archival photographs → photogrammetry → scale/georeference → 3D reconstruction → uncertainty record → temporal layer → ALA/Digital-Twin asset`

## Source-control rule for ResearchGate

ResearchGate is a discovery and repository layer, not an automatic authority layer. Each ResearchGate record must be traced to its DOI, publisher, institutional repository or primary dataset when available. Duplicate uploads are one source lineage. Extract methods, parameters, limitations and provenance rather than relying on titles or abstracts alone.

## Existing queue

The remaining queues from v1.2 remain active unless explicitly superseded. In particular, `Q-AAT-001` and `Q-ATH-001` accept AnthroSource records as scholarly anthropology/archaeology inputs, while primary archaeology remains the preferred direct historical evidence.

## Queue states

UNQUEUED → DATA-GATHERING → READY → SIMULATING → VALIDATING → PROTOTYPE → COMPLETE. HOLD is used for data, regulatory, safety, licence or IP blocks. VERIFY SOURCE FILE is used where an original historical register/source must first be recovered.

## Safety and evidence control

Civilian archaeological, materials, agriculture, energy, photonics and computational research may proceed through the normal evidence pipeline. Aerospace/mobility work remains limited to lawful public/dual-use efficiency, materials and historical engineering research. No classified, restricted or weapon-development material is requested or incorporated.

All queues inherit the repository evidence doctrine and must not convert speculative material into factual claims merely because a simulation is visually suggestive.