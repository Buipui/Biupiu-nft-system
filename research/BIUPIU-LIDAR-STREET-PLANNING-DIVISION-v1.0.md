# BIUPIU LiDAR-Based Street Planning Division

**Division code:** `LIDAR-STREET`

**Version:** 1.0  
**Date:** 16 September 2026  
**Status:** Active research / planning framework

## Purpose

Create a dedicated Biupiu spatial-planning division that uses authoritative LiDAR-derived elevation, ground-level models, municipal buildings, roads and supporting infrastructure to study street, corridor and network planning.

The division is designed to serve the Cape Town FSO/light-internet programme first, while remaining reusable for regenerative agriculture access planning, water-flow studies, infrastructure resilience, robotics/logistics, disaster-prevention mapping and future Biupiu urban/regional planning research.

This is a **planning and research system**, not a municipal approval, cadastral survey, civil-engineering certification or construction design.

## Authoritative spatial evidence currently logged

### 1. City of Cape Town 5m contours
The municipal City Maps service exposes a machine-queryable 5m contour layer covering the municipal area. It supports JSON, GeoJSON and PBF queries and includes elevation attributes. The layer is updated annually. Source record: `CCT-5M-CONTOURS-CITYMAPS`. 

### 2. Current LiDAR-derived 5m DTM / contours
The City's current open-data layer documentation records a 5m contour product derived from LiDAR captured between November 2024 and March 2025, with approximately 15 points/m² and stated vertical accuracy of 0.1 m at 95%, derived from a 5m DTM. The height reference is the South African Land Levelling Datum. Source record: `CCT-LIDAR-2024-25-5M-DTM`. 

### 3. Ground Level Map 2019
The City also maintains a 5m bare-earth DEM derived from the 2019B LiDAR dataset, with stated vertical accuracy of 30 cm, and a corresponding Ground Level Map framework. Source record: `CCT-GLM-2019-LIDAR-5M-DEM`.

### 4. Roads
The City exposes machine-queryable Roads feature layers with polyline geometry and road-classification attributes. Source record: `CCT-ROADS-BASE-DATA`.

### 5. Buildings and infrastructure
CCT Buildings and related public/institutional infrastructure layers are part of the FSO GIS acquisition workflow. These are candidate spatial objects, not automatic deployment sites.

## Planning data stack

`LiDAR/DTM → terrain slope/aspect → road geometry → buildings/structures → infrastructure → drainage/water → environmental constraints → access → safety → network corridor → engineering review`

## Core planning functions

### A. Street geometry
- road centreline extraction;
- road hierarchy/classification;
- intersection identification;
- corridor continuity;
- slope-aware routing;
- terrain-constrained alternative routes.

### B. LiDAR terrain analysis
- ground elevation;
- elevation difference between candidate nodes;
- longitudinal and cross-slope estimation;
- terrain obstruction screening;
- ridge/valley identification;
- drainage-direction screening;
- cut/fill research inputs;
- visibility/line-of-sight terrain masks.

### C. FSO / optical-network planning
- candidate node elevation;
- building/terrain obstruction screening;
- preliminary inter-node distance;
- corridor graph construction;
- multi-hop route modelling;
- optical/RF/fibre fallback planning;
- future AI route optimisation;
- digital-twin calibration.

### D. Street and infrastructure planning research
The same spatial framework can later support:
- regenerative-agriculture access roads;
- farm-to-processing logistics;
- water infrastructure planning;
- Eco Motion collection routes;
- emergency/pre-disaster access;
- robotic delivery corridors;
- sensor-network placement;
- renewable-energy site screening;
- municipal infrastructure resilience studies.

## Cape Town FSO integration

The division becomes the geospatial foundation for:

`CCT GIS → LiDAR terrain → buildings → roads → candidate nodes → graph edges → LOS → weather/visibility → power/backhaul → aviation/permission/safety → optical link model → AI routing → digital twin`

The first research corridors remain:

1. CBD/Foreshore ↔ Woodstock/Salt River/Observatory.
2. Observatory/Rondebosch ↔ Newlands/Claremont.

No node is classified as deployable until all required validation gates are passed.

## Candidate-node data contract

Every machine-readable node should preserve:

`NODE_ID`
`SOURCE_LAYER`
`SOURCE_OBJECT_ID`
`LATITUDE`
`LONGITUDE`
`ELEVATION_M`
`STRUCTURE_HEIGHT_M`
`NODE_CLASS`
`ROAD_CONTEXT`
`LOS_STATUS`
`TERRAIN_STATUS`
`BUILDING_OBSTRUCTION_STATUS`
`VISIBILITY_STATUS`
`WIND_STATUS`
`FIBRE_STATUS`
`POWER_STATUS`
`ACCESS_STATUS`
`PERMISSION_STATUS`
`AVIATION_STATUS`
`ENVIRONMENT_STATUS`
`OPTICAL_SAFETY_STATUS`
`STRUCTURAL_STATUS`
`SOURCE_TIMESTAMP`
`VALIDATION_STATUS`

## Street-planning graph

The planned graph has three distinct layers:

### Layer 1 — physical geography
LiDAR/DTM, contours, roads, buildings, drainage and terrain.

### Layer 2 — infrastructure
Power, fibre/backhaul, public facilities, candidate structures and access.

### Layer 3 — operational network
FSO links, RF fallback, fibre fallback, AI routing, environmental telemetry and digital-twin state.

These layers must remain separately auditable.

## LiDAR-derived planning products

Future CODEX outputs:

- `LIDAR-DEM` — normalized elevation grid.
- `LIDAR-SLOPE` — slope map.
- `LIDAR-ASPECT` — terrain orientation map.
- `LIDAR-LOS` — terrain line-of-sight mask.
- `LIDAR-CORRIDOR` — terrain-aware street/network corridor model.
- `LIDAR-DRAINAGE` — preliminary flow-path screening.
- `LIDAR-NODE` — candidate infrastructure node model.
- `LIDAR-ROUTE` — constrained route graph.
- `LIDAR-TWIN` — digital-twin terrain layer.

## Existing Biupiu integration

This division cross-links:

- `LAND-GIS` — spatial evidence and GIS.
- `GEOARCH` — terrain, geology and landscape interpretation.
- `ALA` — long-term landscape atlas.
- `WATER` — drainage/hydrology and water infrastructure.
- `AGRI` — regenerative-farming access and landscape planning.
- `PHOTONICS` — FSO/LiFi/structured-light systems.
- `ELECTROMAG` — hybrid optical/RF systems.
- `METAMATERIALS` — future wavefront/beam-steering interfaces.
- `AI` — route optimisation and predictive link modelling.
- `DIGITAL-TWIN` — terrain/network simulation.
- `COMPUTE` — reproducible geospatial algorithms.
- `GEOMETRY` — terrain and corridor geometry.
- `ROBOTICS` — automated inspection/alignment/logistics.
- `ADV-MFG` — physical node and infrastructure manufacturing.
- `PRE-DISASTER` — infrastructure and terrain failure screening.
- `IP` — prior art, data licensing and engineering protection.

## Existing CODEX assets integrated

- `codex/gis/cpt_fso_site_screen.py`
- `codex/gis/cpt_fso_graph.py`
- `codex/gis/cpt_fso_arcgis_ingest.py`
- `codex/gis/test_cpt_fso_site_screen.py`
- `codex/gis/test_cpt_fso_graph.py`
- `codex/gis/test_cpt_fso_arcgis_ingest.py`

## Evidence discipline

LiDAR elevation is evidence about terrain geometry. It does **not** by itself establish structural capacity, property rights, public access, permission, road ownership, fibre availability, electrical capacity, aviation clearance, optical safety or construction feasibility.

The division therefore uses the following status ladder:

`RAW SOURCE → NORMALIZED → GEOREFERENCED → CROSS-CHECKED → MODELLED → FIELD-VALIDATED → ENGINEERING-VALIDATED → APPROVED`

A model cannot silently promote a lower status to a higher one.

## Privacy and publication control

Public GIS may contain sensitive or address-level information. The Biupiu research graph should preferentially publish generalized public/institutional nodes and source object IDs. Private residential locations should not be published as proposed infrastructure sites without a legitimate research/permission basis.

## Next execution gate

1. Query authoritative road/building/terrain layers.
2. Normalize geometry into the Biupiu spatial schema.
3. Generate terrain-aware candidate corridors.
4. Calculate preliminary elevation and slope differences.
5. Apply building/terrain obstruction tests.
6. Join infrastructure and environmental evidence.
7. Generate an auditable corridor graph.
8. Feed validated spatial features into the Cape Town FSO digital twin.

## Source register

- `CCT-5M-CONTOURS-CITYMAPS` — City of Cape Town City Maps 5m Contours service.
- `CCT-LIDAR-2024-25-5M-DTM` — City of Cape Town Open Data current LiDAR-derived 5m contour/DTM metadata.
- `CCT-GLM-2019-LIDAR-5M-DEM` — City of Cape Town Ground Level Map 2019 LiDAR-derived DEM.
- `CCT-ROADS-BASE-DATA` — City of Cape Town Roads GIS layers.
- `CCT-BUILDINGS` — City of Cape Town building GIS layer used by the FSO acquisition workflow.

## Status

**LIDAR-STREET v1.0 established.** The division is now the dedicated Biupiu spatial-planning branch for LiDAR-based terrain, street, infrastructure and corridor research, with the Cape Town FSO network as its first integrated application.
