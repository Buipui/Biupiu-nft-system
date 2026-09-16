# Biupiu R&D Research Index

**Version:** 2.6  
**Updated:** 16 September 2026  
**Repository:** Biupiu NFT / computational-art / personal R&D portfolio

## Master evidence architecture
`research/BIUPIU-EVIDENCE-LAYER-ARCHITECTURE.md` is the master source-control architecture. Core layers are: primary archaeology/history; JSTOR; AnthroSource; ResearchGate/scientific literature; Emerald Insight; controlled speculative/hypothesis sources; ancient texts; scientific primary data; patents/prior art; public/declassified technical archives; GitHub/BIUPIU CODEX; computational validation; and physical/experimental validation.

**Core doctrine:** No idea is rejected merely because it is unconventional. No idea is accepted merely because it is fascinating. Every important claim becomes a testable research object.

## Permanent research operating protocol
`research/BIUPIU-RESEARCH-OPERATING-PROTOCOL-v2.0.md` is the default workflow. `research/SOURCE-TO-DEPARTMENT-CROSSWALK.md` routes each source layer into relevant Biupiu departments.

## Repository boundary
This is the personal Biupiu computational-art, invention, speculative-research and R&D/IP track. It remains separate from the immediate commercial DTIC/InvestSA library unless explicitly transferred.

## Master indexed streams
- `BIO` / `BIO-GEN` — biotechnology, botany, plant science, genetics and seed breeding.
- `AGRI` — regenerative agriculture, soil systems, agroecology and ancient agriculture.
- `HEMP` — industrial hemp cultivation, fibre, biomass and processing.
- `BIOCARBON` / `BIOCHEM` — biochar, activated carbon, carbon materials, pyrolysis and biomass fractionation.
- `TEXTILES` / `COAT` / `COMPOSITES` — fibres, textiles, nonwovens, adhesives, coatings and natural-fibre composites.
- `MATERIALS` — ceramics, metallurgy, SiC and advanced multifunctional materials.
- `WATER` — springs, hydrology, filtration, irrigation and water-energy conversion.
- `ENERGY` / `ELECTROMAG` — turbines, generators, energy storage, electrical and electromagnetic engineering.
- `PHOTONICS` / `PH-QPM` / `CRM` — FSO, LiFi/VLC, structured light, holography, quantitative phase, crystals and quantum/photonic materials.
- `FSO-CPT` / `LIGHT-NET` — Cape Town light-based internet, terrestrial FSO mesh, VLC/LiFi edge access, hybrid optical/RF/fibre resilience and GIS site screening.
- `MM` / `MM-NASA` — metamaterials/metasurfaces and NASA/public technical cross-reference.
- `AERO` / `STEALTH-GEO` — public-source aerospace, aerodynamics, SR-71/stealth geometry and lightweight mobility.
- `MARINE` — propellers, pumpjets, hydrofoils, hulls and marine turbines.
- `CG-3D` / `GEOMETRY` — parametric geometry, topology, CAD, reconstruction and optimisation; extended by `research/BIUPIU-COMPLEX-GEOMETRY-THUNDERBOLTS-CODEX-v1.0.md`.
- `CODEX` / `COMPUTE` — Python, CFD, FEA/FEM, multiphysics, algorithms, data and reproducible computational engineering.
- `AI` — machine learning, surrogate models, generative engineering and optimisation; now linked to optical link-quality prediction, adaptive routing and GIS-derived digital-twin inputs.
- `DIGITAL-TWIN` — physical systems, sensor data, models and optimisation loops; now includes municipal GIS/elevation inputs for the planned Cape Town FSO network twin.
- `ROBOTICS` / `ADV-MFG` — automation, robotics, machine vision, additive/digital manufacturing and manufacturing constraints.
- `BIOMED` — biomedical and life-science technology R&D.
- `AAT` / `AAT-H` — Ancient Applied Technology and anthropology/human-material systems.
- `GEOARCH` / `LAND-GIS` / `ALA` — geoarchaeology, historical GIS and Ancient Landscape Atlas.
- `PALAEO` / `COAST` — palaeogeography, ancient coastlines and submerged landscapes.
- `EMPIRE` / `CULTURE` — ancient political geography and comparative culture/technology.
- `NAGA` / `HIM` / `UNDERGROUND` — Naga, Himalayan and subterranean research.
- `GEO-MAG` / `SACRED-GRID` — geomagnetics, archaeomagnetism and statistical alignment testing.
- `FAILURE` / `ALA-PRE-DISASTER` — engineering, agricultural, water and civilisational failure/pre-disaster atlas.
- `IP-PA` / `IP` / `DECLASS` — patents, prior art, licensing, FTO and public/declassified engineering records.
- `SPEC` / `SPEC-VIDEO` / `SPEC-SEP` / `SPEC-CONVERGENCE` — controlled speculative-source research, including Thunderbolts Project material as hypothesis/inspiration only.
- `JSTOR` / `ANTHROSOURCE` / `RG` / `EMERALD` / `PRIMARY` / `TEXTS` — transversal evidence-source layers.
- `NFT-IP` / `NFT-CF` / `NFT-ATH-GEO` / `NFT-GEN` / `NFT-PROV` / `NFT-ARCH` / `NFT-ORIGIN` — research-to-art, crowdfunding, generative art, provenance and NFT architecture.
- `NFT-WEB3` / `NFT-MINT` / `NFT-EVM` — smart contracts, Web3 tooling, deployment, minting, token URI management and blockchain provenance.
- `NFT-ALG` / `NFT-GRAPH` / `NFT-REGISTRY` — company algorithm families, semantic version lineage, machine-readable algorithm graph, release commitments and blockchain registry architecture.

## Cape Town light-internet / AI-assisted FSO stream
`research/CAPE-TOWN-LIGHT-INTERNET-AI-FSO-NETWORK-v1.0.md` remains the master architecture. `research/CAPE-TOWN-FSO-GIS-DATA-ACQUISITION-v1.0.md` defines the authoritative-data acquisition workflow, while `research/CAPE-TOWN-FSO-GIS-FINDINGS-v1.0.md` records the current GIS evidence findings.

New findings establish that the City of Cape Town Open Data Service exposes machine-queryable municipal layers including **CCT Buildings**, **5m Contours**, additional 2m ground-level contours, electricity/public-lighting infrastructure and community/public-facility datasets. Current municipal metadata also documents a LiDAR-derived 5m contour/DTM product based on 2024–2025 capture, providing a stronger topographic screening input than an unverified conceptual map. These datasets are research inputs only; they do not establish ownership, permission, structural capacity or deployment approval.

The first graph-construction corridors remain CBD/Foreshore ↔ Woodstock/Salt River/Observatory and Observatory/Rondebosch ↔ Newlands/Claremont. The next implementation gate is a public/institutional candidate-node graph with source object IDs, elevation evidence, link geometry, obstruction status, infrastructure status, weather coverage and regulatory/safety gates. No private address is to be treated as a deployable node merely because it appears in public GIS.

## Regulatory and hybrid-network cross-link
The network architecture now explicitly separates optical FSO from RF fallback. ICASA's current spectrum material documents an E-band light-licensing regime covering 73.375–75.875 GHz paired with 83.375–85.375 GHz, with location/characteristic registration and coordination requirements. This is relevant to a hybrid optical/RF resilience layer; it does not constitute authorisation to deploy any Biupiu network.

## CODEX network implementation
`codex/gis/cpt_fso_site_screen.py` provides deterministic preliminary site/link screening. Associated tests are `codex/gis/test_cpt_fso_site_screen.py`.

Next CODEX work: implement a machine-readable candidate-node/edge graph using authoritative public/institutional GIS objects, then test graph construction before connecting it to AI routing and the digital twin. Planned optical/network modules include FSO channel modelling, structured-light encoding, turbulence eigenmodes, topological encoding, FSO mesh routing, hybrid optical/RF routing, AI link-quality prediction, route optimisation and Cape Town digital-twin modelling.

## Wits optical research integration
The FSO stream cross-links Wits research on long-range FSO, VLC/LiFi, structured light, atmospheric turbulence, turbulence eigenmodes, topological/skyrmion encoding and AI-assisted optical-channel adaptation. These sources inform engineering hypotheses and test design; they do not by themselves establish Cape Town deployment feasibility.

## Metamaterials cross-link
`MM → metasurface wavefront control → beam steering/phase control → structured light → FSO channel → AI optimisation` remains an explicit cross-disciplinary pathway. MM remains a separate research branch with its source cross-link register and NASA/ResearchGate/Emerald/patent/declassified evidence layers.

## Complex geometry / Thunderbolts-inspired CODEX stream
`research/BIUPIU-COMPLEX-GEOMETRY-THUNDERBOLTS-CODEX-v1.0.md` remains the dedicated mathematical/computational reference for toroidal, nested, spiral, helical, braided, vortex, hourglass, wave-superposition, knot and related geometry families. Thunderbolts material remains source/inspiration and controlled hypothesis material only.

## Company algorithm network
`research/BIUPIU-COMPANY-ALGORITHM-NETWORK-v1.0.md` defines the active computational company-network architecture.

### Canonical lineage
`RESEARCH ID → ALGORITHM FAMILY/VERSION → PARAMETERS + SEED → ARTWORK RELEASE → RELEASE MANIFEST → HASHES → BLOCKCHAIN RECORD`

### Proposed network families
- `BIU-ALG-FSO-CPT-001` — Cape Town optical-site screening and candidate-link generation.
- `BIU-ALG-FSO-CHAN-001` — atmospheric optical-channel modelling.
- `BIU-ALG-FSO-AI-001` — AI link-quality prediction/adaptive routing.
- `BIU-ALG-FSO-TWIN-001` — digital-twin calibration against measured network telemetry.
- `BIU-ALG-FSO-GRAPH-001` — authoritative GIS candidate-node/edge graph construction; framework registration pending executable implementation and tests.

These remain framework registrations until validated against authoritative datasets and physical measurements.

## Cross-disciplinary integration
`ENERGY ↔ ELECTROMAG ↔ PHOTONICS ↔ FSO-CPT ↔ CRM ↔ MM ↔ GEOMETRY ↔ CODEX`

`PHOTONICS ↔ STRUCTURED-LIGHT ↔ TURBULENCE ↔ AI ↔ DIGITAL-TWIN ↔ FSO-CPT ↔ LAND-GIS`

`COMPUTE ↔ AI ↔ GEOMETRY ↔ DIGITAL-TWIN ↔ ROBOTICS ↔ ADV-MFG`

`AERO ↔ MARINE ↔ MATERIALS ↔ COMPOSITES ↔ GEOMETRY ↔ COMPUTE ↔ AI`

`SPEC-VIDEO ↔ GEOMETRY/CODEX ↔ ELECTROMAG/PHOTONICS ↔ controlled hypothesis testing`

`NFT-ALG ↔ GEOMETRY ↔ CODEX/COMPUTE ↔ AI ↔ DIGITAL-TWIN ↔ NFT-GEN ↔ NFT-PROV ↔ NFT-EVM`

## Repository status
- ORIGIN-001 remains a prototype and is **NOT MINTED**.
- `BIU-ALG-GEO-FLOW-001@0.1.0` remains the first registered algorithm family/version.
- Complex-geometry execution remains active with deterministic primitives and tests.
- Cape Town FSO/light-internet architecture and pilot-test plan are indexed.
- Cape Town FSO preliminary site-screening CODEX implementation and deterministic tests have been added.
- Authoritative municipal GIS acquisition and first findings are now indexed.
- Network graph algorithm family is framework-level until executable graph construction, authoritative-data validation and physical validation exist.
- `BiupiuResearchRegistry.sol` is a prototype contract and is not represented as production-deployed.
- No production blockchain deployment or live NFT mint is recorded.
- Artwork generation remains paused until explicitly requested.
