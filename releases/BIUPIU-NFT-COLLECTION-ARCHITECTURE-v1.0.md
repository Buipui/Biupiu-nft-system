# BIUPIU NFT COLLECTION ARCHITECTURE v1.0

**Effective:** 2026-09-16  
**Status:** ACTIVE COLLECTION STANDARD  
**Image generation:** PAUSED UNTIL AVAILABLE

## Purpose

This document establishes the production architecture for future BIUPIU NFT releases. Every release will produce two distinct visual assets from the same research/computational record:

1. **PROVENANCE EDITION IMAGE** — branded presentation image showing the research lineage and provenance context.
2. **STAND-ALONE NFT IMAGE** — collector-facing artwork with the research/computational geometry as the hero, designed to function independently without the provenance panel.

The two images are related but are never treated as interchangeable.

## Master pipeline

`RESEARCH → EVIDENCE → RESEARCH ID → COMPUTATIONAL MODEL → GENERATIVE ALGORITHM → PARAMETERS/SEED → STAND-ALONE ARTWORK → PROVENANCE ARTWORK → HASHES → METADATA → IP REVIEW → MINT GATE`

## Asset pair standard

### A. Provenance image

Purpose: document the relationship between BIUPIU, the research subject, computational method and collector asset.

Required visual components:
- approved BIUPIU logo/emblem;
- approved BIUPIU colour system;
- research title and Research ID;
- evidence classification;
- computational method/algorithm ID;
- generation/version information where appropriate;
- restrained source/provenance panel;
- artwork preview;
- no invented blockchain, token, hash or licence data.

### B. Stand-alone NFT image

Purpose: the collectible itself.

Required visual principles:
- artwork-first composition;
- computational geometry must be visually meaningful to the research theme;
- BIUPIU branding is integrated subtly and consistently;
- no large provenance panel unless the concept specifically requires it;
- no fake technical metadata embedded in the artwork;
- no unsupported archaeological claims;
- original composition derived from the recorded computational process.

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

Series:
- WATER
- EARTH
- STONE
- METAL
- SKY
- NETWORK
- LIFE
- TRANSFORMATION

### BIUPIU / GEOMETRY

Pure computational geometry and mathematically generated visual systems linked to research records.

Core families:
- FRACTAL
- PHYLLOTAXIS
- VORONOI
- TESSELLATION
- NETWORK
- SPIRAL
- POLYHEDRA
- FLOW
- SYMMETRY
- RECURSION
- CELLULAR
- MORPHOGENESIS

### BIUPIU / REGENERATIVE SYSTEMS

Research-derived visualisations of regenerative agriculture, soil, water, biomass and ecological networks.

### BIUPIU / BIOLOGICAL SYSTEMS

Biological morphology, genetics/seed research, plant structures, cellular systems and biomimetic computational art, subject to appropriate evidence and IP controls.

### BIUPIU / ADVANCED SYSTEMS

Materials, energy, photonics, metamaterials, aerodynamics and other advanced computational research streams when cleared for public artistic representation.

## Release numbering

NFT IDs remain globally sequential: `BIU-NFT-0001`, `BIU-NFT-0002`, etc.

Collection release IDs use: `ORIGIN-001`, `ANCIENT-001`, `GEOMETRY-001`, etc.

Every release must have at least one Research ID and may cross-link multiple Research IDs.

## Evidence classes

- DOCUMENTED
- RECONSTRUCTED
- EXPERIMENTAL
- HYPOTHESIS
- SPECULATIVE

The artwork must not visually imply a stronger evidence class than the underlying record supports.

## IP boundary

NFT ownership does not transfer Biupiu patents, inventions, trademarks, confidential information, source code, research datasets, commercial rights or future inventions unless an explicit licence says otherwise.

## Image generation rule

When image generation is available, each new release must generate the **two-image pair** in the same controlled session/production stage:

`01_PROVENANCE` + `02_STANDALONE`

Both assets receive separate hashes and are linked to the same release record. If either image is revised, its version and hash must be updated independently.

## Current implementation

ORIGIN-001 / BIU-NFT-0001 remains the pilot implementation. Its existing deterministic SVG is the canonical computational prototype. The new two-image architecture applies to ORIGIN-001's next visual revision and all subsequent releases.
