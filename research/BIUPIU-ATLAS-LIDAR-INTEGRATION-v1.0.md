# Biupiu Atlas — LiDAR Street Planning Integration

**Version:** 1.0  
**Date:** 16 September 2026  
**Status:** Integrated research layer

## Atlas integration

The Biupiu Atlas now incorporates a dedicated `LIDAR-STREET` spatial-planning division. It consolidates the previously logged Cape Town FSO/GIS work into a reusable spatial framework without replacing the original evidence records.

### Existing records retained

- `CAPE-TOWN-LIGHT-INTERNET-AI-FSO-NETWORK-v1.0.md` — overall FSO/light-internet architecture.
- `CAPE-TOWN-FSO-GIS-DATA-ACQUISITION-v1.0.md` — authoritative municipal GIS acquisition workflow.
- `CAPE-TOWN-FSO-GIS-FINDINGS-v1.0.md` — municipal GIS/LiDAR findings.
- `CAPE-TOWN-FSO-CANDIDATE-GRAPH-v1.0.md` — candidate-node/edge graph model.
- `BIUPIU-LIDAR-STREET-PLANNING-DIVISION-v1.0.md` — dedicated LiDAR/street-planning division.
- `codex/gis/cpt_fso_site_screen.py` — preliminary deterministic FSO site screening.
- `codex/gis/cpt_fso_graph.py` — deterministic graph construction.
- `codex/gis/cpt_fso_arcgis_ingest.py` — ArcGIS candidate-node normalization.
- `codex/gis/lidar_street_planning.py` — terrain/elevation/grade primitives.

## Atlas spatial stack

`MUNICIPAL GIS → LiDAR/DTM → contours → terrain derivatives → roads → buildings → infrastructure → hydrology → environmental constraints → candidate corridors → LOS → network graph → engineering/regulatory validation`

## LiDAR planning products

The Atlas will support normalized products for:

1. elevation/DTM;
2. contours;
3. slope;
4. aspect;
5. terrain line-of-sight;
6. road gradient;
7. corridor elevation profile;
8. drainage/flow-path screening;
9. candidate infrastructure nodes;
10. terrain-aware network routes;
11. digital-twin terrain layers.

## FSO integration

For the Cape Town optical-network programme, LiDAR becomes the terrain layer beneath the candidate-node graph:

`LiDAR terrain → road/building geometry → candidate node → edge distance/elevation → obstruction → atmospheric model → power/backhaul → permission/aviation/safety → FSO link model → AI routing → digital twin`

The first corridors remain:

- CBD/Foreshore ↔ Woodstock/Salt River/Observatory.
- Observatory/Rondebosch ↔ Newlands/Claremont.

These are **research corridors**, not approved deployment routes.

## Cross-department routing

`LIDAR-STREET ↔ LAND-GIS ↔ GEOARCH ↔ ALA ↔ WATER ↔ AGRI ↔ PRE-DISASTER`

`LIDAR-STREET ↔ PHOTONICS ↔ ELECTROMAG ↔ METAMATERIALS ↔ FSO-CPT`

`LIDAR-STREET ↔ COMPUTE ↔ GEOMETRY ↔ AI ↔ DIGITAL-TWIN`

`LIDAR-STREET ↔ ROBOTICS ↔ ADV-MFG`

`LIDAR-STREET ↔ IP`

## Atlas evidence boundary

LiDAR is treated as measured/geospatial evidence of terrain geometry, subject to the source dataset's stated accuracy and resolution. It is not treated as proof of property rights, structural capacity, road ownership, network permission, telecom authorisation, aviation clearance or construction feasibility.

All derived planning records must preserve source identifiers, acquisition/update timestamps, processing method and validation status.

## Status ladder

`RAW → NORMALIZED → GEOREFERENCED → DERIVED → CROSS-CHECKED → MODELLED → FIELD-VALIDATED → ENGINEERING-VALIDATED`

No Atlas workflow may silently promote a record between stages.

## Future Atlas expansion

The same LiDAR/street framework can later support:

- regenerative-farming access and field logistics;
- water and drainage planning;
- Eco Motion collection routes;
- emergency/pre-disaster access analysis;
- robotics and autonomous inspection corridors;
- renewable-energy terrain screening;
- sensor-network planning;
- urban/regional infrastructure resilience;
- historical landscape reconstruction when combined with archaeological/historical GIS.

## Execution status

**Integrated.** The LiDAR street-planning division, municipal GIS evidence, FSO candidate graph and CODEX spatial primitives are now linked as one auditable Biupiu Atlas planning layer. Actual candidate-node population and terrain/structure LOS calculations remain the next validation stage and will only use retrieved authoritative spatial features.
