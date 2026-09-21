# BuildPui Digital Twin + Architecture Simulator Integration Contract v1.0

Status: IMPLEMENTED — CONTRACT DRAFT / RUNTIME VERIFICATION OPEN
Date: 2026-09-21
Branch: buildpui/next-gate-contracts-2026-09-21

## Purpose

Define a repository-safe integration contract between the BuildPui architecture simulator, digital-twin records, composite-material evidence, and future physical-twin/runtime adapters.

This document is an architecture and data-contract artifact. It does not certify structural performance, code compliance, fire safety, durability, or physical engineering validation.

## Core lifecycle

SOURCE -> EVIDENCE -> MATERIAL_MODEL -> COMPONENT_MODEL -> ASSEMBLY_MODEL -> BUILDING_TWIN -> SIMULATION_RUN -> REVIEW -> VALIDATION_RECORD -> PROVENANCE -> RELEASE

No simulated, inferred, or proposed value may be promoted to observed or physically validated state without an explicit evidence-backed gate.

## Digital-twin state separation

- observed: measured or externally observed value with timestamp, sensor/source, units, and quality flag.
- desired: target or design intent supplied by an authorised actor.
- computed: deterministic calculation derived from declared inputs and equations.
- simulated: result produced by a named model, version, solver, mesh/configuration, and assumptions.
- validated: result correlated against an identified physical test or authoritative accepted benchmark.
- actuated: command actually issued to an approved device/system; prohibited in this phase unless a separate runtime and safety gate is passed.

AI outputs remain proposed, inferred, or flagged until promoted by a human-reviewed evidence gate.

## Required identifiers

Every promoted object must include:

- stable object ID and object type
- parent/child and spatial relationships
- schema version
- source and provenance references
- licence/usage status
- author and timestamp
- units and coordinate reference where relevant
- uncertainty and assumptions
- evidence state: UNREVIEWED, CATALOGUED, RESEARCH-SUPPORTED, SIMULATION-READY, SIMULATION-EXECUTED, PHYSICALLY-TESTED, VALIDATED, or REJECTED
- unresolved contradictions and open questions

## Minimum object classes

1. SiteTwin
2. BuildingTwin
3. SpaceTwin
4. EnvelopeAssembly
5. StructuralComponent
6. CompositeMaterialCard
7. FabricationProcess
8. SensorObservation
9. SimulationModel
10. SimulationRun
11. EvidenceRecord
12. ValidationRecord
13. ProvenanceRecord
14. LicensingRecord
15. SafetyReview

## CompositeMaterialCard minimum fields

- material_id
- constituent materials and volume/mass fractions
- manufacturing process and cure/print conditions
- density and moisture condition
- thermal conductivity and test condition, if available
- mechanical properties with directionality and test standard, if available
- fire behaviour classification or explicit UNKNOWN state
- acoustic properties, if available
- durability/environmental exposure assumptions
- recycled/biogenic content and calculation boundary
- source DOI/URL and licence
- measured vs assumed vs simulated labels
- applicability limitations

Missing properties must be represented as UNKNOWN, not estimated silently.

## Simulation acceptance rules

- Inputs must declare units, coordinate system, boundary conditions, and assumptions.
- Each run must record model version, solver/configuration, mesh or discretisation information where applicable, and deterministic seed where relevant.
- Outputs must include convergence/error information and a reproducibility reference.
- Contradictory evidence is retained and marked OPEN; it is not silently averaged away.
- Safety-critical conclusions require qualified human review and appropriate physical testing.
- No actuation adapter is enabled by this contract.

## Research federation and licensing

ResearchGate, Emerald Insight, and House & Home references are metadata/context sources only unless a compatible licence or permission explicitly allows further use.

Permitted default harvesting:

- title, authors, date, DOI/URL, abstract-level short notes where lawful, keywords, source, licence indicator, and relevance mapping.

Not permitted by default:

- bulk copying of protected full text, images, product photography, product descriptions, paywalled tables, or proprietary datasets.

House & Home records are limited to reference metadata, category/context tags, and links. They are not treated as engineering evidence unless an independent technical source supports the claim.

## Gate record

### Completed / implemented in this branch

- Integration contract created.
- Digital-twin state separation specified.
- Material/evidence/provenance requirements specified.
- Simulation-before-actuation boundary specified.
- Licensing and protected-content restrictions specified.
- Open validation states and contradiction handling specified.

### Verified

- File created on the dedicated BuildPui integration branch.
- Contract is documentation-level and makes no physical-validation claim.

### Open

- Implement typed schemas (JSON Schema or equivalent).
- Add machine-readable example records.
- Add validation tests and schema linting.
- Connect repository adapters to an executable simulator/runtime.
- Verify IFC/OpenUSD interoperability in the host environment.
- Perform numerical, physical, safety, and regulatory validation through qualified workflows.
- Review all source records for licence and provenance completeness.

## Promotion decision

PROMOTION-READY FOR SCHEMA IMPLEMENTATION ONLY.
RUNTIME, PHYSICAL VALIDATION, ACTUATION, AND STATUTORY APPROVAL REMAIN OPEN.
