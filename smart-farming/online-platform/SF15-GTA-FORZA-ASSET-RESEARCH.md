# SF-15 — GTA V / Forza Asset Research and Rights-Clean Sandbox Basis

Date: 2026-09-18

## Objective
Extend the SF-14 rights audit to GTA V Nexus Mods and Forza-related resources. The purpose is to learn from large open-world environments, vehicle presentation, road systems, traffic, handling, materials, lighting and world streaming — not to copy proprietary game assets into the commercial Biupiu World.

## GTA V Nexus findings
Nexus contains large vehicle packs and visual/world overhauls, but the checked vehicle packs generally restrict asset use, conversion, redistribution or commercial use. Examples checked include Ultimative 4K Vehicle Pack, Ultimative Luxury Car Pack, CARPACK 50CARS and Mega Addon Car Pack. citeturn0search0turn0search1turn0search2turn0search9

Useful research categories:
- large vehicle libraries and class taxonomy
- traffic density and population systems
- road/intersection layouts
- weather, lighting and visual-overhaul techniques
- city/rural/industrial environment composition
- vehicle handling concepts
- streaming/performance approaches
- map/world modularity

GTA V assets themselves remain third-party/proprietary and are **not approved production assets** for Biupiu.

## Forza findings
ForzaTech Studio documents tooling for viewing/editing/converting Forza Motorsport and Forza Horizon game files, but explicitly describes asset extraction as for personal modding/research and warns that modifying game files may violate game terms. citeturn0search12turn0search15

Therefore:
- Forza game car meshes/textures/materials: RESEARCH-ONLY.
- Extracted Forza assets: DO NOT import into the commercial Biupiu runtime.
- Forza handling/presentation concepts: MAY INFORM original Biupiu vehicle specifications.
- Original/licensed third-party vehicle assets: MAY be evaluated separately under the asset licence register.

## Sandbox design basis
Create an original Biupiu sandbox using the following design references:
1. Open-world streaming and district zoning.
2. Modular road, terrain, vegetation and architecture kits.
3. Vehicle classes: passenger, utility, agricultural, emergency, logistics, marine and experimental.
4. PBR materials with LOD tiers.
5. Traffic and pedestrian simulation using original data.
6. Day/night and weather systems.
7. Garage/showroom/marketplace presentation.
8. Physics parameter abstraction rather than copied game physics.
9. Facility-linked vehicles: farms, labs, workshops, research campuses and ports.
10. Research/reconstruction environments clearly labelled by evidence level.

## Rights gate
Every third-party asset lot must record:
- source
- creator
- exact asset
- licence
- commercial-use status
- redistribution status
- modification/conversion status
- dependencies
- attribution
- evidence URL
- approval state

No asset is production-approved merely because it is downloadable.
