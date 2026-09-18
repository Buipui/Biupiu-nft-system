# Biupiu R&D Research Index

**Version:** 3.1  
**Updated:** 18 September 2026  
**Repository:** Biupiu NFT / computational-art / personal R&D portfolio

## Mobile application layer

**Biupiu R&D OS Mobile v0.7 foundation added.**

`software/rnd-os-mobile/` contains the Android application foundation. `software/rnd-os-mobile/MOBILE-ARCHITECTURE-v0.7.md` defines the mobile architecture.

The mobile client is separated from the R&D OS core. It consumes the API rather than accessing PostgreSQL directly and inherits server-side authentication, tenant scope, evidence rules and audit controls.

Initial Android foundation: Kotlin, Jetpack Compose, Navigation Compose, Android API 26+ baseline, dashboard shell, Research Objects navigation, Experimental Control Centre navigation and an API abstraction layer.

**Mobile status:** development foundation only. API authentication integration, offline persistence, evidence capture, automated Android tests, production security review and store-release work remain future gates.

## Research & Innovation Centre OS
`research/BIUPIU-RESEARCH-INNOVATION-CENTRE-OS-v1.0.md` is now the centre-level architecture. It turns the repository into an integrated research, experimentation, simulation, engineering, innovation and technology-development operating system around the existing Experimental Control Centre.

### Commercial software product layer
`research/BIUPIU-R&D-OS-SOFTWARE-ARCHITECTURE-v1.0.md` defines the proposed licensable Biupiu R&D OS as a separate commercial software product built from the repository's research methodology and validated against the repository as a reference environment.

The proposed product lifecycle is:
`PROJECT → RESEARCH OBJECT → SOURCE → CLAIM → HYPOTHESIS → MODEL → SIMULATION → EXPERIMENT → DATASET → RESULT → REPLICATION → TECHNOLOGY READINESS → IP → PROTOTYPE → PRODUCT / LICENCE`.

The commercial architecture covers research-object management, evidence control, Experimental Control Centre workflows, AI research intelligence, automated experiment generation, virtual-lab connectors, Materials Genome, Technology Combination Engine, Knowledge Graph, failure/lessons, IP Firewall, digital twin/digital factory interfaces, innovation portfolio management, APIs, tenancy, auditability, deployment and licensing editions.

**Commercialisation status:** architecture defined; commercial validation not yet established; production SaaS not yet built or launched. The software concept must be validated through MVP testing, real research workflows, customer discovery and willingness-to-pay evidence before commercial claims are made.

### R&D OS v0.2 implementation layer
`software/rnd-os/` now contains the executable v0.2 development foundation. It includes a JSON storage abstraction, PostgreSQL-ready relational schema, relationship and lineage APIs, lifecycle transition validation, integrity-checked research package export/import validation, non-production role/auth primitives, expanded automated tests and a GitHub Actions Node 20 CI workflow.

The current runtime remains intentionally local/development-only. PostgreSQL is modelled but not connected; authentication is scaffolding rather than production identity/security; package import validates without overwriting the datastore. These boundaries prevent prototype capabilities from being represented as production-grade systems.

Core centre systems now include:
- `BIUPIU-INTELLIGENCE-LAYER-v1.0.md` — evidence-aware research intelligence and next-test queries.
- `BIUPIU-AUTOMATED-EXPERIMENT-GENERATOR-v1.0.md` — claim/hypothesis to structured experiment pipeline.
- `BIUPIU-VIRTUAL-LAB-v1.0.md` — CFD, FEA/FEM, thermal, electromagnetic, optical, agricultural, energy, robotics and manufacturing simulation domains.
- `BIUPIU-MATERIALS-GENOME-v1.0.md` — searchable material composition, properties, processing, testing and application registry.
- `BIUPIU-TECHNOLOGY-COMBINATION-ENGINE-v1.0.md` — cross-department technology-combination and hypothesis generation.
- `BIUPIU-TECHNOLOGY-READINESS-EVIDENCE-ENGINE-v1.0.md` — evidence-state and R0–R9 maturity tracking.
- `BIUPIU-FAILURE-LESSONS-REGISTER-v1.0.md` — searchable negative, failed and inconclusive result archive.
- `BIUPIU-KNOWLEDGE-GRAPH-v1.0.md` — source-to-product relationship graph.
- `BIUPIU-DIGITAL-FACTORY-v1.0.md` — future manufacturing, robotics, machine vision and digital-factory architecture.
- `BIUPIU-LIVING-SYSTEMS-LAB-v1.0.md` — regenerative agriculture and biological systems experimentation architecture.
- `BIUPIU-IP-FIREWALL-v1.0.md` — public/internal/confidential/pre-patent/IP control states.
- `BIUPIU-FORESIGHT-CENTRE-v1.0.md` — scientific, patent, standards, university, manufacturing and emerging-technology monitoring.
- `BIUPIU-INVENTION-INCUBATOR-v1.0.md` — discovery-to-product invention lifecycle.
- `BIUPIU-EXTERNAL-COLLABORATION-LAYER-v1.0.md` — structured university, laboratory, engineering, manufacturing, investor and government collaboration records.

The Experimental Control Centre remains the execution orchestration layer: `SOURCE → CLAIM → HYPOTHESIS → MODEL → SIMULATION → EXPERIMENT → MEASUREMENT → VALIDATION → REPLICATION → IP/PRODUCT PATH`.

## Master evidence architecture
`research/BIUPIU-EVIDENCE-LAYER-ARCHITECTURE.md` is the master source-control architecture. Core layers are: primary archaeology/history; JSTOR; AnthroSource; ResearchGate/scientific literature; Emerald Insight; controlled speculative/hypothesis sources; ancient texts; scientific primary data; patents/prior art; public/declassified technical archives; GitHub/BIUPIU CODEX; computational validation; and physical/experimental validation.

**Core doctrine:** No idea is rejected merely because it is unconventional. No idea is accepted merely because it is fascinating. Every important claim becomes a testable research object.

## Permanent research operating protocol
`research/BIUPIU-RESEARCH-OPERATING-PROTOCOL-v2.0.md` is the default workflow. `research/SOURCE-TO-DEPARTMENT-CROSSWALK.md` routes each source layer into relevant Biupiu departments.

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
- `BITCHUTE-ENG` / `ENG-VALIDATION` / `PROTOTYPE-QUEUE` — BitChute source discovery, engineering claim validation, patents/prior art, creator/licensing records and controlled physical validation.
- `VIDEO-SERIES` / `SPEC-VIDEO` — original Biupiu engineering-validation video production, episode evidence notes, media-rights checks and build-log documentation.

## Centre integration rule
All existing department streams remain active. New centre systems are overlays that route existing research into intelligence, experiments, simulations, materials, combinations, failures, IP, manufacturing, living systems, foresight, collaboration and invention pathways rather than replacing the underlying research streams.

## Repository status
- Research & Innovation Centre OS v1.0 added.
- **Biupiu R&D OS Software Architecture v1.0 added as the commercial software product specification/reference layer.**
- **Biupiu R&D OS executable v0.2 development layer added.**
- Experimental Control Centre remains active as the execution layer.
- Intelligence, automated experiment generation, Virtual Lab, Materials Genome, Technology Combination Engine, Technology Readiness/Evidence Engine, Failure/Lessons Register, Knowledge Graph, Digital Factory, Living Systems Lab, IP Firewall, Foresight Centre, Invention Incubator and External Collaboration Layer added.
- ORIGIN-001 remains a prototype and is **NOT MINTED**.
- `BIU-ALG-GEO-FLOW-001@0.1.0` remains the first registered algorithm family/version.
- Complex-geometry execution remains active with deterministic primitives and tests.
- Cape Town FSO/light-internet architecture and pilot-test plan are indexed.
- Cape Town FSO preliminary site-screening CODEX implementation and deterministic tests have been added.
- Authoritative municipal GIS acquisition and first findings are indexed.
- Network graph algorithm family remains framework-level until executable graph construction, authoritative-data validation and physical validation exist.
- `BiupiuResearchRegistry.sol` is a prototype contract and is not represented as production-deployed.
- No production blockchain deployment or live NFT mint is recorded.
- Artwork generation remains paused until explicitly requested.

## Version

**Biupiu R&D Research Index v3.0 — Executable R&D OS v0.2 Integration**  
**Updated:** 18 September 2026


## Department subscriber products

The repository now defines a shared department-scoped subscriber model and two specialist product architectures:

- `research/BIUPIU-DEPARTMENT-SUBSCRIBER-ACCESS-CONTROL-v1.0.md` — common tenant, entitlement, role, visibility, audit and information-firewall model.
- `research/BIUPIU-SMART-METAL-WORKSHOP-v1.0.md` — METALLURGY-only smart home-workshop product for hobbyist metalworkers.
- `research/BIUPIU-SMART-FARMING-v1.0.md` — FARMING-only smart farming product.

Both products use the same subscriber/identity architecture while enforcing department-scoped search, AI retrieval, exports and resource access. A subscriber can hold multiple explicit department entitlements, but no department access is implied by another entitlement.


## Cultural heritage department environments

Added culturally contextualised specialist spaces:
- `research/BIUPIU-TEXTILES-CULTURAL-HERITAGE-SPACE-v1.0.md` — TEXTILES environments and Global Fibre Innovation Lab.
- `research/BIUPIU-MATERIALS-CULTURAL-HERITAGE-SPACE-v1.0.md` — MATERIALS environments and Advanced Materials Laboratory.
- `research/BIUPIU-CULTURAL-HERITAGE-ENVIRONMENT-MATRIX-v1.0.md` — cross-department navigation and evidence rules.

The main hub routes users through their subscribed department before exposing its cultural environments and specialist workspaces. Historical context and modern experiments remain separately classified.
