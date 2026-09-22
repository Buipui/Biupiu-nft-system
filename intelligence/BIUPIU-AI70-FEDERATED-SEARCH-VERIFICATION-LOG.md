# AI-70 Federated Search Verification Log
Date: 2026-09-21

## Executed
- Repository-first search rule formalized.
- Federated source-lane model formalized.
- Multilingual query expansion formalized.
- Provenance, licence, security and compatibility gates made mandatory.
- Evidence classes separated from relevance/ranking.
- Deduplication and corroboration rules formalized.
- Search-to-promotion chain made fail-closed.
- Learning-event fields added for search/fetch/rejection/adoption/failure.
- External code explicitly prevented from silent promotion.

## Harvest evidence
- GitHub documentation confirms repository/global search and code-navigation capabilities.
- NASA ADS provides a developer API for search, metrics and export.
- Open Federated Search provides a documented example of heterogeneous repository fan-out, adapter translation, common metadata and aggregation.
- A current open-source federated AI-search example demonstrates literal/regex, lexical, semantic and hybrid retrieval plus trust-weighted fusion and content-hash deduplication; it is treated as an architectural research lead, not a dependency.

## Verification
ARCHITECTURE: PASS
REPOSITORY-FIRST: PASS
MULTILINGUAL ROUTING: PASS
PROVENANCE: PASS
LICENCE GATE: PASS
SECURITY GATE: PASS
EVIDENCE CLASSIFICATION: PASS
NO-SILENT-PROMOTION: PASS
RUNTIME FEDERATION: PENDING
AUTOMATED RETRIEVAL BENCHMARKS: PENDING
FULL EXTERNAL-ADAPTER IMPLEMENTATION: PENDING

## Learning event
Observation: heterogeneous repositories require adapter-specific query translation and normalized metadata before results can be aggregated safely.
Lesson: federation should normalize provenance and evidence without pretending that different source types have identical authority.
Confidence: SUPPORTED
Promotion: ARCHITECTURE_REFERENCE_ONLY

## Next gate
AI-71: machine-readable query-profile schema + adapter interface + retrieval benchmark corpus + repository-wide search audit.
