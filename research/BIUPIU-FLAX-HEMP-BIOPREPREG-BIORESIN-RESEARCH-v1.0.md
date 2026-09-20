# Biupiu Flax / Hemp Bio-Prepreg & Bio-Resin Research v1.0

**Date:** 20 September 2026  
**Status:** Research baseline — not a validated product specification

## Scope and routing

- **COMPOSITES:** flax fibre, hemp fibre, hybrid flax/hemp laminates, natural-fibre sandwich structures, fibre treatments, interfaces, moisture and ageing.
- **BIO-RESINS:** furan / polyfurfuryl alcohol (PFA), bio-epoxy, epoxidised vegetable-oil (EVO) systems, bio-polyesters, curing agents, additives, fire retardants and circular feedstocks.
- **Cross-links:** TEXTILES, COAT, MATERIALS, AUTOMOTIVE, BIOMASS, TESTING, DIGITAL-TWIN.
- **Record families:** `BPU-CMP-MAT-*`, `BPU-RES-*`, `BPU-SIM-CMP-*`, `BPU-SIM-RES-*`.

## Evidence baseline

### Flax composites

Flax is a high-specific-performance natural reinforcement with strong stiffness-to-weight potential, but performance is sensitive to fibre quality, alignment, moisture, porosity, fibre volume fraction, processing and interface chemistry. Research should compare woven, unidirectional, nonwoven and short-fibre formats rather than treating “flax” as one material.

### Hemp composites

Hemp reinforcement offers low density and useful specific mechanical properties. Hydrophilicity, variability in fibre extraction, lumen/porosity, fibre damage and fibre–matrix adhesion are primary design variables. Alkali, silane, enzymatic, plasma and physical treatments must be tracked as separate formulations with safety and environmental controls.

### Hemp bio-prepregs

The repository should treat hemp prepreg as a manufacturing system, not merely a resin/fibre pair. Required fields include fibre architecture, areal weight, resin content, tack/drape, storage conditions, out-time, consolidation pressure, cure schedule, void content and post-cure condition. Candidate processes: hot-melt impregnation, solution impregnation, vacuum-bag consolidation, compression moulding and resin infusion.

### Furan / PFA resins

Polyfurfuryl alcohol is attractive for renewable feedstock and fire-performance research. Published flax/furan work indicates lower mechanical performance than carbon/glass epoxy in some comparisons, while fire behaviour can be advantageous. Long-term water uptake, acidic degradation products, interface durability and processing shrinkage must be explicit test variables. Fire-retardant additions to the matrix and treatment of the fabric must be compared separately because fibre treatment can impair adhesion and water tolerance.

### Epoxidised vegetable oils

EVO-derived epoxies are a platform family rather than a single resin. Record oil source (soybean, linseed, sunflower, canola, etc.), oxirane content, functionality, viscosity, diluent, hardener, catalyst, bio-based carbon content, cure kinetics, glass-transition temperature, modulus, toughness, moisture response and ageing. Many systems remain only partially bio-based because curing agents and modifiers may be fossil-derived; report bio-content transparently rather than labelling the complete formulation “fully bio-based.”

### Hybrid and interfacial strategies

Priority comparisons:

1. untreated versus treated flax/hemp;
2. flax-only, hemp-only and flax/hemp hybrid layups;
3. bio-epoxy versus PFA/furan versus EVO-epoxy;
4. matrix-only fire retardant versus fibre treatment;
5. natural fibre versus basalt or glass hybrid control;
6. dry, humid, wet–dry cycling and thermal ageing;
7. vacuum infusion versus prepreg/compression processing.

## Minimum data schema

Each material record should include:

- material/resin ID and version;
- fibre species, cultivar/source, extraction method and treatment;
- fibre architecture, areal weight, orientation and fibre-volume fraction;
- matrix chemistry, bio-content, viscosity, cure chemistry and cure schedule;
- density, tensile/flexural/compressive properties, interlaminar shear strength;
- fracture toughness, impact, fatigue, creep and vibration properties;
- Tg, thermal decomposition, flammability/fire response;
- water uptake, humidity, UV, freeze/thaw and chemical ageing;
- manufacturing process, void content and defects;
- uncertainty range, source DOI/URL, evidence classification and licence;
- test method and specimen geometry, preferably mapped to ASTM/ISO standards.

## Test programme for Biupiu

**Screening:** density, fibre volume, resin content, moisture uptake, tensile, flexural, short-beam/interlaminar shear, DMA/Tg and microscopy.  
**Engineering:** compression, impact, fatigue, open-hole tension, buckling panels, thermal cycling, water immersion, salt-fog where relevant, fire screening and dimensional stability.  
**Manufacturing:** prepreg tack/drape, storage/out-time, consolidation pressure, cure kinetics, void fraction, repeatability and scrap rate.  
**Gate rule:** literature values are estimates until replicated on Biupiu feedstocks and process settings. Missing values remain unknown with uncertainty; they are never replaced by zero or silently copied from another resin.

## Research sources captured

- Islam et al., *Thermoset and thermoplastic polymer composites reinforced with flax fiber: Properties and application—A review* (2024/2025), DOI 10.1002/pls2.10172.
- Islam et al., *Mechanical properties of hemp fiber-reinforced thermoset and thermoplastic polymer composites: A comprehensive review* (2025), DOI 10.1002/pls2.10173.
- Kandola, *Fully bio-based flax/furan versus carbon/glass epoxy composites: Scope and limitations in terms of fire and physico-mechanical performances* (2024), DOI 10.1002/pc.28527.
- Shelly et al., *Mechanical performance of bio-based fiber reinforced polymer composites: A review* (2025), DOI 10.1002/pc.30000.
- Comparative flax/biopolymer woven composites and PFA prepreg research (Composites Part C, 2025), DOI-linked source record.

## Development status

This file is a research and engineering requirements baseline. It does not certify a formulation, structural suitability, fire rating, or regulatory compliance. All structural claims require specimen-level testing and independent review.
