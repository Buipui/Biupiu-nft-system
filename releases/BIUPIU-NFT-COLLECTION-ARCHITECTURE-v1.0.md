# BIUPIU NFT COLLECTION ARCHITECTURE v2.1

**Effective:** 2026-09-16  
**Status:** ACTIVE COLLECTION + WEB3 + ALGORITHM NETWORK STANDARD  
**Image generation:** PAUSED UNTIL AVAILABLE

## Purpose

This is the production architecture for future BIUPIU NFT releases, from research and computational generation through blockchain minting. Every release produces two distinct visual assets from the same research/computational record:

1. **PROVENANCE EDITION IMAGE** — branded presentation image showing research lineage and provenance context.
2. **STAND-ALONE NFT IMAGE** — collector-facing artwork with computational geometry/research as the hero.

The two images are related but never interchangeable.

## Master pipeline

`RESEARCH → EVIDENCE → RESEARCH ID → COMPUTATIONAL MODEL → ALGORITHM FAMILY/VERSION → PARAMETERS/SEED → STAND-ALONE ARTWORK → PROVENANCE ARTWORK → RELEASE MANIFEST → HASHES → METADATA → IP/LICENCE GATE → RESEARCH REGISTRY ANCHOR → SMART CONTRACT → TESTNET DEPLOYMENT → TEST MINT → VERIFICATION → PRODUCTION MINT → BLOCKCHAIN PROVENANCE`

## Company algorithm network

Future computational-geometry NFTs are connected through a reusable Biupiu Algorithm Network rather than independent scripts.

Architecture record: `research/BIUPIU-COMPANY-ALGORITHM-NETWORK-v1.0.md`  
Algorithm registry: `research/BIUPIU-ALGORITHM-REGISTRY-v1.0.md`

The algorithm network has five development layers:

- **L0:** geometry primitives.
- **L1:** fields, graphs and structural systems.
- **L2:** research/domain models.
- **L3:** generative and transformation operators.
- **L4:** optimisation/AI where explicitly documented.
- **L5:** release renderer/export pipeline.

Algorithms evolve by version. Historical NFT releases retain the exact version used to generate them.

### ORIGIN-001 anchor

The first registered family is `BIU-ALG-GEO-FLOW-001`, the lineage of the existing `FLOW-GEOMETRY-001` prototype used by ORIGIN-001 / `BIU-NFT-0001`.

**Network rule: algorithms evolve; released records do not.**

## Asset pair standard

### A. Provenance image
Required: approved BIUPIU logo/emblem; approved BIUPIU colour system; research title and Research ID; evidence classification; computational method/algorithm ID; generation/version information where appropriate; restrained provenance panel; artwork preview; and no invented blockchain, token, hash or licence data.

### B. Stand-alone NFT image
Required principles: artwork-first composition; computational geometry meaningful to the research theme; subtle BIUPIU branding; no unnecessary provenance panel; no fake technical metadata embedded in the artwork; no unsupported archaeological claims; original composition derived from the recorded computational process.

## Brand lock

All releases inherit `brand/BIUPIU-NFT-BRAND-LOCK-v1.0.md`.

Working palette:
- Deep Forest `#063D2C`
- Biotech Emerald `#0E5A45`
- Teal Flow `#0F8C86`
- Warm Gold `#D4AF5A`
- Pale Gold `#E7D8A8`
- Soft Ivory `#F2EBDD`
- Carbon Black `#07110D`

The supplied BIUPIU banner and DNA/leaf/orbital emblem remain the master visual references.

## Collection structure

### BIUPIU / ORIGIN
Foundational Biupiu concepts and the origin story of the research-to-art system.

### BIUPIU / ANCIENT SYSTEMS
Documented or evidence-controlled ancient technologies translated through computational geometry.

Series: WATER, EARTH, STONE, METAL, SKY, NETWORK, LIFE, TRANSFORMATION.

### BIUPIU / GEOMETRY
Pure computational geometry and mathematically generated visual systems linked to research records.

Families: FRACTAL, PHYLLOTAXIS, VORONOI, TESSELLATION, NETWORK, SPIRAL, POLYHEDRA, FLOW, SYMMETRY, RECURSION, CELLULAR, MORPHOGENESIS.

### BIUPIU / REGENERATIVE SYSTEMS
Research-derived visualisations of regenerative agriculture, soil, water, biomass and ecological networks.

### BIUPIU / BIOLOGICAL SYSTEMS
Biological morphology, genetics/seed research, plant structures, cellular systems and biomimetic computational art, subject to evidence and IP controls.

### BIUPIU / ADVANCED SYSTEMS
Materials, energy, photonics, metamaterials, aerodynamics and other advanced computational research streams when cleared for public artistic representation.

## Web3 / smart-contract architecture

The repository contains an EVM minting layer:

- `contracts/BiupiuNFT.sol` — ERC-721 reference contract with capped supply, owner-controlled minting, batch minting, per-token URI and ERC-2981 royalty signalling.
- `hardhat.config.js` — development/testnet configuration.
- `package.json` — Hardhat, ethers, OpenZeppelin and dotenv tooling.
- `.env.example` — local-only configuration template; private keys must never be committed.
- `deploy-nft.js` — deployment workflow.
- `mint-nft.js` — mint workflow.
- `WEB3-MINTING.md` — operational Web3 documentation.
- `NFT-MINTING-ARCHITECTURE-v2.0.md` — blockchain architecture and governance.

### Initial development networks

- Ethereum Sepolia — chain ID 11155111.
- Polygon Amoy — chain ID 80002.

These are development/testnet targets. Mainnet deployment requires a separate release decision and verification gate.

## Biupiu blockchain network

The initial blockchain network is an EVM anchoring/registry layer, not a claim that Biupiu has launched an independent Layer-1 blockchain.

Architecture record: `research/BIUPIU-BLOCKCHAIN-REGISTRY-ARCHITECTURE-v1.0.md`

Planned separation:

1. **BiupiuNFT** — ownership, token IDs and token metadata.
2. **BiupiuResearchRegistry** — planned registry for research/algorithm/release hash commitments.
3. **GitHub** — canonical source, algorithm, documentation, release and reproducibility record.

The registry should anchor identifiers and hashes rather than confidential research or unpublished IP.

## On-chain vs off-chain

On-chain: token ownership, token URI, supply constraints, mint events, royalty signalling and, when implemented, approved research/release hash anchors.

Off-chain/content-addressed: research, source genealogy, artwork files, provenance records, algorithms, datasets, licences and detailed IP documentation.

## Release numbering

NFT IDs remain globally sequential: `BIU-NFT-0001`, `BIU-NFT-0002`, etc.

Collection release IDs use: `ORIGIN-001`, `ANCIENT-001`, `GEOMETRY-001`, etc.

Algorithm families are separately versioned and reusable across releases.

Every release must have at least one Research ID and may cross-link multiple Research IDs.

## Evidence classes

DOCUMENTED, RECONSTRUCTED, EXPERIMENTAL, HYPOTHESIS, SPECULATIVE.

The artwork must not visually imply a stronger evidence class than the underlying record supports.

## IP boundary

NFT ownership does not transfer Biupiu patents, inventions, trademarks, confidential information, source code, research datasets, commercial rights or future inventions unless an explicit licence says otherwise.

## Mint readiness gate

Before public minting:

1. final stand-alone image approved;
2. final provenance image approved;
3. research/source genealogy frozen;
4. evidence classification confirmed;
5. source/code/image licences cleared;
6. IP/patent sensitivity reviewed;
7. algorithm family/version frozen;
8. parameters and seed recorded;
9. metadata/release manifest frozen;
10. both asset hashes recorded;
11. token URI/content-addressed files pinned;
12. contract reviewed/tested;
13. research registry anchor prepared/verified where implemented;
14. testnet deployment completed;
15. test mint completed and metadata resolved;
16. contract source verified where supported;
17. deployment address and chain ID recorded;
18. final licence and collector terms approved;
19. production mint authorised.

## Image generation rule

When image generation is available, each release generates the pair:

`01_PROVENANCE` + `02_STANDALONE`

Both receive separate hashes and are linked to the same release record. If either image changes, its version/hash is updated independently.

## Current implementation

ORIGIN-001 / BIU-NFT-0001 remains the pilot. Its deterministic SVG is the canonical computational prototype. The two-image architecture, reusable algorithm network and planned blockchain registry now govern its future finalisation and all subsequent releases.

**No production blockchain deployment or mint is represented by this architecture update.**
