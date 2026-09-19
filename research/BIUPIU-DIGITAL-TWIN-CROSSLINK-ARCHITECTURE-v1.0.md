# Biupiu Digital Twin Cross-Link & Dependency Architecture v1.0

Date: 19 September 2026
Status: Architecture integration branch — schema/guardrail layer

## Purpose
Make the Digital Twin the cross-domain integration and dependency-observation layer so new research, algorithms, models, code, datasets, departments, economic systems and IP records cannot silently become orphaned.

## Core graph
Research -> Evidence -> Model -> Algorithm -> Software Component -> Digital Twin Asset -> Simulation -> Validation -> IP/Provenance -> Release

Parallel operational graph:
Department <-> Capability <-> Service <-> Data Contract <-> Digital Twin <-> Validation

Economic/IP graph:
Validated Output -> IP Record -> Provenance -> NFT (where approved) -> Blockchain Anchor

Commercial graph:
Validated Product -> Manufacturing -> Supply Chain -> Marketplace -> Treasury/BPU (where approved)

## Mandatory node classes
DEPARTMENT, RESEARCH, SOURCE, EVIDENCE, DATASET, MODEL, ALGORITHM, SOFTWARE, DIGITAL-TWIN, SIMULATION, SENSOR, ROBOT, GEOMETRY, MATERIAL, EXPERIMENT, VALIDATION, IP, NFT, BLOCKCHAIN-REGISTRY, BPU, TREASURY, MARKETPLACE, PRODUCT, MANUFACTURING, SUPPLY-CHAIN, COMMERCIAL, GOVERNANCE.

## Mandatory edge types
DEPENDS_ON, PRODUCES, CONSUMES, VALIDATES, DERIVES_FROM, IMPLEMENTS, SIMULATES, REPRESENTS, USES, VERSION_OF, EVOLVES_FROM, PROVENANCE_OF, ANCHORED_BY, SETTLES_THROUGH, FUNDS, MANUFACTURES, DEPLOYED_TO, ROUTES_TO, REQUIRES_REVIEW, PROMOTED_FROM, SUPERSEDES.

## Digital Twin rule
Every production-intended model, algorithm, engineering asset, sensor interface or simulation result that materially affects a domain must have a Digital Twin relationship or an explicit NO-TWIN-JUSTIFICATION record.

The Digital Twin does not imply that a physical twin exists. It may represent a computational system, proposed design, simulation object or monitored physical asset.

## Orphan detection
A repository integrity pass should flag:
1. Department with no capability/output mapping.
2. Algorithm with no owner department.
3. Model with no algorithm or documented source.
4. Digital Twin object with no model/data contract.
5. Simulation with no model/version.
6. Validation result with no experiment/model/version.
7. NFT with no approved provenance record.
8. Blockchain anchor with no release manifest.
9. BPU transaction component with no treasury/settlement policy.
10. Treasury component with no authorization/control policy.
11. Marketplace component with no BPU/payment interface.
12. Product with no manufacturing/supply-chain relationship where applicable.
13. External dependency with no licence/security status.
14. AI agent with no policy/authorization boundary.
15. Production component with no rollback/version lineage.

## Change propagation
When a dependency changes, the graph should identify impacted downstream nodes:
source -> model -> algorithm -> software -> twin -> simulation -> validation -> product/IP/release

A version change must not silently mutate historical records. New versions receive new IDs; old releases retain their lineage.

## Integration gates
DISCOVER -> CLASSIFY -> LICENCE -> INDEX -> ADAPT -> UNIT TEST -> INTEGRATION TEST -> DIGITAL-TWIN TEST -> DOMAIN VALIDATION -> PROVENANCE -> PROMOTION

Third-party code remains external until licence, security, dependency and compatibility checks pass.

## Department coverage
First-class cross-link targets include BIO, BIO-GEN, AGRI, HEMP, BIOCARBON, BIOCHEM, TEXTILES, COAT, COMPOSITES, MATERIALS, WATER, ENERGY, ELECTROMAG, PHOTONICS, PH-QPM, CRM, METAMATERIALS, AERO, MARINE, COMPUTE, MATH, AI, GEOMETRY, DIGITAL-TWIN, ROBOTICS, ADV-MFG, BIOMED, GEOARCH, LAND-GIS, ALA, AAT, AAT-H, PALAEO-COAST, EMPIRE-CULTURE, NAGA-HIM, OLMEC-AMR, PRE-DISASTER, GEO-MAG, SPEC, IP, NFT-ART, NFT-PROV, BPU, TREASURY, MARKETPLACE and BIUPIU-WORLD.

## Economic/IP cross-link
BPU, Treasury, Marketplace and NFT systems are not direct substitutes for engineering systems. They connect through validated release/provenance and commercial transaction interfaces.

NFTs represent approved digital assets/provenance records where applicable. Blockchain provides anchoring/verification/transaction infrastructure. Treasury governs authorized ecosystem funds. BPU is the planned settlement asset. Marketplace provides commercial transaction context.

No financial asset, contract, wallet or token is considered production-ready merely because its node exists in the architecture.

## Digital Twin control principle
The Digital Twin is the integration observer, not the sole authority.

Authoritative state remains in the relevant subsystem. The Digital Twin consumes versioned contracts and evidence, detects dependency gaps, runs/requests simulation or validation, and reports integration status.

## Required machine-readable future records
Recommended records:
- architecture/node-registry.json
- architecture/edge-registry.json
- architecture/interface-registry.json
- architecture/orphan-rules.json
- architecture/change-impact-rules.json
- architecture/department-capability-map.json
- architecture/digital-twin-contract.json

## Failure-learning rule
Failures become versioned evidence records:
failure -> cause hypothesis -> reproduction -> fix -> regression test -> affected graph nodes -> learning record

No failure record is silently deleted when resolved.

## Acceptance criterion
A department or subsystem is not considered fully integrated merely because it appears in an index. It must have:
- an owner/canonical record;
- defined inputs/outputs;
- at least one valid dependency path;
- interface/data contract where applicable;
- validation status;
- provenance/version lineage;
- explicit commercial/private-R&D boundary;
- Digital Twin mapping or documented exception.
