# Cape Town FSO LiDAR Corridor Dataset v1.0

**Status:** Research-stage corridor dataset specification with authoritative-source acquisition record  
**Date:** 16 September 2026

## Execution-gate result

The authoritative City of Cape Town spatial services were re-queried. The current municipal service exposes CCT Buildings, Roads, public/institutional facilities, electricity/public lighting and 5m contour layers. The current 5m contour layer is derived from LiDAR captured November 2024–March 2025 and is derived from a 5m DTM. citeturn0search0turn0search6

A separate City service documents the 2025 5m bare-earth DTM as derived from 2025 LiDAR. citeturn0search10

The City also maintains the older 2019B LiDAR Ground Level Map, including a 5m bare-earth DEM and 2m contours, providing a historical comparison surface. citeturn0search11turn0search14

## Source layers acquired/confirmed

| Source ID | Layer | Role | Status |
|---|---|---|---|
| CCT-LIDAR-2025-DTM | 2025 5m bare-earth DTM | ground elevation | confirmed service |
| CCT-LIDAR-2024-25-CONTOURS | current 5m contours | terrain screening | confirmed service |
| CCT-GLM-2019 | 2019B 5m DEM / 2m contours | historical ground-level comparison | confirmed service |
| CCT-BUILDINGS | CCT Buildings | obstruction/candidate structure layer | listed in municipal service |
| CCT-ROADS | Roads | street/corridor geometry | municipal GIS source |
| CCT-PUBLIC-INFRA | community/public facilities | candidate-node screening | municipal GIS source |
| CCT-ELECTRIC | public lighting/electricity layers | power/infrastructure context | municipal GIS source |

## Corridor execution model

The two existing research corridors are retained:

1. CBD/Foreshore → Woodstock/Salt River/Observatory
2. Observatory/Rondebosch → Newlands/Claremont

They are **research corridors, not approved deployment routes**.

For each corridor the dataset pipeline is:

`road geometry → LiDAR/DTM elevation → terrain grade → building obstruction → candidate public/institutional nodes → infrastructure context → atmospheric data → optical link model → regulatory/safety gates`

## Important data limitation

The live ArcGIS service exposes the required layers, but the current web retrieval environment did not return the individual CCT Buildings/Roads feature records from direct layer requests. Therefore this execution does **not** fabricate node coordinates, elevations or LOS results.

The next machine-ingestion step must query the feature layers directly and preserve their source object IDs and timestamps.

## Required machine output

```text
CORRIDOR_ID
NODE_ID
SOURCE_LAYER
SOURCE_OBJECT_ID
NODE_CLASS
LATITUDE
LONGITUDE
GROUND_ELEVATION_M
STRUCTURE_HEIGHT_M
ROAD_CONTEXT
TERRAIN_GRADE
TERRAIN_OBSTRUCTION
BUILDING_OBSTRUCTION
LINK_DISTANCE_M
LOS_STATUS
VISIBILITY_STATUS
POWER_STATUS
BACKHAUL_STATUS
ACCESS_STATUS
PERMISSION_STATUS
AVIATION_STATUS
OPTICAL_SAFETY_STATUS
ENGINEERING_STATUS
SOURCE_TIMESTAMP
VALIDATION_STATUS
```

## LiDAR comparison rule

Where both current and historical terrain products are available, Biupiu should calculate:

`ΔZ = Z_current - Z_historical`

but must not interpret a difference as actual physical terrain change until the source epochs, datum, processing method and spatial registration are reconciled.

## Atlas integration

This dataset belongs to the Biupiu Atlas `LIDAR-STREET` spatial layer and cross-links to:

`LAND-GIS ↔ GEOARCH ↔ WATER ↔ AGRI ↔ PRE-DISASTER ↔ PHOTONICS ↔ FSO-CPT ↔ AI ↔ DIGITAL-TWIN ↔ COMPUTE`

## Validation gates

1. Authoritative feature extraction.
2. Coordinate/reference-system normalization.
3. LiDAR elevation sampling.
4. Road/corridor snapping.
5. Building/terrain obstruction analysis.
6. Weather/visibility integration.
7. Infrastructure and backhaul verification.
8. Permission/aviation/environment/optical-safety review.
9. Field survey.
10. Engineering validation.

**Current gate status:** Steps 1–2 are implemented as the repository ingestion framework; the live source layers are confirmed, but individual feature extraction and field validation remain outstanding.
