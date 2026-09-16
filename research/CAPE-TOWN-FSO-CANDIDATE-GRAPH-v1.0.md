# Cape Town FSO Candidate Graph v1.0

**Status:** Research-screening graph specification  
**Record:** BPU-NET-FSO-CPT-GRAPH-001  
**Date:** 16 September 2026

## Purpose

This record defines the first machine-readable graph layer for the Cape Town light-internet research programme. It connects validated public/institutional GIS observations into candidate optical links.

## Initial corridors

**Corridor A:** CBD/Foreshore ↔ Woodstock/Salt River/Observatory  
**Corridor B:** Observatory/Rondebosch ↔ Newlands/Claremont

These are investigation corridors, not deployment recommendations.

## Graph model

- **Node:** public/institutional or otherwise permission-verified structure/asset with authoritative coordinates and source ID.
- **Edge:** preliminary geometric link generated when node separation is within the configured screening distance.
- **Edge status:** `screening` until terrain/building LOS, atmospheric availability, infrastructure, permission, aviation and safety gates are resolved.

## CODEX implementation

`codex/gis/cpt_fso_graph.py` now provides:

- deterministic node representation;
- preliminary local planar distance calculation;
- deterministic candidate-edge generation;
- serialisable graph output;
- explicit validation gates.

`codex/gis/test_cpt_fso_graph.py` provides deterministic tests for symmetry, distance gating, ordering and validation metadata.

## Data discipline

The graph does **not** contain invented rooftop coordinates, private addresses or assumed permissions. Candidate records must originate from authoritative GIS observations and preserve source IDs and timestamps.

The City of Cape Town municipal GIS service provides relevant building, topographic and infrastructure layers for this acquisition workflow. The current research record treats those datasets as spatial evidence, not as permission to install equipment.

## Required edge validation

Before an edge can advance beyond screening:

1. authoritative coordinate validation;
2. terrain/elevation analysis;
3. building obstruction / LOS analysis;
4. terminal-height verification;
5. weather and visibility statistics;
6. optical link-budget modelling;
7. power and backhaul availability;
8. access and property permission;
9. aviation/airspace review;
10. optical eye-safety assessment;
11. environmental/heritage constraints;
12. structural and mounting assessment;
13. RF fallback/licensing review where an RF bearer is proposed.

## AI / digital-twin integration

Once validated observations are available, the graph becomes an input to:

`GIS → graph → FSO channel model → weather/visibility model → AI link-quality model → hybrid route optimisation → digital twin`

AI may predict link quality or propose routing alternatives, but deterministic safety, legal, aviation and permission gates remain outside autonomous optimisation.

## Evidence status

**Current status:** plausible computational infrastructure with authoritative-data acquisition underway. No physical network deployment, site approval, measured optical performance or guaranteed availability is claimed.
