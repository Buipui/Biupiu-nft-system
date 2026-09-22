# Biupiu Federated Repository Search Protocol v1.0
Date: 2026-09-21
Status: HARD-IMPLEMENTED AS RESEARCH/DISCOVERY GOVERNANCE
Gate: AI-70

## Purpose
Extend the existing Biupiu harvest protocol into a federated, evidence-governed search layer spanning the Biupiu repository, public Git repositories, standards/catalogue sources, scientific indexes, government/space research, and multilingual sources.

This is a discovery and evidence protocol. It does not grant authority to execute, copy, merge, or promote external material.

## Search federation
Canonical fan-out:

QUERY NORMALISATION
→ IDENTIFIER / EXACT-TERM SEARCH
→ LEXICAL SEARCH
→ SEMANTIC / CONCEPT SEARCH
→ DOMAIN-SOURCE SEARCH
→ MULTILINGUAL EXPANSION
→ REPOSITORY / CODE SEARCH
→ SOURCE FETCH
→ PROVENANCE CHECK
→ DEDUPLICATION
→ EVIDENCE CLASSIFICATION
→ CROSS-SOURCE CORROBORATION
→ LICENCE / SECURITY CHECK
→ LEARNING EVENT
→ CANDIDATE INTEGRATION
→ HARD PROMOTION GATE

## Source lanes
1. Biupiu repository/history
2. GitHub repository/code/search
3. Official standards publishers
4. Government and public-sector technical repositories
5. NASA/ADS and other authoritative scientific indexes
6. Scholarly metadata/search services
7. Open-access repositories
8. Official project/developer documentation
9. Foreign-language technical repositories
10. Community/discovery sources

Discovery sources may locate material; authoritative sources are required for final factual verification where available.

## Search protocol
Every query is expanded into:
- exact technical identifiers
- acronyms and long forms
- synonyms
- implementation terminology
- protocol/standard names
- relevant programming-language terms
- domain terms
- foreign-language equivalents
- transliterations where useful

English plus Arabic, Chinese, Japanese, Korean, German, Italian, French, Spanish, Portuguese and Russian are supported discovery lanes. Translation is an indexing aid only; original-language evidence is preserved for verification.

## Repository-first rule
For a Biupiu capability, search the Biupiu repository/history first. Existing contracts, schemas and implementations must be reused or extended before creating parallel authorities.

## External implementation rule
External code is never promoted because it was found, highly starred, frequently cited, or returned by semantic search. Promotion requires:
PROVENANCE → LICENCE → SECURITY → COMPATIBILITY → TEST → INTEGRATION → REVIEW → RELEASE.

## Result identity
Each result should retain:
source_id, source_type, repository/project, URL/reference, path or document identifier, title, author/organisation where available, publication/update date, language, query lineage, retrieval timestamp, licence/status, evidence class, corroboration set and promotion state.

## Evidence classes
ESTABLISHED — directly verified against an authoritative primary source.
SUPPORTED — independently corroborated or supported by authoritative secondary evidence.
PRELIMINARY — plausible candidate requiring verification.
HYPOTHESIS — unverified proposal or research lead.
REJECTED — contradicted, unsafe, incompatible, unlicensed, unverifiable or otherwise unsuitable.

## Ranking rule
Search ranking is not truth ranking. Relevance and source authority are separate dimensions. A highly relevant low-authority result must not outrank authoritative evidence during promotion.

Where multiple sources repeat the same claim, content identity and provenance are retained so corroboration does not become false independent evidence.

## Federated-search architecture references
The harvest adopts the architectural pattern demonstrated by open federated-search systems: fan-out to heterogeneous repositories, adapter/gateway translation, common metadata, result aggregation and source-specific query handling. OpenSearch is treated as an interoperability reference rather than a mandatory implementation dependency.

GitHub search is used for repository/code discovery and code navigation. Scientific discovery may use APIs/indexes such as NASA ADS. Semantic retrieval is an optional candidate lane and must remain auditable.

## Security / privacy
- Never index secrets, private keys, credentials or confidential datasets.
- Redact sensitive material before indexing where applicable.
- Do not bypass authentication, robots/access controls, paywalls or licence restrictions.
- Store only the minimum provenance needed to reproduce the research result.
- Treat fetched code as untrusted until scanned and reviewed.
- Search results never become executable instructions automatically.

## Learning integration
Every search, fetch, rejection, deduplication, corroboration, adoption and failure can emit a governed LearningEvent.

Minimum learning fields:
event_id, protocol_version, query_profile, source_ids, observation, evidence_class, decision, reason, test_result, licence_state, security_state, promotion_state, timestamp.

## Hard gate
No result may enter an IMPLEMENTED or VERIFIED state solely from search output.

Promotion chain:
DISCOVERED → IDENTIFIED → PROVENANCE-CHECKED → LICENCE-CHECKED → SECURITY-CHECKED → COMPATIBILITY-CHECKED → TESTED → REVIEWED → IMPLEMENTED → VERIFIED.

## Acceptance
AI-70 passes when:
- repository-first search is mandatory;
- multilingual expansion is mandatory for relevant international research;
- heterogeneous source adapters are defined;
- provenance and evidence classes are retained;
- deduplication/corroboration are explicit;
- licence/security gates block unsafe promotion;
- search cannot silently promote code or claims.

## Current state
Architecture: IMPLEMENTED
Repository protocol: HARD-IMPLEMENTED
External adapters: REFERENCE / NOT AUTOMATICALLY ENABLED
Runtime federation: PENDING
Automated retrieval evaluation: PENDING
