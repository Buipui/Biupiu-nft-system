# BIUPIU FEDERATION PROTOCOL v1.0

Status: MAINLINE — protocol implemented; external/runtime gates remain evidence-gated.

## Canonical authority hierarchy
HUMAN RELEASE AUTHORITY
-> BIUPIU CORE OS / DMS VALIDATION
-> DOMAIN OWNER
-> BIUPIU INTELLIGENCE
-> FEDERATION CONTROL / MULTI-AI LAYER
-> ADAPTER / PROVIDER
-> EXTERNAL REFERENCE

**Correction applied 22 September 2026:** Native Biupiu Intelligence is not the top-level authority. It may discover, classify, learn, route and propose. Core OS/DMS validation and the owning domain retain execution authority; human/release authority retains final promotion authority.

Executable contract: `software/rnd-os-ai/src/biupiu_ai/authority_hierarchy.py`.

## Federation sequence
RESTORE -> REGISTER -> FREEZE IDENTITIES -> DISCOVER AI SYSTEMS -> ROUTE -> VERIFY -> TEST -> FAILURE LEARN -> CORE OS/DMS VALIDATE -> HUMAN RELEASE -> PROMOTE

## AI-system discovery rule
The Federation must maintain a machine-readable registry of every canonical federation AI system.

Discovery must search, in order:
1. Canonical AI-team manifests and architecture specifications.
2. Federation protocol, registry, orchestration and adapter modules.
3. Historical AI gate/log records and supersession links.
4. World and NFT repositories plus linked repository records.
5. Prior conversation/library architecture records when repository evidence is incomplete.
6. External provider references only as reference/adapter candidates.

For every identified AI system record:
- canonical ID/name
- role and authority boundary
- repository path
- interface/adapter
- model/provider status
- evidence state
- licence/provenance state
- runtime verification state
- dependencies
- supersession/conflict links
- consuming systems
- promotion authority

Do not infer a canonical AI identity from a provider name, adapter, team role, or numbered gate. If evidence is insufficient, record DISCOVERY-PENDING rather than inventing an identity.

## Authority rule
Specialist systems are adapters/providers. They cannot directly modify authoritative Core OS state. AI/federation proposals require Core OS/DMS validation, and executable promotion additionally requires provenance, licence, security, regression/reproducibility and human approval.

## World boundary
Biupiu World consumes approved, versioned federation outputs, asset identity, Digital Twin events and approved contracts. World is not OS authority, simulator truth, physical certification authority, AI promotion authority, or NFT/EVM state authority.

## NFT / provenance boundary
The NFT system remains the provenance, algorithm-lineage and blockchain anchoring layer. Computational-geometry algorithms, artwork, manifests, source commits and hashes may be cross-linked to World assets through identifiers and approved manifests. Blockchain records do not override federation or OS authority.

## Quantum rule
Simulator-first; classical baseline required; no hardware activation or quantum-advantage claim without measured evidence.

## Multilingual rule
Original-language evidence is retained. Translation is an indexing/working aid, not evidence validation.

## External research rule
NASA/DARPA material remains external reference material unless redistribution rights and promotion gates are explicitly satisfied.

## Final state
Federation readiness is FAIL-CLOSED until every required gate has VERIFIED evidence.
