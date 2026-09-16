# Cape Town FSO GIS Data Acquisition & Node Discovery v1.0

**Record:** BPU-NET-FSO-CPT-002  
**Status:** Data-acquisition specification  
**Date:** September 2026

## Objective

Move the Cape Town light-internet project from conceptual zones to reproducible geospatial screening using authoritative datasets. No rooftop or property is designated as a deployable node until the required datasets, line-of-sight analysis, permissions and safety reviews are completed.

## Primary municipal GIS source

The City of Cape Town Open Data Service exposes thematic GIS layers including topography, electricity/public lighting and a CCT Buildings feature layer. The service supports JSON/GeoJSON/PBF query formats and advanced queries for the buildings layer. citehttps://citymaps.capetown.gov.za/agsext/rest/services/Theme_Based/Open_Data_Service/MapServer/-1

## Required data layers

### Tier 1 — geographic structure
- CCT Buildings
- 5 m contours / elevation
- roads and access
- municipal boundaries
- public facilities and suitable institutional sites

### Tier 2 — infrastructure
- electricity supply/public-lighting layers
- existing fibre/backhaul information where lawfully available
- telecommunications infrastructure where public data exists
- candidate public/institutional structures

### Tier 3 — environmental
- visibility/fog observations
- wind speed/direction
- humidity
- rainfall
- cloud/fog frequency
- aerosol/coastal exposure where available

### Tier 4 — constraints
- aviation/airport restrictions
- heritage/environmental constraints
- property ownership/permission status
- public-safety and optical eye-safety requirements

## Node-discovery workflow

```text
CCT GIS layers
   ↓
Candidate structure extraction
   ↓
Height/elevation enrichment
   ↓
Neighbour-node search
   ↓
Distance calculation
   ↓
Terrain/building obstruction test
   ↓
Meteorological availability model
   ↓
Fibre/power/access enrichment
   ↓
Safety + aviation + environmental gates
   ↓
Multi-hop graph generation
   ↓
AI optimisation / digital twin
```

## Initial candidate corridors

The first computational pass should test corridors connecting the previously defined research zones rather than selecting individual buildings prematurely:

1. CBD/Foreshore ↔ Woodstock/Salt River/Observatory
2. Observatory/Rondebosch ↔ Newlands/Claremont
3. Claremont ↔ Bellville/Tyger Valley
4. Bellville ↔ Century City/Milnerton
5. Century City/Milnerton ↔ Paarden Eiland
6. Airport/logistics corridor as a controlled industrial branch
7. Later Stellenbosch/Winelands extension

## Candidate-node requirements

A candidate receives `SCREENING` status only when it has:

- unique node ID;
- coordinates;
- elevation/structure-height source;
- source-data timestamp;
- LOS result;
- candidate link distances;
- weather-data coverage;
- power assessment;
- backhaul assessment;
- maintenance/access assessment;
- permission status;
- aviation/environmental flags;
- safety review status.

Missing information is recorded as `UNKNOWN`, not inferred.

## FSO-specific modelling

Each candidate link should store:

- path length;
- terminal heights;
- terrain obstruction;
- building obstruction;
- expected visibility distribution;
- fog probability where data exists;
- wind exposure;
- rain/cloud effects where relevant;
- optical margin assumptions;
- fallback bearer;
- estimated availability;
- uncertainty interval.

The model should compare direct links against shorter multi-hop routes. This is particularly important for Cape Town because weather-dependent availability can change the value of a redundant mesh.

## Regulatory/resilience layer

The optical bearer and any RF fallback are treated separately. ICASA's current spectrum material includes location-specific registration/licensing requirements for radio systems and specifically identifies E-band light licensing for 73.375–75.875 GHz paired with 83.375–85.375 GHz. Any RF fallback must therefore be checked against the applicable South African spectrum framework rather than assumed licence-free. citehttps://www.icasa.org.za/pages/spectrum-licensing

## Output schema

The next dataset should produce machine-readable records equivalent to:

```text
NODE_ID
LATITUDE
LONGITUDE
ELEVATION_M
STRUCTURE_HEIGHT_M
LOS_STATUS
NEAREST_NODE_ID
LINK_DISTANCE_M
VISIBILITY_MODEL
WIND_MODEL
FIBRE_STATUS
POWER_STATUS
ACCESS_STATUS
PERMISSION_STATUS
AVIATION_STATUS
ENVIRONMENT_STATUS
SAFETY_STATUS
FALLBACK_STATUS
SCREENING_STATUS
SOURCE_IDS
DATA_TIMESTAMP
```

## Validation rule

The GIS screen is a **research filter**, not a construction approval. Any high-scoring candidate must still pass authoritative site survey, optical safety, structural, electrical, telecommunications/regulatory, property and environmental/aviation checks.

## Next execution gate

Populate the schema from authoritative GIS and environmental datasets, then generate a candidate-node graph for the first two corridors. Do not publish exact private addresses or treat public GIS coordinates as permission to install equipment.
