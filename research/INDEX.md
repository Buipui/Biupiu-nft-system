# Biupiu R&D Research Index

**Version:** 2.2  
**Updated:** 16 September 2026  
**Repository:** Biupiu NFT / computational-art / personal R&D portfolio

## Master evidence architecture
`research/BIUPIU-EVIDENCE-LAYER-ARCHITECTURE.md` is the master source-control architecture. Core layers are: primary archaeology/history; JSTOR; **AnthroSource**; ResearchGate/scientific literature; **Emerald Insight**; controlled speculative/hypothesis sources; ancient texts; scientific primary data; patents/prior art; public/declassified technical archives; GitHub/BIUPIU CODEX; computational validation; and physical/experimental validation.

**Core doctrine:** No idea is rejected merely because it is unconventional. No idea is accepted merely because it is fascinating. Every important claim becomes a testable research object.

## Permanent research operating protocol
`research/BIUPIU-RESEARCH-OPERATING-PROTOCOL-v2.0.md` is the default workflow. `research/SOURCE-TO-DEPARTMENT-CROSSWALK.md` routes each source layer into relevant Biupiu departments.

**Ancient-technology rule:** ancient knowledge generates the question; archaeology establishes the historical record; anthropology explains human-material context; science tests mechanisms; engineering converts validated mechanisms into designs; computation models and optimises them; experiments decide what works; IP review determines what can be protected or commercialised.

## Repository boundary
This is the personal Biupiu computational-art, invention, speculative-research and R&D/IP track. It remains separate from the immediate commercial DTIC/InvestSA library unless explicitly transferred.

## Master department architecture
`research/BIUPIU-DEPARTMENT-INDEX.md` is the authoritative department map for the full Biupiu R&D/IP portfolio. It integrates biotechnology, regenerative agriculture, genetics/seed breeding, industrial hemp, biochar/biocarbon, biochemical engineering, textiles/fibres, adhesives/coatings, composites, advanced materials, water, energy, electrical/electromagnetics, photonics, quantum/photonic materials, metamaterials, aerospace, marine, computational engineering, AI, computational geometry, digital twins, robotics/automation, advanced manufacturing, biomedical/life sciences, geoarchaeology, historical GIS, Ancient Applied Technology, anthropology/human-material systems, geomagnetics, controlled speculative research, IP and NFT/generative art.

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
- `MM` / `MM-NASA` — metamaterials/metasurfaces and NASA/public technical cross-reference.
- `AERO` / `STEALTH-GEO` — public-source aerospace, aerodynamics, SR-71/stealth geometry and lightweight mobility.
- `MARINE` — propellers, pumpjets, hydrofoils, hulls and marine turbines.
- `CG-3D` / `GEOMETRY` — parametric geometry, topology, CAD, reconstruction and optimisation.
- `CODEX` / `COMPUTE` — Python, CFD, FEA/FEM, multiphysics, algorithms, data and reproducible computational engineering.
- `AI` — machine learning, surrogate models, generative engineering and optimisation.
- `DIGITAL-TWIN` — physical systems, sensor data, models and optimisation loops.
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
- `SPEC` / `SPEC-VIDEO` / `SPEC-SEP` / `SPEC-CONVERGENCE` — controlled speculative-source research.
- `JSTOR` / `ANTHROSOURCE` / `RG` / `EMERALD` / `PRIMARY` / `TEXTS` — transversal evidence-source layers used across relevant departments.
- `NFT-IP` / `NFT-CF` / `NFT-ATH-GEO` / `NFT-GEN` / `NFT-PROV` / `NFT-ARCH` / `NFT-ORIGIN` — research-to-art, crowdfunding, generative art, provenance and NFT architecture.
- `NFT-WEB3` / `NFT-MINT` / `NFT-EVM` — smart contracts, Web3 tooling, deployment, minting, token URI management and blockchain provenance.

## NFT / Web3 master architecture
The NFT system is now a complete research-to-blockchain development track rather than an artwork-only repository.

### Research-to-NFT pipeline
`RESEARCH → EVIDENCE → RESEARCH ID → COMPUTATIONAL MODEL → ALGORITHM → PARAMETERS/SEED → STAND-ALONE ARTWORK → PROVENANCE ARTWORK → HASHES → METADATA → IP/LICENCE GATE → SMART CONTRACT → TESTNET → TEST MINT → VERIFICATION → PRODUCTION MINT → BLOCKCHAIN RECORD`

### Mandatory two-image standard
Every future NFT release is designed as a paired asset:

1. **01_PROVENANCE** — BIUPIU branded research/provenance presentation.
2. **02_STANDALONE** — independent collector-facing computational artwork.

The pair shares a Research ID/release record but receives independent versions and hashes.

### Web3 repository layer
- `contracts/BiupiuNFT.sol` — ERC-721 reference contract with capped supply, owner-controlled minting, batch minting, per-token URI and ERC-2981 royalty signalling.
- `hardhat.config.js` — EVM development/testnet configuration.
- `package.json` — Hardhat/ethers/OpenZeppelin/dotenv tooling.
- `.env.example` — secret-safe local configuration template.
- `scripts/deploy.js` — deployment workflow specification.
- `scripts/mint.js` — mint workflow specification.
- `docs/WEB3-MINTING-LAYER-v1.0.md` — operational Web3 documentation.
- `docs/NFT-MINTING-ARCHITECTURE-v2.0.md` — contract/network/wallet/on-chain/off-chain architecture.

### Development networks
- Ethereum Sepolia — chain ID 11155111.
- Polygon Amoy — chain ID 80002.

These are test/development targets. Mainnet deployment is a separate release-governance decision.

### Security doctrine
Private keys, seed phrases and `.env` files are never committed. Deployment and treasury wallets are separated conceptually, and future production architecture should consider role separation/multisig custody. Contract code must be tested and source-verified where supported before production use.

### IP doctrine
The blockchain token does not automatically transfer Biupiu patents, inventions, trademarks, confidential research, source code, datasets or commercial rights. Token URI metadata and licence terms define the rights actually granted.

## Core evidence-source registry

### `SRC-PRIMARY` — Primary archaeology/history
Highest-priority layer for direct claims about physical sites, artefacts, chronology and historical records.

### `SRC-JSTOR` — JSTOR
Core scholarly layer for archaeology, anthropology, history, material culture, technology, environment and ancient civilisations.

### `SRC-ANTHROSOURCE` — AnthroSource / American Anthropological Association
Core anthropology/archaeology layer for craft production, technology transmission, human-material relationships, cultural ecology, social organisation and ancient agricultural landscapes. See `research/ANTHROSOURCE-ANCIENT-TECHNOLOGY-REGISTER.md` for indexed records and exact source metadata.

**Mandatory use cases:** ancient technology process studies; craft and materiality; technology transmission; human-material interaction; cultural ecology; agricultural landscapes; archaeological landscape methods; and anthropology-led interpretation of technological behaviour.

**Important boundary:** AnthroSource supports anthropological/archaeological propositions and research framing. It does not automatically prove an engineering performance claim. Engineering mechanisms must be independently tested through scientific, computational or experimental evidence.

### `SRC-RESEARCHGATE` — ResearchGate/scientific literature
Scientific and engineering discovery layer for archaeometry, metallurgy, materials, genetics, experimental archaeology, computational research and engineering. Prefer publisher/institutional/DOI versions for final evidence records.

### `SRC-EMERALD` — Emerald Insight
Core systems/implementation layer for sustainability, water, agriculture, infrastructure, engineering management, optimisation and socioeconomic implementation. Index at publication/DOI level and distinguish content type.

### `SRC-TEXTS` — Ancient texts
Textual evidence and cultural traditions, with strict separation between historical testimony, mythology, later commentary and modern interpretation.

### `SRC-SCI` — Scientific primary data
Dating, archaeogenomics, isotopes, palaeoclimate, geology, geophysics, chemistry, physics and environmental datasets.

### `SRC-IP` — Patents/prior art
Modern implementation and FTO layer. Patent publication does not establish efficacy; record legal status and relevant claims.

### `SRC-DECLASS` — Public/declassified technical archives
Historical/public engineering layer. Use only lawfully public/declassified information and validate technical claims independently.

### `SRC-GITHUB-CODEX` — GitHub / BIUPIU CODEX
Reproducible code, algorithms, simulation methods, datasets and computational engineering. Record repository, commit/version, licence and dependencies.

### `SRC-COMPUTE` — Computational validation
GIS/CAD/CFD/FEA/EM/thermal/acoustic/statistical/network/optimisation and digital-twin validation.

### `SRC-EXPERIMENT` — Physical validation
Biupiu laboratory/field reconstruction, prototypes, sensor measurements and repeatability studies.

## AnthroSource master register integration
`research/ANTHROSOURCE-ANCIENT-TECHNOLOGY-REGISTER.md` is now a formal sub-index of this master index.

Current indexed records include:

1. **AS-AAT-001 — Agricultural landscapes and relict field systems:** Casana (2024), *The state of the field: Emerging approaches to the archaeology of agricultural landscapes*, DOI 10.1111/apaa.12181. Routes to `AAT/AGRI/GEOARCH/LAND-GIS/ALA/WATER/CODEX`. Use for landscape-scale agricultural archaeology and modern archaeological methods; not as proof of a particular Biupiu technology.
2. **AS-AAT-002 — Technology as material and behavioural selection:** Bleed (1997), *Content as Variability, Result as Selection: Toward a Behavioral Definition of Technology*, DOI 10.1525/ap3a.1997.7.1.95. Routes to `AAT/AAT-H/MATERIALS/GEOMETRY/CODEX/IP`. Supports process/skill/selection/context-aware technology records.
3. **AS-AAT-003 — Craft production, fibres and metals:** Hendon (2015), *Producing Goods, Shaping People: The Materiality of Crafting*, DOI 10.1111/apaa.12068. Routes to `AAT/AAT-H/HEMP/TEXTILES/MATERIALS/BIOCARBON/COMPOSITES`. Bridges ancient craft/process research with modern material and process engineering questions.
4. **AS-AAT-004 — Early blade technologies:** Bar-Yosef (1999), *The Big Deal about Blades: Laminar Technologies and Human Evolution*, DOI 10.1525/aa.1999.101.2.322. Routes to `AAT/AAT-H/MATERIALS/GEOMETRY/PALAEO/CODEX`. Supports comparative study of geometry/process evolution without assuming a single technological origin.
5. **AS-AAT-005 — Stone-tool making and materiality:** Efrati (2026), *Reframing the Chipped Edge: Combining Materiality, Ontology, and Embodiment to Rethink Stone Tool-Making and Human Conscious Behavior in the Paleolithic Past*, DOI 10.1111/anoc.70016. Routes to `AAT/AAT-H/GEOMETRY/MATERIALS/PALAEO`. Use for contemporary anthropology of stone-tool making and embodied human-material interaction; do not infer untested engineering mechanisms.

**Methodological extensions now required:** future ancient-agriculture searches should cross-reference agricultural-landscape archaeology, LiDAR/aerial imagery, ecological datasets and Indigenous/traditional ecological knowledge where relevant; future ancient-craft searches should record materials, skills, process, labour/social context and output; future ancient-technology claims must distinguish archaeological evidence from modern engineering reconstruction.

## Evidence workflow
`hypothesis/source → exact claim → source genealogy → PRIMARY → JSTOR → ANTHROSOURCE → RESEARCHGATE → EMERALD → TEXTS/SCIENCE → patents/declassified → GIS/CODEX → experiment → evidence status → IP/NFT gate`

Evidence controls: **A Directly demonstrated; B Strongly supported; C Plausible/incomplete; D Testable hypothesis; E Unsupported/contradicted; M Mythological/cultural; S Speculative/inspirational.**

Three videos repeating the same source count as one source lineage, not three independent confirmations.

## Cross-department integration
`AAT/AAT-H ↔ GEOARCH/LAND-GIS/ALA/PALAEO ↔ COMPUTE/GEOMETRY ↔ NFT-ART`

`JSTOR/ANTHROSOURCE/RESEARCHGATE/EMERALD/PRIMARY/TEXTS ↔ every relevant AAT division`

`ANTHROSOURCE → AAT/AAT-H → AGRI/WATER/GEOARCH/LAND-GIS → MATERIALS/HEMP/TEXTILES → CODEX/GEOMETRY`

`BIO/BIO-GEN → AGRI → HEMP → BIOCARBON/BIOCHEM → MATERIALS/COMPOSITES/TEXTILES/COAT`

`AGRI ↔ WATER ↔ GEOARCH ↔ LAND-GIS ↔ ALA/AAT`

`ENERGY ↔ ELECTROMAG ↔ PHOTONICS ↔ CRM ↔ MM`

`AERO ↔ MARINE ↔ MATERIALS ↔ COMPOSITES ↔ GEOMETRY ↔ COMPUTE ↔ AI`

`COMPUTE ↔ AI ↔ GEOMETRY ↔ DIGITAL-TWIN ↔ ROBOTICS ↔ ADV-MFG`

`IP ↔ every department`

`NFT-ATH-GEO ↔ AAT/AAT-H ↔ GEOARCH/WATER/AGRI ↔ GEOMETRY/CODEX ↔ NFT-PROV/NFT-GEN ↔ NFT-EVM/NFT-MINT`

## Current high-value integrated programmes

1. **HempCarbon Energy Storage:** HEMP ↔ BIOCARBON ↔ ENERGY ↔ MATERIALS ↔ ELECTROMAG ↔ CODEX ↔ IP.
2. **BioCarbon Metallurgy / Wootz research:** AAT/AAT-H ↔ MATERIALS ↔ BIOCARBON ↔ BIOCHEM ↔ CODEX ↔ EXPERIMENT ↔ IP.
3. **Ancient Hydraulic Systems:** AAT/AAT-H ↔ AGRI ↔ WATER ↔ GEOARCH ↔ LAND-GIS ↔ Emerald/JSTOR/AnthroSource ↔ CFD/CODEX.
4. **Computational Turbine Engine:** ENERGY ↔ MARINE ↔ AERO ↔ GEOMETRY ↔ COMPUTE ↔ AI ↔ patents/declassified records ↔ EXPERIMENT.
5. **Digital Ancient Technology Atlas:** AAT ↔ AAT-H ↔ GEOARCH ↔ ALA ↔ GEOMETRY ↔ CODEX ↔ NFT-ATH-GEO.
6. **Photonics / Structured Light:** PHOTONICS ↔ PH-QPM ↔ COMPUTE ↔ AI ↔ DIGITAL-TWIN ↔ ELECTROMAG.
7. **Metamaterials:** METAMATERIALS ↔ MM-NASA ↔ MATERIALS ↔ PHOTONICS/ELECTROMAG ↔ GEOMETRY ↔ CODEX.
8. **Anthropology of Technology / Human-Material Systems:** AAT-H ↔ ANTHROSOURCE ↔ AAT ↔ MATERIALS ↔ AGRI ↔ HEMP/TEXTILES ↔ GEOARCH ↔ CODEX.
9. **Research-to-Blockchain NFT System:** NFT-ATH-GEO/NFT-GEN/NFT-PROV/NFT-ORIGIN ↔ CG-3D/GEOMETRY ↔ CODEX ↔ IP ↔ NFT-EVM/NFT-MINT. This programme converts evidence-controlled research and reproducible computational outputs into paired provenance/stand-alone artwork assets, content-addressed metadata and controlled EVM minting records.

## CODEX execution layer
`research/CODEX-SPEC-EXECUTION.md` is the computational gate from source capture through claim extraction, provenance graph, baseline data, null/alternative models, simulation/statistics, evidence-status update and IP/NFT output. `research/CODEX-DEPARTMENT-QUEUES.md` operationalises department-specific simulation backlogs.

## NFT/Web3 execution layer
`releases/BIUPIU-NFT-COLLECTION-ARCHITECTURE-v1.0.md` is now v2.0 and includes the blockchain minting lifecycle. `contracts/BiupiuNFT.sol` is the reference ERC-721 contract. Hardhat/ethers tooling is configured for development and testnet deployment. The production gate requires final paired artwork, frozen metadata, asset hashes, licence/IP review, testnet deployment, test mint, verification and only then production mint authorisation.

## New permanent source and routing files
- `research/ANTHROSOURCE-ANCIENT-TECHNOLOGY-REGISTER.md`
- `research/SOURCE-TO-DEPARTMENT-CROSSWALK.md`
- `research/BIUPIU-RESEARCH-OPERATING-PROTOCOL-v2.0.md`
- `releases/BIUPIU-NFT-COLLECTION-ARCHITECTURE-v1.0.md` — now v2.0 Web3-enabled NFT architecture.
- `docs/WEB3-MINTING-LAYER-v1.0.md` — smart-contract/deployment/minting operations.
- `docs/NFT-MINTING-ARCHITECTURE-v2.0.md` — blockchain governance and on-chain/off-chain separation.

## Repository correlation rule
Every newly indexed AnthroSource record must be correlated against: primary archaeology/history; JSTOR where relevant; ResearchGate/scientific literature; Emerald for implementation/system context where relevant; patents/prior art for modern implementations; public/declassified technical records where relevant; GitHub/CODEX for reproducibility; and a defined experimental question where the claim can be tested.

Each resulting research object should carry: source ID, exact claim, source genealogy, evidence status, department codes, computational/CODEX queue, experimental path, IP status and NFT relevance.

## Status

**Master R&D index upgraded to v2.2.** The NFT stream is now explicitly connected to the EVM smart-contract/minting layer, while the research-to-art evidence architecture, two-image release standard and IP boundary remain mandatory. Image generation remains paused; no final NFT image is represented as minted or production-approved.
