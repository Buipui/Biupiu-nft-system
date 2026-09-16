# Cape Town FSO GIS Findings v1.0

**Date:** 16 September 2026  
**Status:** Research / data-acquisition stage  
**Record:** BPU-NET-FSO-CPT-GIS-001

## 1. Purpose

This record converts the Cape Town light-internet concept into a reproducible GIS evidence layer using authoritative City of Cape Town spatial services. It does **not** approve, rank, or designate installation sites.

## 2. Authoritative municipal GIS findings

The City of Cape Town Open Data Service exposes ArcGIS REST services with machine-queryable spatial layers. The current service inventory includes:

- **CCT Buildings (Layer 135)** — municipal building locations represented as point features; the service supports JSON/GeoJSON/PBF queries and advanced queries.
- **5m Contours (Layer 15)** — topographic contour lines at 5 m intervals.
- **Ground Level Map 2m Contours (Layer 161)** — additional topographic resolution available in the municipal service.
- **Electricity / public-lighting layers** — available under the Basic Services & Infrastructure group.
- Community-service layers include municipal facilities such as libraries, schools and other public/institutional locations that may be relevant to permission-led pilot research.

The municipal service documents the CCT Buildings dataset as locations of City of Cape Town buildings, including offices, clinics, depots, fire stations, halls, law-enforcement facilities, libraries, pools, reservoirs, sports facilities, traffic departments and workshops. This makes the municipal layer particularly useful for identifying public/institutional candidate classes without treating private property as automatically available.

## 3. New topographic evidence

A current City Maps 5 m contour service states that its contours were derived from LiDAR captured between November 2024 and March 2025, with a stated point-cloud density of 15 points/m² and vertical accuracy of 0.1 m at 95%. The contours are derived from a 5 m DTM and use the South African Land Levelling Datum.

These properties make the dataset suitable as a **screening input** for terrain-aware link modelling, subject to checking the exact dataset version, coordinate transformation and local conditions before engineering use.

## 4. Candidate-node acquisition rule

The first implementation should prioritise public/institutional structures and municipal assets rather than private addresses. Each candidate record must retain:

`NODE_ID, SOURCE_LAYER, SOURCE_OBJECT_ID, NODE_CLASS, LATITUDE, LONGITUDE, ELEVATION_SOURCE, STRUCTURE_HEIGHT_SOURCE, ACCESS_STATUS, PERMISSION_STATUS, AVIATION_STATUS, ENVIRONMENT_STATUS, SAFETY_STATUS, BACKHAUL_STATUS, POWER_STATUS, WEATHER_STATUS, SOURCE_TIMESTAMP, SCREENING_STATUS`

No candidate becomes a deployable node until permissions, optical safety, aviation/airspace, structural, environmental and network engineering checks are complete.

## 5. Corridor graph construction

The first two research corridors remain:

1. CBD/Foreshore ↔ Woodstock/Salt River/Observatory
2. Observatory/Rondebosch ↔ Newlands/Claremont

The GIS pipeline is:

`municipal candidate layers → public/institutional candidate extraction → coordinate/elevation normalisation → neighbour search → path-distance calculation → terrain/building obstruction model → weather/visibility model → fibre/power/access checks → safety/aviation/environment gates → multi-hop graph → AI/digital twin`

At this stage, the repository records the **data sources and graph rules**, not a fabricated list of deployable rooftops or links.

## 6. Optical/RF regulatory cross-link

ICASA's current Spectrum Licensing material documents the South African E-band light-licensing regime for 73.375–75.875 GHz paired with 83.375–85.375 GHz. Station location and characteristics are recorded in a reference RF database, with users responsible for coordination and compatibility with registered stations.

This is relevant only to an RF/E-band fallback or hybrid bearer. Optical free-space links and RF spectrum authorisation remain distinct engineering/regulatory layers.

## 7. AI / digital-twin inputs added

The GIS layer now feeds the planned AI/digital-twin system with:

- node coordinates and source IDs;
- terrain/elevation evidence;
- public/institutional asset class;
- candidate-link geometry;
- distance and obstruction indicators;
- power/backhaul availability status;
- weather/visibility coverage status;
- permission and regulatory gates;
- uncertainty and data timestamp.

AI outputs must remain decision-support signals. Safety, legal, aviation and deployment gates remain deterministic human/authoritative checks.

## 8. Evidence boundary

Municipal GIS data establishes spatial information and dataset provenance. It does not establish ownership permission, structural capacity, optical safety, telecommunications authorisation, or guaranteed atmospheric availability. Those remain separate validation layers.

**Next gate:** build the machine-readable candidate-node graph from public/institutional GIS features for the first two corridors, then connect it to the deterministic `cpt_fso_site_screen.py` pipeline and test graph construction before any physical-site recommendation.

## Sources

- City of Cape Town Open Data Service / ArcGIS REST layers: CCT Buildings, 5m Contours, electricity/public lighting and community-service datasets.
- City of Cape Town current 5m contour metadata and LiDAR-derived DTM description.
- ICASA Spectrum Licensing and E-band operating procedure material.
