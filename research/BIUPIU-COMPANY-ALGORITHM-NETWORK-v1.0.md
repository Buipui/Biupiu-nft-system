# Biupiu Company Algorithm Network v1.0

**Status:** Active architecture specification  
**Date:** 16 September 2026  
**Primary track:** Biupiu computational geometry + NFT + Web3  
**Boundary:** Personal Biupiu R&D/NFT repository; separate from the immediate commercial DTIC/InvestSA funding library.

## Purpose

The Biupiu Company Algorithm Network is the reusable computational layer behind future NFT releases. Each new computational-geometry NFT is treated as a new node in a versioned algorithm lineage rather than as an isolated artwork.

The network keeps four linked identities distinct:

`RESEARCH ID → ALGORITHM ID/VERSION → ARTWORK RELEASE → BLOCKCHAIN RECORD`

This allows algorithms to evolve while preserving the exact algorithm, parameters, source commit and asset hash used for every historical NFT.

## Core network model

```text
BIUPIU RESEARCH GRAPH
        │
        ├── Research IDs
        │
        └── Evidence / source genealogy
                │
                ▼
      BIUPIU ALGORITHM NETWORK
        │
        ├── Geometry primitives
        ├── Domain models
        ├── Composition operators
        ├── Optimisation / AI layers
        └── Deterministic generation records
                │
                ▼
        NFT RELEASE MANIFEST
        │
        ├── 01_PROVENANCE
        ├── 02_STANDALONE
        ├── metadata.json
        └── SHA-256 hashes
                │
                ▼
       BIUPIU BLOCKCHAIN NETWORK
        │
        ├── NFT contract
        ├── Research/algorithm registry
        └── on-chain release events
```

## Algorithm lineage

Every algorithm receives an immutable identity and a mutable version lineage.

Recommended format:

- Algorithm family: `BIU-ALG-[DOMAIN]-[NUMBER]`
- Version: semantic version, e.g. `1.0.0`, `1.1.0`
- Release instance: `BIU-REL-[YEAR]-[NUMBER]`

Example:

- `BIU-ALG-GEO-FLOW-001` — Flow Geometry family
- `BIU-ALG-GEO-FLOW-001@0.1.0` — current ORIGIN-001 prototype lineage
- `BIU-ALG-GEO-FLOW-001@1.0.0` — future validated production-ready generation lineage

A version change must never overwrite the historical record used by an earlier NFT. New versions create new records.

## Algorithm layers

### L0 — Primitive geometry
Circles, arcs, splines, polygons, polyhedra, vectors, matrices, coordinate transforms, topology, mesh primitives.

### L1 — Field and structural systems
Flow fields, radial fields, Voronoi, tessellation, cellular systems, networks, symmetry, recursion, phyllotaxis and parametric surfaces.

### L2 — Research/domain models
Hydrology, terrain, biological morphology, ancient construction geometry, materials, photonics, aerodynamics, marine geometry and other research-linked models.

### L3 — Generative operators
Seeded noise, recursion, transformations, morphogenesis, constraint systems, procedural composition and deterministic variation.

### L4 — Optimisation/AI
Parameter search, surrogate models, optimisation, clustering, computer vision or generative-AI assistance where explicitly documented.

### L5 — Release renderer
The final renderer/export pipeline that creates the collector-facing asset and provenance presentation asset.

## NFT update rule

As more NFTs are created, the algorithm network is updated in this order:

1. Assign or reuse a Research ID.
2. Select an existing algorithm family or create a new family.
3. Increment algorithm version only when the algorithm itself changes.
4. Record parameters and seed for the individual artwork.
5. Generate the two-image pair.
6. Hash artwork, metadata and the release manifest.
7. Commit all source and records to GitHub.
8. Anchor the release on the selected EVM network using the registry contract.
9. Link the registry entry to the NFT token contract/token ID when minting occurs.

## Reusable computational geometry kernel

The network should progressively build a reusable kernel instead of duplicating code between NFTs. Candidate modules:

- `geometry/primitives`
- `geometry/fields`
- `geometry/graphs`
- `geometry/fractals`
- `geometry/tessellation`
- `geometry/parametric`
- `geometry/topology`
- `geometry/morphogenesis`
- `geometry/flow`
- `geometry/mesh`
- `geometry/render`

Each module should have its own version, tests where practical, dependencies, licence, and change record.

## ORIGIN-001 migration

The existing `FLOW-GEOMETRY-001` prototype becomes the first registered algorithm family in the company algorithm network.

Current lineage:

- Research: `BIU-ANC-001`
- Secondary research: `BIU-GEO-001`
- NFT: `BIU-NFT-0001`
- Existing generator: `releases/ORIGIN-001/algorithm/flow_geometry_001.py`
- Current prototype seed: `20260915`
- Current status: artistic/computational prototype; not an archaeological validation

No earlier NFT is retroactively altered when the family is improved.

## Blockchain architecture

The initial company network is an **EVM anchoring network**, not a new independent blockchain. GitHub remains the canonical development/provenance source, while EVM contracts provide tamper-evident public anchors for approved release records.

Recommended separation:

- `BiupiuNFT` — ownership and token metadata layer.
- `BiupiuResearchRegistry` — research/algorithm/release hash anchor layer.
- GitHub — source code, documentation, parameters, release manifests and historical versions.

This design reduces the amount of sensitive or changeable information that must be written on-chain while preserving verifiable commitments to the release state.

## IP boundary

The registry anchors hashes and identifiers. It does not publish confidential Biupiu IP, private datasets, trade secrets, unpublished patent claims or source material that the release process has not approved for publication.

An on-chain hash is a proof of a recorded value; it is not itself a transfer of ownership or a licence.

## Governance gates

A computational artifact can move through:

`DRAFT → COMPUTATIONAL TEST → ARTWORK CANDIDATE → PROVENANCE REVIEW → IP REVIEW → HASH LOCK → TESTNET ANCHOR → MINT APPROVAL → PRODUCTION RECORD`

Mainnet deployment and minting remain separate approvals from algorithm development.

## Network principle

**Algorithms evolve; records do not.**

Future NFTs may share algorithm families, but each released NFT must retain the exact algorithm version, parameters, seed, source commit and asset hash that generated it.
