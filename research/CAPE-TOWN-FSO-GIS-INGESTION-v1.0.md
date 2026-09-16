# Cape Town FSO GIS Ingestion v1.0

**Status:** Executed research pipeline stage  
**Date:** 16 September 2026  
**Record:** BPU-NET-FSO-CPT-GIS-INGEST-001

## What was executed

The repository now contains a deterministic adapter for converting validated City of Cape Town ArcGIS feature responses into candidate FSO nodes.

The adapter:

1. accepts ArcGIS feature JSON;
2. restricts automatic candidate extraction to public/institutional usage classes;
3. preserves the municipal source layer and object ID;
4. preserves coarse locality metadata where supplied;
5. records permission, safety, aviation, environment, height and LOS as unresolved rather than inferring them;
6. excludes features without geometry;
7. deliberately does not copy street-address text into the graph payload.

## Candidate classes

The first extraction layer supports municipal/public classes including offices, fire stations, libraries, halls, clinics, depots, law-enforcement facilities, reservoirs, sports facilities, traffic departments, workshops and community facilities.

This is a **candidate-node filter**, not a deployment recommendation.

## Graph integration

The output is compatible with `codex/gis/cpt_fso_graph.py` and can subsequently feed:

`candidate nodes → candidate edges → terrain/building LOS → weather/visibility → link budget → power/backhaul → permission/aviation/safety/environment → AI routing → digital twin`

## Evidence status

City GIS establishes the spatial source record. It does not establish ownership/permission, structural capacity, optical safety, aviation clearance, RF authorisation, atmospheric availability or deployability.

The municipal GIS service provides machine-queryable building and topographic layers; current research records therefore treat the GIS service as the authoritative spatial input and retain source IDs for reproducibility.

## Privacy / precision control

The graph layer is intentionally designed around public/institutional assets and source object IDs. Exact private addresses are not promoted into the candidate graph merely because they appear in GIS data.

## Next gate

Run the adapter against an archived, validated ArcGIS response for the CCT Buildings layer, then perform corridor filtering for the two initial research corridors. Only after that should terrain/building obstruction and atmospheric availability modelling be attached to edges.
