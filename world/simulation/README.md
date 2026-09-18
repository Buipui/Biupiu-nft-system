# Biupiu World — Civilisation Farming Simulation

This layer turns the civilisation site specifications into reproducible simulation assets.

## Design contract
1. Preserve each civilisation's terrain, water system, materials, settlement pattern and agricultural geometry.
2. Separate archaeological evidence from reconstruction.
3. Every site carries evidence metadata and a reconstruction flag.
4. Simulation values are game/education parameters, not claims about historical yields.
5. Barter and treasury interfaces use virtual units only.

## Current sites
- Inka mountain terraces + Moray research zone.
- Maya lowland milpa/terrace/wetland scenarios.
- Babylonian alluvial irrigation.
- Hanging Gardens reconstruction scenario, explicitly labelled uncertain.

## Next implementation layer
A future 3D client can consume the JSON site configs, instantiate terrain/structures, run the farming engine, and expose evidence cards before players enter reconstructed mechanics.
