# 📁 BIU NFT System — Repository Structure

## Overview

This document explains the organization of the Biupiu NFT System repository. The structure reflects the complete **Research → Algorithm → Artwork → Metadata → Blockchain** pipeline.

---

## 🏗️ Top-Level Architecture

```
Biupiu-nft-system/
├── 📄 Core Documentation
│   ├── README.md                          # Project overview
│   ├── LAUNCH-PLAN.md                     # Dual-asset model launch strategy
│   ├── MASTER-TEMPLATE.md                 # Master record template for all artifacts
│   ├── INVENTION-REGISTER.md              # IP/invention tracking
│   ├── FOUNDING-CROWDFUNDING-BRIEF.md     # Public crowdfunding campaign
│   ├── NFT-MINTING-ARCHITECTURE-v2.0.md   # Blockchain architecture
│   ├── WEB3-MINTING.md                    # Deployment & minting guide
│   └── WEB3-SECURITY.md                   # Security best practices
│
├── 🔬 Research & Documentation
│   └── research/
│       ├── INDEX.md                       # Master research index
│       ├── BIUPIU-COMPANY-ALGORITHM-NETWORK-v1.0.md
│       ├── BIUPIU-ALGORITHM-REGISTRY-v1.0.md
│       ├── BIUPIU-BLOCKCHAIN-REGISTRY-ARCHITECTURE-v1.0.md
│       └── NFT-ANCIENT-SYSTEMS-COMPUTATIONAL-GEOMETRY.md
│
├── 🎨 Artwork & Provenance
│   ├── artworks/
│   │   ├── README.md
│   │   ├── provenance/
│   │   │   └── BIUPIU-NFT-PROVENANCE-ARTPIECE-MASTER-REFERENCE-v1.0.md
│   │   ├── genesis/
│   │   │   ├── BIU-ART-0001-A-provenance.md
│   │   │   └── BIU-ART-0001-A-source.txt
│   │   └── collections/
│   │       └── [future collections]
│   │
│   ├── nft-metadata/
│   │   ├── README.md                      # Metadata standards
│   │   ├── BIU-ART-0001-A.json            # Genesis artwork metadata
│   │   ├── BIU-COA-0001.json              # Genesis certificate metadata
│   │   └── [future NFT metadata files]
│   │
│   └── docs/
│       ├── landing/
│       │   └── index.html                 # Public-facing landing page
│       ├── TESTNET-CHECKLIST.md           # Deployment validation checklist
│       ├── DUAL-ASSET-MODEL.md            # Technical specification
│       └── imagery/
│           ├── biu-art-0001-a-preview.png
│           └── biu-coa-0001-preview.png
│
├── ⚙️ Smart Contracts
│   └── contracts/
│       ├── BiupiuNFT.sol                  # ERC-721 NFT contract
│       ├── BiupiuCertificate.sol          # Certificate of Authenticity contract
│       ├── BiupiuResearchRegistry.sol     # Registry/anchoring contract
│       └── BiupiuProvenanceRegistry.sol   # Dual-asset bonding registry
│
├── 🧪 Testing & Deployment
│   ├── tests/
│   │   ├── BiupiuNFT.test.js
│   │   ├── BiupiuCertificate.test.js
│   │   ├── BiupiuResearchRegistry.test.js
│   │   └── dual-asset-bond.test.js
│   │
│   ├── deploy/
│   │   ├── deploymentConfig.json
│   │   ├── deployment-log.md
│   │   └── testnet-addresses.json
│   │
│   ├── hardhat.config.js                 # Hardhat configuration
│   ├── deploy-nft.js                     # Deployment script
│   ├── deploy-registry.js                # Registry deployment
│   └── mint-nft.js                       # Minting script
│
├── 📦 Configuration
│   ├── package.json                      # Node dependencies
│   ├── .env.example                      # Environment template
│   ├── .gitignore                        # Git ignore rules
│   └── .github/
│       └── workflows/
│           └── [CI/CD pipelines]
│
├── 🏛️ Collections & Releases
│   ├── releases/
│   │   ├── README.md
│   │   ├── GENESIS-0001/
│   │   │   ├── release-manifest.json
│   │   │   ├── BIU-ART-0001-A-manifest.md
│   │   │   ├── BIU-COA-0001-manifest.md
│   │   │   └── hashes.json
│   │   └── [future releases]
│   │
│   └── collections/
│       ├── README.md
│       ├── GENESIS/
│       │   ├── collection-config.json
│       │   └── metadata.json
│       └── [future collections]
│
├── 🎯 Brand & Marketing
│   └── brand/
│       ├── README.md
│       ├── style-guide.md
│       ├── logos/
│       └── templates/
│
├── 📚 Codex & Knowledge Base
│   └── codex/
│       ├── README.md
│       ├── GLOSSARY.md
│       ├── ALGORITHM-REGISTRY.md
│       └── RESEARCH-LINKS.md
│
└── 📋 Metadata Archive
    └── metadata/
        ├── README.md
        └── [legacy metadata storage]
```

---

## 📂 Directory Descriptions

### **Root Level** — Project Identity

| File | Purpose | Updated |
|------|---------|----------|
| `README.md` | Project overview & philosophy | Every major version |
| `MASTER-TEMPLATE.md` | Template for all research records | v1.0 |
| `LAUNCH-PLAN.md` | Genesis dual-asset launch strategy | Current |
| `INVENTION-REGISTER.md` | IP & invention tracking | As needed |
| `FOUNDING-CROWDFUNDING-BRIEF.md` | Public campaign brief | v1.0 |
| `NFT-MINTING-ARCHITECTURE-v2.0.md` | Blockchain architecture | v2.0 |
| `WEB3-MINTING.md` | Deployment instructions | Current |
| `WEB3-SECURITY.md` | Security guidelines | v1.0 |

---

### **research/** — Research & Architecture

| File | Purpose |
|------|----------|
| `INDEX.md` | Master index of all research projects |
| `BIUPIU-COMPANY-ALGORITHM-NETWORK-v1.0.md` | Versioned algorithm families |
| `BIUPIU-ALGORITHM-REGISTRY-v1.0.md` | Algorithm versioning rules |
| `BIUPIU-BLOCKCHAIN-REGISTRY-ARCHITECTURE-v1.0.md` | On-chain anchoring design |
| `NFT-ANCIENT-SYSTEMS-COMPUTATIONAL-GEOMETRY.md` | Ancient tech × geometry stream |

**Rules:**
- Version all architecture documents
- Never silently update — create new versions
- Cross-reference with MASTER-TEMPLATE.md

---

### **artworks/** — Creative & Provenance Records

**Subdirectories:**

- **`provenance/`** — Reusable provenance templates
  - `BIUPIU-NFT-PROVENANCE-ARTPIECE-MASTER-REFERENCE-v1.0.md` — canonical standard
  
- **`genesis/`** — First NFT pair records
  - `BIU-ART-0001-A-provenance.md` — Artwork documentation
  - `BIU-ART-0001-A-source.txt` — Source/seed data
  
- **`collections/`** — Organized by collection
  - Example: `collections/ANCIENT-SYSTEMS/` for future collections

**Rules:**
- One directory per major artwork/collection
- Include both 01_PROVENANCE and 02_STANDALONE documentation
- Reference corresponding metadata in `nft-metadata/`

---

### **nft-metadata/** — Metadata & Standards ✅ NEW

| File | Purpose |
|------|----------|
| `README.md` | Metadata standards & naming convention |
| `BIU-ART-0001-A.json` | Genesis artwork metadata |
| `BIU-COA-0001.json` | Genesis certificate metadata |

**Naming Convention:** `BIU-[TYPE]-[NUMBER]-[VARIANT].json`
- `BIU-ART-XXXX-A.json` — Artwork NFT
- `BIU-COA-XXXX.json` — Certificate NFT

**Rules:**
- All metadata versioned in JSON
- Include dual-asset bond information
- Maintain immutability (never edit released metadata)

---

### **docs/** — Public Documentation ✅ NEW

**Subdirectories:**

- **`landing/`** — Web presence
  - `index.html` — Public-facing dual-asset showcase
  
- **`imagery/`** — Asset previews
  - `biu-art-0001-a-preview.png` — Artwork preview
  - `biu-coa-0001-preview.png` — Certificate preview

**Files:**
- `TESTNET-CHECKLIST.md` — Deployment validation ✅ NEW
- `DUAL-ASSET-MODEL.md` — Technical specification

---

### **contracts/** — Smart Contracts

| Contract | Purpose |
|----------|----------|
| `BiupiuNFT.sol` | ERC-721 minting (existing) |
| `BiupiuCertificate.sol` | Certificate token |
| `BiupiuResearchRegistry.sol` | Hash anchor layer |
| `BiupiuProvenanceRegistry.sol` | Dual-asset bonding |

**Rules:**
- Use OpenZeppelin for base implementations
- Full test coverage required
- Document all public functions

---

### **tests/** — Test Suites

| File | Tests |
|------|-------|
| `BiupiuNFT.test.js` | Minting, URI, royalties |
| `BiupiuCertificate.test.js` | Certificate functions |
| `BiupiuResearchRegistry.test.js` | Registry operations |
| `dual-asset-bond.test.js` | Bonding mechanism |

**Target:** >90% coverage

---

### **deploy/** — Deployment Records

| File | Purpose |
|------|----------|
| `deploymentConfig.json` | Network & contract settings |
| `deployment-log.md` | Testnet deployment history |
| `testnet-addresses.json` | Deployed contract addresses |

---

### **releases/** — Collection Manifests

**Structure:**
```
releases/
├── GENESIS-0001/
│   ├── release-manifest.json      # Collection metadata
│   ├── BIU-ART-0001-A-manifest.md # Artwork record
│   ├── BIU-COA-0001-manifest.md   # Certificate record
│   └── hashes.json                # SHA-256 commitments
└── [future releases]
```

**Rules:**
- One directory per release
- Manifest = immutable record of published assets
- Hash all files for blockchain anchor

---

### **collections/** — Collection Configuration

**Structure:**
```
collections/
├── GENESIS/
│   ├── collection-config.json
│   └── metadata.json
└── [future collections]
```

---

### **codex/** — Knowledge Base

| File | Purpose |
|------|----------|
| `README.md` | Codex overview |
| `GLOSSARY.md` | Terminology & definitions |
| `ALGORITHM-REGISTRY.md` | Algorithm families & versions |
| `RESEARCH-LINKS.md` | External research sources |

---

### **brand/** — Branding & Marketing

| Directory | Purpose |
|-----------|----------|
| `logos/` | BIU logo files (SVG, PNG) |
| `templates/` | Marketing templates |
| `style-guide.md` | Brand guidelines |

---

## 🔄 Data Flow Through the Repository

```
1. RESEARCH INPUT
   └→ research/ (document research)
   └→ MASTER-TEMPLATE.md (record structure)

2. ALGORITHM DEVELOPMENT
   └→ BIUPIU-COMPANY-ALGORITHM-NETWORK-v1.0.md (version algorithm)
   └→ contracts/ (implement on-chain)

3. ARTWORK GENERATION
   └→ artworks/genesis/ (record artwork)
   └→ docs/imagery/ (store previews)

4. METADATA CREATION
   └→ nft-metadata/ (create JSON)
   └→ Validate against README.md standards

5. RELEASE PREPARATION
   └→ releases/GENESIS-0001/ (create manifest)
   └→ Generate hashes.json

6. BLOCKCHAIN DEPLOYMENT
   └→ deploy/ (store addresses)
   └→ BiupiuResearchRegistry (anchor hashes)
   └→ BiupiuNFT (mint tokens)

7. RELEASE PUBLICATION
   └→ collections/ (finalize)
   └→ docs/landing/ (public page)
```

---

## 📋 File Organization Checklist

### Before Testnet Deployment
- [ ] All research documented in `research/`
- [ ] All artwork in `artworks/genesis/`
- [ ] All metadata in `nft-metadata/`
- [ ] All contracts in `contracts/` with tests
- [ ] Release manifest in `releases/GENESIS-0001/`
- [ ] Deployment config in `deploy/`
- [ ] Public docs in `docs/`

### Before Mainnet Deployment
- [ ] All above ✅
- [ ] Testnet deployment addresses in `deploy/testnet-addresses.json`
- [ ] Security review documented
- [ ] Gas estimates calculated
- [ ] IPFS links verified
- [ ] Landing page live and tested

---

## 🚀 Key Principles

1. **Versioning** — All documents are versioned; never silently update
2. **Immutability** — Released metadata never changes
3. **Traceability** — Every artifact links back to research
4. **Separation** — Research (private) vs. Public (published)
5. **Canonical Source** — GitHub is the source of truth for provenance
6. **Blockchain Anchoring** — Hashes recorded on-chain for verification

---

**Last Updated:** September 16, 2026  
**Maintainer:** BIU Studio  
**Version:** 1.0


---

## 🧭 System-wide organization and authority boundaries — 22 September 2026

The repository has grown beyond the original NFT-only structure. The following top-level domains are now the maintained organization model:

| Domain | Canonical role | Authority boundary |
|---|---|---|
| `research/` | evidence, hypotheses, architecture, governance, provenance | evidence is not executable authority by publication alone |
| `intelligence/` | retrieval, classification, routing, learning diagnostics, orchestration indexes | AI/proposals cannot bypass OS validation |
| `software/` | Core OS, AI, mobile/web and Digital Orchestra implementations | executable authority remains versioned and tested |
| `core/` / `packages/` | native interfaces and shared contracts | contract ownership is explicit; no silent semantic merges |
| `digital-twin/` | state/twin representations and events | does not become physical truth |
| `simulators/` | domain models, numerical analysis and adapters | simulation is not physical certification without correlation |
| `world/` | World research/specifications and current staging material | dedicated World runtime belongs in `Buipui/Buipui-World` after controlled migration |
| `contracts/` / `payment/` | NFT/EVM, provenance, entitlement/payment boundaries | no client-side authority or unverified production claims |
| `tests/` / `.github/workflows/` | verification and CI gates | passing source inspection is not equivalent to runtime verification |

### Canonical federation flow

`RESEARCH/EVIDENCE → INTELLIGENCE → DIGITAL ORCHESTRA → CORE OS/DMS VALIDATION → DIGITAL TWIN/FEDERATION → DOMAIN SIMULATOR/ADAPTER → OBSERVATION → LEARNING EVIDENCE → REGRESSION → RELEASE/HUMAN GATE`

### World consolidation rule

Existing `world/` content is classified into runtime, asset, simulation, research, shared-contract, speculative and legacy lanes before migration. It is **not** blindly duplicated into the dedicated World repository. The migration manifest is:

`research/BIUPIU-WORLD-REPOSITORY-MIGRATION-MANIFEST-v1.0.md`

### Evidence / harvest rule

External repositories, foreign-language sources, OEM material, generated code and simulator results remain reference/pattern/adapter candidates until provenance, licence/IP, security, compatibility, build, smoke and regression gates are satisfied. Conflicting semantics are preserved and reconciled explicitly rather than silently merged.

### Verification state

Current structural organization is implemented. World runtime migration, full cross-system runtime execution, device/emulator verification, hardware/physical correlation and release verification remain open until evidence exists.

**Organization version:** 1.1  
**Last updated:** 22 September 2026
