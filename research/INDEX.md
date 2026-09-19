# Biupiu R&D Research Index

**Version:** 3.3  
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

## Physical Test Data + Material Calibration

Added `research/BIUPIU-PHYSICAL-TEST-DATA-SCHEMA-v1.0.json` and `research/BIUPIU-MATERIAL-CALIBRATION-LOOP-v1.0.md`; **GATE BM-06 executed**. Physical coupon, adhesive, laminate and rotating-subassembly results now have a traceable route into the Digital Twin while preserving raw data, uncertainty, conditioning, batch provenance and independent validation data.

## Blade Baseline Dataset + Comparison Workflow

Added `research/BIUPIU-BLADE-BASELINE-DATASET-v1.0.json` and `research/BIUPIU-BLADE-COMPARISON-WORKFLOW-v1.0.md`; **GATE BM-05 executed**. The baseline dataset contains the common candidate families, load-case definitions, required material properties and result fields. Unknown properties remain null rather than being invented.

## Blade Simulation Runner + Result Schema

Added `research/BIUPIU-BLADE-SIMULATION-RUNNER-SPEC-v1.0.md` and `research/BIUPIU-BLADE-RESULT-RECORD-SCHEMA-v1.0.json`; **GATE BM-04 executed**. The runner specification enforces identical geometry/load cases across candidate fibre/resin systems and requires provenance, model version, boundary conditions, uncertainty and evidence state for every result.

## Resin Formulation + Blade Twin Integration

Added `research/BIUPIU-RESIN-FORMULATION-SCHEMA-v1.0.json` and `research/BIUPIU-RESIN-BLADE-TWIN-SCHEMA-v1.0.md`; **GATE BM-03 executed**. Resin chemistry, cure state, fibre treatment, interface properties and laminate data are now defined as machine-readable inputs to the Blade Digital Twin. The comparison runner must preserve uncertainty and never silently substitute missing material properties.

## Bio-Adhesive and Resin Genome

Added `research/BIUPIU-BIO-ADHESIVE-RESIN-GENOME-v1.0.md` and opened **GATE BM-02**. The new matrix covers partly bio-based epoxies, plant-oil epoxies, lignin-modified and lignin-curing systems, cardanol, vanillin/eugenol, furan, tannin/polyphenol and rosin-derived resin/adhesive families. It links resin chemistry, fibre treatment, interface performance, manufacturing and ageing to the existing Blade Material Genome and Digital Twin.

ResearchGate evidence is routed into the formulation and blade tracks; Emerald Insight remains a complementary source layer for natural-fibre processing, sustainability and implementation. Literature values remain source-specific and are not treated as Biupiu design allowables.

## Blade Material Genome and qualification gate

Added `research/BIUPIU-BLADE-MATERIAL-GENOME-v1.0.md` and opened **GATE BM-01**. The genome establishes a common qualification matrix for hemp/epoxy, flax/epoxy, hemp/flax/epoxy, hemp/flax/basalt/epoxy and secondary plant composites. Literature observations remain source-specific and cannot substitute for Biupiu-tested allowables.

The next executable stage is the common Blade Digital Twin parameter schema and simulation runner, using identical geometry/load cases across material candidates.

## Plant-based composites and blade materials

Added `research/BIUPIU-PLANT-BASED-BLADE-MATERIALS-v1.0.md` for plant-fibre blade selection and evidence-controlled micro-turbine materials research. Hemp and flax are primary plant-fibre candidates for stiffness-driven composite blade regions; basalt is retained as a non-plant hybrid reinforcement for high-load zones.

Added `research/BIUPIU-PLANT-FUNCTIONAL-ALLOCATION-REGISTRY-v1.0.md`, allocating plant species/feedstocks to HEMP, TEXTILES, COMPOSITES, MATERIALS, ENERGY, AERO, MARINE, AGRI, WATER, BIOCARBON, BIOCHEM, BIOMED, ROBOTICS/ADV-MFG and AI/COMPUTE by measurable functionality.

Added `research/BIUPIU-BIO-COMPOSITE-DIGITAL-TWIN-v1.0.md`, linking plant → fibre → laminate → blade/component → system with CFD/FEA, sensor data, manufacturing parameters and evidence states.

### Plant-composite evidence bundle
ResearchGate and Emerald Insight evidence is routed through `RG` and `EMERALD`. Current evidence supports hemp/flax as leading natural-fibre blade candidates, while hybridisation and manufacturing conditions remain qualification variables. No literature record is treated as certification.

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


## Assassin's Creed Shadows rendering research — ACS-01..ACS-06
Added `research/BIUPIU-ASSASSINS-CREED-SHADOWS-RENDERING-RESOURCE-INDEX-v1.0.md`. Public technical references associated with Assassin's Creed Shadows are now indexed as reference-only rendering research and mapped into CG-3D, COMPUTE, DIGITAL-TWIN, AI, Unreal Engine 5, World Development Lab and cinematic rendering. The integration covers ray-traced GI/reflections, DDGI/radiance-cache research, performance tiers, original Japan-world environment targets and provenance/licence controls. Proprietary Ubisoft assets, binaries, extracted game files and restricted content remain excluded. **ACS-01 through ACS-04 executed; ACS-05/ACS-06 remain gated on connected renderer/UE5 hosts.**


## Forza Motorsport 6 graphics research — FM6-01

Added `research/BIUPIU-FORZA-FM6-GRAPHICS-RESEARCH-v1.0.md` and the provider-neutral `forza-reference.ts` adapter/test. FM6 is treated as a technical/visual reference only: LODs, normals/tangents/UVs, automotive materials, lighting, scene hierarchy, resource optimisation and camera presentation are mapped into Biupiu's original Unreal/Blender/Redshift/V-Ray/Octane/Lumion/KeyShot pipeline. Proprietary Forza assets, extracted resources, encryption keys and game binaries are explicitly excluded. **FM6-01 executed.**

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

**Biupiu R&D Research Index v3.3 — Adobe Media Production Integration**  
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


## Civilisation sandbox environments

The Main Hub now has separate culturally contextualised sandbox environments for:
- Southern African
- West African
- North African / Mediterranean
- South Asian
- East Asian
- Ancient Americas

Each sandbox follows: MAIN HUB → CIVILISATION SANDBOX → CULTURAL HUB → DEPARTMENT ENVIRONMENT → WORKSHOP/LAB → PROJECT → RESEARCH OBJECT. Department subscriber entitlements remain authoritative, so entering a sandbox does not unlock unrelated departments. Historical evidence, reconstruction and modern R&D remain separate and evidence-classified.


## Biupiu World — ancient civilisation layer

`research/BIUPIU-WORLD-ANCIENT-CIVILISATIONS-v1.0.md` defines the next world-building layer: separate civilisation environments inside regional sandboxes, department-specific spaces, historical/reconstruction zones, an asset-provenance model and evidence/access firewalls. Initial mapped environments include Southern African cultures, Ancient Egypt/Nubian-Kushite, Sumerian/Akkadian/Babylonian/Assyrian Mesopotamia, Indus/Harappan and South Asian environments, ancient Chinese/Japanese environments, and Mesoamerican/Andean environments. Damascus is modelled as a regional historical city/trade/metalworking gateway.


## Advanced Crystal Labs

Added the crystal-lab layer to Biupiu World:
- Mesopotamia Advanced Crystal Lab — archaeological/materials/optics research environment.
- Mu / Atlantean Crystal Speculative Lab — controlled hypothesis-testing environment.
- Atlantean Gardens — speculative world-building environment connecting water, minerals, optics, geometry and botanical zones.
- Crystal Claim-to-Test Register — source → hypothesis → experiment → measurement → reproduction → result workflow.

The speculative environments are explicitly separated from established archaeology and physics. Subscriber department controls remain active, and negative experimental results are retained.


## Robert Sepehr / Atlantean Gardens cross-link layer

Added `research/BIUPIU-ROBERT-SEPEHR-CROSS-LINK-INDEX-v1.0.md`. It cross-links source material on Atlantis, Hyperborea, Thule, Hy-Brasil, Celtic/Atlantic-contact claims, Hercules traditions, Amorites, Peru/Andes, Moon-Eyed People, Green Children of Woolpit, Odin/Norse material and Lost Tribes/Levant history into Biupiu World. These are separated into historical, mythological, folklore and speculative research environments and routed through the existing claim-to-test framework. citeturn0search2turn0search4


## Biupiu World — New Age Theory / Lost Civilisations

Added `research/BIUPIU-NEW-AGE-THEORY-LOST-CIVILISATIONS-v1.0.md` as a dedicated Main Hub speculative-research layer.

Core environments:
- Atlantis
- Mu
- Hyperborea
- Tartaria / Great Tartaria
- Hollow Earth

Additional linked lost-land, lost-city and esoteric traditions:
- Lemuria
- Kumari Kandam
- Thule
- Hy-Brasil
- Agartha
- Shambhala
- Aztlan
- Iram/Ubar
- Paititi
- Zerzura
- Ys
- Vineta
- Cantre'r Gwaelod
- El Dorado

A reality-control library separately models documented submerged/transformed landscapes including Doggerland, Sundaland, Beringia, Sahul and Te Riu-a-Māui / Zealandia. These are comparison cases, not evidence for the speculative entities.

The New Age Theory layer preserves source provenance, evidence states, counter-evidence and claim-testing so speculative world-building cannot silently become established history.


## New Age Theory entry point and character layer

Biupiu World now has a dedicated **MAIN HUB → NEW AGE THEORY** entry point for Atlantis, Mu, Hyperborea, Tartaria / Great Tartaria, Hollow Earth and associated lost-land/inner-Earth research.

Added:
- `research/BIUPIU-NEW-AGE-THEORY-CHARACTERS-v1.0.md` — original guide characters, environment avatars and neutral player research archetypes.
- The character system inherits department subscriber permissions and evidence-state controls.
- Historical/legendary figures are not presented as documentary portraits; original Biupiu characters are used for navigation and research guidance.

The full world model is defined in `research/BIUPIU-NEW-AGE-THEORY-LOST-CIVILISATIONS-v1.0.md`.


## New Age Theory visual production layer

Character and environment design now incorporates a controlled visual-reference workflow for archived videos/descriptions and allocated mod assets. See `research/BIUPIU-NEW-AGE-THEORY-CHARACTERS-v1.0.md`.

Priority packages:
- Tartaria
- Atlantis
- Hyperborea
- Mu
- Hollow Earth

Every source/mod asset receives provenance and licence metadata before reuse. Visual claims such as alleged giant inhabitants remain source-specific speculative variants rather than established facts.


## AI production integration gates

- `research/BIUPIU-AI-PRODUCTION-MODEL-GATE-v1.0.md` — AI-12 production-model boundary and retrieval benchmark gate.
- `research/BIUPIU-AI-END-TO-END-GATE-v1.0.md` — AI-13 provider adapter boundary, fail-closed behavior and deterministic end-to-end grounding test.
- `software/rnd-os-ai/src/biupiu_ai/provider_adapter.py` — provider configuration/health contract and fail-closed adapter boundary.
- `software/rnd-os-ai/tests/test_ai13.py` — provider safety and end-to-end citation propagation tests.
- **AI-13 status:** repository adapter boundary implemented; live external provider transport and real Android network test remain gated.

## AI-14 secure provider and mobile contract gate
- `research/BIUPIU-AI-SECURE-PROVIDER-HARNESS-v1.0.md` — AI-14 provider test harness, security boundary and mobile API contract.
- `software/rnd-os-ai/src/biupiu_ai/provider_harness.py` — deterministic injected provider harness with fail-closed citation checks.
- `software/rnd-os-ai/tests/test_ai14.py` — provider success, missing-citation and timeout/failure tests.
- `software/rnd-os-mobile/app/src/main/java/com/biupiu/rndos/ai/AiApiContract.kt` — stable Android AI request/response/error contract.
- **AI-14 status:** repository test harness and mobile API contract implemented; live provider transport, production authentication and compiled Android network integration remain gated.

## AI-15 authenticated gateway gate
- `research/BIUPIU-AI-AUTHENTICATED-GATEWAY-v1.0.md` — AI-15 bearer authentication contract, redaction controls and CI specification.
- `software/rnd-os-ai/src/biupiu_ai/auth_contract.py` — bearer-header validation and authorization redaction helpers.
- `software/rnd-os-ai/tests/test_ai15.py` — authentication-format and redaction tests.
- **AI-15 status:** authentication contract and tests implemented; CI workflow commit was blocked by repeated GitHub repository-state conflicts and has not been claimed as deployed or executed.


## Adobe media-production integration

Added `research/BIUPIU-ADOBE-PRODUCTION-PIPELINE-v1.0.md` and the `software/rnd-os-media/adobe/` adapter boundary for professional media production.

- Premiere Pro: UXP-first integration target; legacy CEP/PProPanel retained only as compatibility/reference material.
- After Effects: compositing, motion graphics, VFX and render-queue adapter boundary; legacy CEP/ExtendScript isolated behind an adapter.
- `MEDIA-JOB-SCHEMA.json` defines portable media-job, provenance, evidence, IP and licence metadata.
- Pipeline tracks include Engineering Showcase, Digital Twin, Biupiu World, Product Development Showreel and Research Evidence Video.
- Adobe software, proprietary binaries and SDK assets are not redistributed in this repository.

**ADOBE-01:** executed — architecture/provenance layer integrated. Live Adobe execution remains gated until the target workstation has the relevant Adobe applications and UXP/adapter test environment installed and validated.

## AI-16 production gateway policy gate
- `research/BIUPIU-AI-PRODUCTION-GATEWAY-v1.0.md` — bounded request schema, rate/cost policy and provider staging boundary.
- `software/rnd-os-ai/src/biupiu_ai/gateway_policy.py` — deterministic gateway request and provider-staging policy.
- `software/rnd-os-ai/tests/test_ai16.py` — request-limit, cost-limit and staging-prerequisite tests.
- **AI-16 status:** policy contract and deterministic tests implemented; live provider transport and production infrastructure remain gated.


## Redshift professional rendering integration

Added `research/BIUPIU-REDSHIFT-RESOURCES-v1.0.md`. GitHub research identified the official Maxon Redshift OSL shader repository and Redshift OCIO configuration resources, plus Cinema 4D Redshift automation/API references and Houdini/Redshift examples. Redshift is now mapped as a renderer adapter in the provider-neutral render pipeline for PRODUCT_STILL, DIGITAL_TWIN, CINEMATIC_SHOWREEL, CONCEPT_VARIATION and RESEARCH_VISUALIZATION workflows.

**RED-01 status:** architecture/resource integration executed. No proprietary Redshift binaries, SDKs or licensed assets are copied into the repository. Live Redshift execution remains gated on an installed and validated Redshift-capable environment.


## Lumion visualization integration — LUM-01

Added `research/BIUPIU-VISUALIZATION-PIPELINE-LUMION-v1.0.md`. Lumion is now indexed as a complementary real-time visualisation/presentation layer for CAD/BIM/product/environment concepts, Digital Twin presentation, investor imagery and video production. The authoritative engineering path remains CAD/CAE, simulation, Digital Twin and physical validation.

The Lumion track cross-links `CG-3D`, `DIGITAL-TWIN`, `COMPUTE`, `ROBOTICS`, `AERO`, `MARINE`, `MATERIALS`, `NFT-ATH-GEO`, `NFT-IP` and `VIDEO-SERIES`. Proprietary binaries, cracks/unlocks, and unlicensed asset redistribution are explicitly excluded. **LUM-01 executed.** Next: LUM-02 open-asset/PBR compatibility registry.

## AI-17 provider-neutral gateway service gate
- `research/BIUPIU-AI-GATEWAY-SERVICE-v1.0.md` — AI-17 gateway service, request IDs and structured error contract.
- `software/rnd-os-ai/src/biupiu_ai/gateway_service.py` — authentication/policy/provider orchestration with structured responses.
- `software/rnd-os-ai/tests/test_ai17.py` — gateway success, authentication failure and provider-failure tests.
- `software/rnd-os-mobile/app/src/main/java/com/biupiu/rndos/ai/AiApiContract.kt` — Android success/error envelope with request IDs.
- **AI-17 status:** gateway service and mobile error envelope implemented; live transport and production infrastructure remain gated.


## Lumion LUM-02 — open-asset/PBR registry

Added `research/BIUPIU-OPEN-ASSET-PBR-COMPATIBILITY-REGISTRY-v1.0.md`. The registry cross-links legitimate open/PBR discovery sources to Lumion, Unreal Engine 5, Blender, V-Ray, CAD/CAE, the Materials Genome and Digital Twin. Candidate resources are not treated as approved project assets until licence and provenance checks pass. **LUM-02 executed.** Next: LUM-03 machine-readable asset/material manifest.


## Redshift RED-03 — deterministic adapter/test-scene gate

Added `packages/biupiu-render-pipeline/src/redshift.ts` as a provider-neutral Redshift adapter contract with fail-closed environment validation, OSL validation-set identifiers, provenance rules and no proprietary dependency embedding. Added `research/BIUPIU-REDSHIFT-TEST-SCENE-SPEC-v1.0.md` for deterministic still/sequence validation and `packages/biupiu-render-pipeline/tests/redshift.validation.ts` for the adapter contract checks. **RED-03 status:** repository implementation complete; live Redshift rendering, shader loading and output-hash validation remain blocked until a connected Redshift-capable host/render node is available.

## AI-18 gateway state gate
- `research/BIUPIU-AI-GATEWAY-STATE-v1.0.md` — AI-18 replay, idempotency, audit and abuse-control boundary.
- `software/rnd-os-ai/src/biupiu_ai/gateway_state.py` — synchronized process-local replay/rate state and audit events.
- `software/rnd-os-ai/tests/test_ai18.py` — replay, rate-limit and audit tests.
- **AI-18 status:** development/test state layer implemented; distributed durable production state remains gated.


## Redshift RED-04 — cross-engine interoperability gate

Added `research/BIUPIU-RENDER-INTEROPERABILITY-RED-04-v1.0.md`, a provider-neutral interoperability matrix covering Blender, Unreal Engine 5, Redshift, V-Ray, Octane, Lumion and KeyShot. Added a machine-readable handoff manifest and deterministic provider-matrix test under `packages/biupiu-render-pipeline/`. The gate preserves source asset identity, model version, evidence/IP/licence state, provider/version, conversion settings, output hash and derivative-only rules. **RED-04 status:** implementation complete and ready for live cross-engine testing; live interoperability is not claimed until connected application environments produce measured results.


## Lumion LUM-03 — machine-readable asset/material manifest

Added `research/visual-assets/biupiu-visual-asset-manifest.schema.json`, an example manifest, and README documentation. The schema records asset identity, source/creator, licence evidence, file hashes/metadata, PBR maps, provenance/transformation history, authoring/target applications, and links to Biupiu Digital Twin/Materials Genome/project IDs. **LUM-03 executed.**


## RED-05 — Universal asset/material interchange

Added `research/BIUPIU-UNIVERSAL-ASSET-INTERCHANGE-RED-05-v1.0.md` and the provider-neutral interchange implementation under `packages/biupiu-render-pipeline/`. The new manifest carries sourceAssetId, sourceModelVersion, research/evidence/IP/licence states, geometry units/coordinate metadata, stable material IDs, PBR metadata and provenance into provider packages. GLTF, FBX and USD are supported as interchange targets, with OBJ/USDZ/native formats available to adapters. Provider-specific conversion remains adapter-controlled and lossy/unsupported features must be recorded rather than silently substituted.

Added `src/interchange.ts`, a canonical test fixture and `tests/red-05.interchange.ts`. The render pipeline export file was normalized to real newlines and now exposes the RED-05 contract. The module contract was expanded to match all provider IDs already defined by the pipeline. **RED-05 status:** repository implementation complete; live cross-provider conversion/render validation remains gated on connected application hosts and measured outputs.


## Lumion LUM-04 — automated validation + visualization provenance

Added `research/visual-assets/validate_visual_asset.py`, `VISUALIZATION-JOB-PROVENANCE-v1.0.md`, and an example visualization-job record. The pipeline now defines a licence/provenance validation gate and records source model, renderer/version, scene version, output hashes and Digital Twin/project lineage for renders and videos. JSON Schema 2020-12 is the manifest validation basis. glTF/PBR remains the interoperability reference for portable real-time material description. **LUM-04 executed.**


## RED-06 — Asset conversion and material translation

Added `packages/biupiu-render-pipeline/src/conversion.ts`, a provider-neutral conversion report contract that explicitly distinguishes READY, LOSSY, BLOCKED and FAILED conversions. Unsupported material features must be reported with a loss reason/fallback rather than silently dropped. Added the RED-06 fixture and automated invariants test, and exposed the conversion contract through the render-pipeline package and module contract. **RED-06 status:** repository conversion/loss-reporting architecture implemented; actual provider conversion and visual-equivalence acceptance remain gated on connected renderer hosts and measured round-trip results.


## FS2002 Nexus Mods × GitHub cross-link

Added `research/BIUPIU-FS2002-NEXUS-GITHUB-CROSS-LINK-v1.0.md`. The track separates Microsoft Flight Simulator 2002 from modern MSFS content and cross-links historically relevant Nexus/GMax authoring documentation with open-source GitHub tooling for legacy scenery, BGL analysis, simulator-state interoperability, head tracking and period technical documentation. **FS2K2-01 discovery/cross-link gate: executed.** No third-party game assets were copied or redistributed, and no live FS2002 compatibility is claimed.


## Microsoft Flight Simulator 2024 — Nexus Mods × GitHub cross-link

Added `research/BIUPIU-MSFS2024-NEXUS-GITHUB-CROSS-LINK-v1.0.md`. The new MSFS 2024 track separates current simulator-generation resources from FS2002/FSX/MSFS 2020 material and cross-links Nexus aircraft, EFB/cockpit, texture/livery, localization and visual resources with GitHub avionics, cockpit I/O, AI, SimConnect and addon-management tooling. **MSFS24-01 discovery/cross-link gate: executed.** No third-party Nexus assets or proprietary binaries were copied.

## AI-21 transactional audit integration gate
- `research/BIUPIU-AI-TRANSACTIONAL-AUDIT-v1.0.md` — AI-21 gateway/audit persistence integration and failure boundary.
- `software/rnd-os-ai/src/biupiu_ai/gateway_service.py` — AuditStore integration for success, rejection and provider-failure events.
- `software/rnd-os-ai/tests/test_ai21.py` — persistence integration tests.
- **AI-21 status:** transactional audit integration boundary implemented; production durable-store failure semantics remain gated.


## Lumion LUM-05 — unified renderer router

Added `research/visual-assets/BIUPIU-UNIFIED-RENDERER-ROUTER-v1.0.md`. The routing contract now connects approved asset manifests and visualization jobs to Lumion, Unreal Engine 5, V-Ray, Blender and CAD/BIM workflows, while keeping engineering truth outside the renderer layer. **LUM-05 executed.**
