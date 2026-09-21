# Biupiu NFT System

## Project Purpose

The Biupiu NFT System is a structured digital-asset, computational-art, crowdfunding and intellectual-property framework for the Biupiu personal R&D / digital-art portfolio.

The founding phase is designed as a **crowdfunding project to help launch and establish the Biupiu research and development ecosystem**. It connects original artwork and computational outputs to documented research while maintaining a clear boundary between NFT ownership and underlying Biupiu intellectual property.

## Architecture Status

Existing subscriber tiers, DMS entitlement controls, BPU payment interfaces and Web3 provenance architecture remain the canonical layers. Native payment integration is now documented under `payment/native/` and deliberately reuses those systems rather than creating a parallel entitlement model.

### Native payment boundary

`Client -> Payment Gate -> Provider Verification -> DMS Entitlement -> Audit/Trust -> optional Blockchain Anchor`

The client cannot grant paid access. Android digital subscriptions use the appropriate platform billing rail; authoritative entitlement state is server-side. BPU remains disabled until its own launch gates pass.

### Closed-shell real-world deployment boundary

Future physical Biupiu sites may use a private closed-shell server architecture. This is a deployment target, not a claim that the production infrastructure exists today.

Target boundary:

`Public Interface -> Authenticated Gateway -> Biupiu DMS -> Private Service Layer -> Isolated Research/Industrial Systems`

Future production gates include hardware-backed identity, mutual authentication, network segmentation, signed releases, secure boot/TPM-equivalent roots of trust, key rotation, controlled updates, offline/isolated operation and auditable site/device authorization.

### Native payment security documents

- `payment/native/README.md`
- `payment/native/PRODUCT-MAPPING-v1.json`
- `payment/native/SECURITY-VERIFICATION-GATES-v1.md`
- `payment/native/FOREIGN-LANGUAGE-HARVEST-MANIFEST-v1.md`

These documents define architecture and gates. They do **not** falsely mark production payment processing as complete.

## Research Architecture

Biupiu uses a permanent multi-layer research stack:

**Primary archaeology/history -> JSTOR -> AnthroSource -> ResearchGate -> Emerald Insight -> ancient texts/scientific data -> patents/prior art -> public/declassified engineering -> GitHub/BIUPIU CODEX -> computational validation -> physical validation -> IP/NFT gate.**

## Core Connections

- Original physical and digital artworks
- Generative and computational art
- 3D computational geometry
- Ancient-technology and archaeological research themes
- Ancient Africa and human-origins research
- Computational engineering and AI
- 3D holography and quantitative-phase modelling
- Photonics and optical communications
- Metamaterials and advanced materials
- Energy, water and biological systems
- Invention and concept records
- NFT metadata and provenance
- EVM smart contracts and controlled minting
- **Biupiu Company Algorithm Network** — reusable, versioned computational families
- **Biupiu Blockchain Registry Network** — planned hash/identity anchoring layer
- Signed physical works and art-book records
- Founding crowdfunding releases
- **Biupiu World Arcade / Mod Hub resource layer**
- **Biupiu-native game-resource registry and rights classification**

## Portfolio Boundary

This repository is a dedicated NFT / computational-art / IP / personal R&D track. It remains separate from the immediate commercial DTIC/InvestSA funding library unless an item is explicitly approved for transfer into that business registry.

## Core Repository Structure

- `MASTER-TEMPLATE.md` — master record template for artworks, computational artifacts, concepts and NFT releases.
- `INVENTION-REGISTER.md` — controlled register for inventions, concepts and research-linked IP records.
- `FOUNDING-CROWDFUNDING-BRIEF.md` — public project brief for the founding NFT crowdfunding campaign.
- `metadata/` — NFT metadata records.
- `artworks/` — artwork records and provenance references.
- `research/` — indexed research, algorithm, blockchain, game-resource and rights records.
- `releases/` — collection and crowdfunding release plans.
- `contracts/BiupiuNFT.sol` — EVM ERC-721 reference contract.
- `hardhat.config.js` — Hardhat network/solidity configuration.
- `deploy-nft.js` — deployment script.
- `mint-nft.js` — minting script.
- `.env.example` — local configuration template; never commit `.env` or private keys.
- `WEB3-MINTING.md` — deployment and minting guide.
- `NFT-MINTING-ARCHITECTURE-v2.0.md` — blockchain architecture and release gate.
- `research/BIUPIU-COMPANY-ALGORITHM-NETWORK-v1.0.md` — reusable company algorithm-network architecture.
- `research/BIUPIU-ALGORITHM-REGISTRY-v1.0.md` — immutable algorithm-family/version registry.
- `research/BIUPIU-BLOCKCHAIN-REGISTRY-ARCHITECTURE-v1.0.md` — planned research/release blockchain anchoring architecture.
- `research/BIUPIU-ARCADE-AND-EMULATION-RESOURCE-ARCHITECTURE-v1.0.md` — rights-aware arcade/emulation and native-runtime architecture.
- `research/BIUPIU-NATIVE-GAME-RESOURCE-REGISTRY-v1.0.json` — machine-readable game/resource registry schema.
- `research/BIUPIU-CREATOR-MOD-HUB-ARCHITECTURE-v1.0.md` — free Unreal/Unity/Biupiu creator and modding architecture.
- `payment/native/` — native payment boundary, tier mapping, security gates and harvest manifest.

## Research -> Algorithm -> NFT -> Blockchain Pipeline

`Research -> source/evidence -> Research ID -> computational model -> algorithm family/version -> parameters + seed -> 01_PROVENANCE + 02_STANDALONE -> release manifest -> hashes -> metadata -> IP/licence gate -> blockchain registry anchor -> smart contract -> testnet -> test mint -> verification -> production record`

Every serious artwork receives a Biupiu Research ID and a separate NFT ID. One research project may generate multiple artworks or editions, and one algorithm family may generate multiple releases.

## Algorithm network rule

**Algorithms evolve; released records do not.**

Future NFTs should reuse the computational kernel where appropriate. A change to an algorithm creates a new version and never silently changes the historical algorithm used by an earlier NFT. Every release records the exact algorithm version, parameters, seed, source commit and asset hashes.

## Two-Image NFT Standard

Every future NFT release is designed as a pair:

1. **01_PROVENANCE** — BIUPIU branded research/provenance presentation.
2. **02_STANDALONE** — independent collector-facing computational artwork.

The pair shares the research/release record but receives independent versions and hashes.

## Web3 / EVM Minting Layer

The current development stack uses Solidity, OpenZeppelin Contracts, Hardhat and ethers.js.

Development/testnet targets:

- Ethereum Sepolia — chain ID 11155111.
- Polygon Amoy — chain ID 80002.

The reference contract provides capped supply, controlled minting, batch minting, token URI storage and ERC-2981 royalty signalling. Production use remains gated by contract testing, testnet deployment, verification, IP/licence review and final release approval.

## Biupiu Intelligence Learning Layer

The Intelligence layer now includes a versioned learning/provenance foundation for research, experiments, model outputs, failures and repository maintenance. Learning records preserve old/new lineage and do not automatically delete superseded material. Approved learning checkpoints can optionally be anchored through `contracts/BiupiuLearningRegistry.sol`; raw learning data remains off-chain.

Core maintenance events — bug fixes, code changes, technology/dependency updates, audits, index repairs and regression evidence — can be represented as learning events. This creates a traceable feedback loop without claiming that the system autonomously trains or scientifically validates itself.

## Blockchain Network Rule

The initial Biupiu blockchain architecture is an **EVM anchoring/registry network**, not an independently launched Biupiu Layer-1. GitHub remains the canonical detailed provenance record; approved hashes and release identities can later be anchored on-chain through a dedicated `BiupiuResearchRegistry` contract.

The registry should record commitments such as release ID, Research ID, algorithm ID/version, manifest/artwork/metadata hashes and optional NFT contract/token references. Confidential research, private datasets, secrets and unpublished IP remain off-chain.

## Biupiu Arcade / Game Resource Layer

Biupiu World now has a registered architecture for future virtual arcades, retro-PC rooms, console rooms, digital museums and game-development showcases.

The system deliberately separates:

**emulator/runtime rights -> game/content rights -> Biupiu distribution rights -> creator rights -> provenance.**

No external game is considered commercially distributable merely because it is old, free to download, available in an archive, associated with a closed publisher, or compatible with an open-source emulator.

Canonical documents:

- `research/BIUPIU-ARCADE-AND-EMULATION-RESOURCE-ARCHITECTURE-v1.0.md`
- `research/BIUPIU-NATIVE-GAME-RESOURCE-REGISTRY-v1.0.json`
- `research/BIUPIU-CREATOR-MOD-HUB-ARCHITECTURE-v1.0.md`

### Native target

External emulators such as MAME, DOSBox and ScummVM are compatibility/reference resources subject to their licences. The long-term Biupiu target is a **Biupiu Arcade Runtime Interface** and eventually a native Biupiu Engine implementation.

Target interaction:

`Avatar -> Biupiu Arcade -> Rights/Entitlement Gate -> Runtime Adapter -> Game Session -> DMS/Leaderboard/Provenance`

### Rights classification

- **GREEN** — intended Biupiu use/redistribution rights verified.
- **BLUE** — free/open but scope requires review.
- **YELLOW** — rights holder identified; permission/licence required.
- **ORANGE** — ownership/chain-of-title investigation.
- **RED** — no approved Biupiu use.
- **GREY** — research/reference only.

Unknown rights remain non-distributable.

## Biupiu Free Creator / Mod Hub

Biupiu will use a free community modding layer as a deliberate give-back to modders and as a creator-acquisition mechanism.

Initial compatibility targets:

**Unreal Engine + Unity + Biupiu-native formats.**

The long-term native layer includes creator identity, asset packaging, dependency resolution, cross-engine metadata, provenance, licence declarations, security scanning, compatibility testing, versioning, rollback and attribution.

Creators retain the rights they actually own. Biupiu should receive only the permissions required by the explicit publishing licence.

The intended growth loop is:

`Free tools -> creators -> mods -> players -> Biupiu World -> social discovery -> more creators -> professional users -> simulation/CAD demand -> Biupiu Engine adoption`

The free layer is not dependent on copyrighted third-party ROM redistribution.

## Ancient Systems × Computational Geometry

Dedicated stream: `NFT-ATH-GEO`  
Record: `research/NFT-ANCIENT-SYSTEMS-COMPUTATIONAL-GEOMETRY.md`

Planned themes include ancient water engineering, agricultural terraces and waru-waru systems, mining and metallurgy, ceramics, stone construction, architectural geometry, archaeoastronomy, ancient transport/trade networks and southern African archaeological technologies.

Potential computational systems include circles, spirals, fractals, Voronoi structures, tessellation, symmetry, topology, polyhedra, flow fields, networks, phyllotaxis, recursion and parametric surfaces/meshes.

## Evidence Classification

- **DOCUMENTED** — supported by reliable historical, archaeological or scientific evidence.
- **RECONSTRUCTED** — computational/physical reconstruction based on available evidence.
- **EXPERIMENTAL** — Biupiu experiment testing a proposed mechanism/model.
- **HYPOTHESIS** — proposed interpretation requiring further investigation.
- **SPECULATIVE** — creative exploration inspired by a subject.

Artistic interpretation must not be presented as archaeological or scientific proof.

## NFT Classes

- **Class A — Art:** primarily aesthetic digital/generative work.
- **Class B — Research Art:** artwork linked to documented Biupiu research.
- **Class C — Computational Artifact:** artwork linked to an algorithm, parameters and reproducible-generation record where appropriate.

## Provenance Standard

Where applicable, each computational artwork preserves Research ID, NFT ID, source/reference genealogy, evidence classification, algorithm name/version, software/dependencies, input data, parameters, generation seed, Git version/commit, artwork version, asset hash, metadata hash, blockchain information and applicable licence.

Provenance chain: **Research Source -> Evidence Classification -> Model -> Algorithm Family/Version -> Parameters -> Artwork Pair -> Metadata -> Release Manifest Hash -> Registry Anchor -> Smart Contract -> Blockchain Token.**

## Crowdfunding

The founding collection is intended to help establish Biupiu research and development infrastructure. Potential uses include research and development, computational resources, software, experimental development, agricultural/materials research, prototyping, digital infrastructure, documentation, generative-art development, archive/website infrastructure and IP development.

The NFT project should not be described as granting equity, investment returns or ownership of Biupiu unless a separate legally compliant structure expressly provides those rights.

## Intellectual Property

NFT ownership does not automatically transfer Biupiu patents, inventions, trademarks, proprietary research, confidential information, biological materials, source code or underlying scientific discoveries. Each release must state its applicable licence.

Third-party images, code, datasets and research outputs require rights/licence review before commercial use. Potentially patentable or IP-sensitive information may remain private until appropriate protection has been considered.

## Master Research Index

`research/INDEX.md` remains the master R&D research index. The algorithm, blockchain, native payment, game-resource and creator specifications are linked into the NFT/Web3 track and should be used as the operating architecture for future computational-geometry and Biupiu World releases.

## Blender / Biupiu World Production Layer

The repository now defines two Blender engine paths: the official Blender upstream mirror for Windows desktop production and the reviewed Android Blender fork for mobile. Both consume the Biupiu Digital Twin and asset-provenance contracts. Biupiu World character, environment and product-development showreel pipelines are documented under `world/`, `docs/blender-windows/` and `showcase/`.

## Biupiu OS / Biupiu AI separation

As of 19 September 2026, the original R&D OS v1.0 implementation is the **Core OS Baseline**. Biupiu AI is a separate modular intelligence layer under `software/rnd-os-ai/`.

The system remains integrated through explicit OS interfaces: **AI -> OS validation/audit -> authoritative state**. AI is optional to core OS operation and does not directly bypass authoritative OS controls.

Canonical architecture: `research/BIUPIU-OS-AI-SEPARATION-ARCHITECTURE-v1.0.md`.

## Mathematics / Problem-Solving Layer

The repository includes a dedicated MATH verification-oriented layer for problem classification, deterministic invariant checking, numerical residual validation and future formal theorem-proving adapters.

Pipeline: PROBLEM -> CLASSIFY -> RETRIEVE -> DECOMPOSE -> SOLVE -> VERIFY -> SIMULATE -> SENSITIVITY -> DIGITAL-TWIN -> VALIDATE -> RECORD.

## Gate-Learning / Conflict-Resolution Architecture

Repeated repository gates are governed by the Gate-Learning Architecture and machine-readable Gate-Learning Matrix. Execute/diagnose/fix/retest cycles preserve failure evidence, regression evidence, dependency impact and promotion lineage rather than treating repeated passes as learning by themselves.

Canonical documents: `research/BIUPIU-GATE-LEARNING-ARCHITECTURE-v1.0.md` and `research/BIUPIU-GATE-LEARNING-MATRIX-v1.0.json`.

The Intelligence layer uses these records to improve diagnostic retrieval and preventative-test generation while preserving authoritative OS controls, human release authority and third-party licence/security boundaries.

**README synchronization:** 21 September 2026
