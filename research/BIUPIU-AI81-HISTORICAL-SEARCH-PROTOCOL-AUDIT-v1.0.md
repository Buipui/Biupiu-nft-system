# BIUPIU AI-81 — Historical Search-Protocol Audit v1.0

**Audit window:** repository inception through 2026-09-21  
**Scope:** README files, research/index documents, protocol manifests, changelogs, workflow declarations, and prior gate records.

## Purpose

Identical words do not imply identical search protocols. AI-81 therefore classifies protocols by **semantic intent, source lane, retrieval unit, query expansion, evidence rules, promotion rules, and execution boundary**, not by matching labels alone.

## Required audit record

Each discovered protocol must record:

- `protocol_id`, `version`, `first_seen_commit`, `last_seen_commit`
- `file_path`, `heading_or_anchor`, `date_context`
- `semantic_intent`
- `source_lanes`
- `query_dimensions`
- `retrieval_unit`
- `language_strategy`
- `provenance_requirements`
- `evidence_states`
- `licence_security_rules`
- `promotion_gate`
- `downstream_consumers`
- `supersedes`, `superseded_by`, `conflicts_with`
- `implementation_state`, `verification_state`

## Semantic protocol families

| Family | Distinguishing function | Must not be collapsed into |
|---|---|---|
| Repository-first | Searches Biupiu history, indexes, and canonical records before external discovery | General web search |
| GitHub/code harvest | Finds repositories, files, commits, code, licences, and implementation evidence | Scholarly discovery |
| Standards retrieval | Locates exact editions, applicability, requirements, and conformity evidence | General technical research |
| Scholarly/scientific | Retrieves papers, metadata, citations, methods, and reproducible evidence | Historical ethnography |
| Anthropology/archaeology | Preserves culture/site/period/collector/context and paragraph-level provenance | Generic keyword search |
| Foreign-language federation | Expands terms across languages while retaining original-language evidence | Automatic translation-as-proof |
| OEM/industrial | Searches manufacturer, protocol, component, diagnostics, and service documentation | Open-source code search |
| OpenBooks/public-domain | Searches open texts and archival material with rights and edition controls | Licensed/paywalled corpus bypass |
| Patent/prior-art | Searches claims, families, dates, jurisdictions, and legal status | Scientific validation |
| Simulation/validation | Searches models, assumptions, test conditions, residuals, and failure modes | Discovery-only retrieval |
| Security/audit | Searches vulnerabilities, controls, threat models, test evidence, and remediation history | Functional feature search |
| Repository housekeeping | Detects duplicates, stale claims, contradictions, unsupported statuses, and leakage | Research discovery |

## Federation decision rule

A protocol is considered the same only when its semantic fingerprint matches across: intent, source lane, retrieval unit, evidence model, promotion gate, and consumer. Shared vocabulary is insufficient.

## Hard implementation contract

`DISCOVERED -> IDENTIFIED -> PROVENANCE_CHECKED -> LICENCE_CHECKED -> SECURITY_CHECKED -> COMPATIBILITY_CHECKED -> TESTED -> REVIEWED -> IMPLEMENTED -> VERIFIED`

No search result, README phrase, citation count, star count, or semantic similarity may independently promote an item to implementation or verification.

## Readme/history audit procedure

1. Enumerate all branches and the default branch.
2. Enumerate commits from the repository's earliest reachable commit to the audit timestamp.
3. Inspect every README-like file and every file containing search, harvest, federation, protocol, research, query, source, evidence, audit, or learning instructions.
4. Extract protocol statements with file path, heading, commit, and surrounding context.
5. Normalize wording but preserve the original text reference.
6. Generate semantic fingerprints and detect duplicates, refinements, supersession, and contradictions.
7. Reconcile the master index, README, learning log, changelog, and machine-readable registry.
8. Run tests for schema validity, missing provenance fields, illegal status jumps, duplicate fingerprints, and unsupported blockchain claims.

## Evidence limitation

A connector-accessible commit listing and current default-branch tree are evidence for the accessible history, but they do not by themselves prove that every historical branch, deleted ref, or inaccessible object was retrieved. The audit must report coverage explicitly rather than claiming totality without a complete commit/ref inventory.

## Security and privacy

Never index secrets, private keys, credentials, confidential datasets, or unpublished IP. Do not bypass authentication, paywalls, robots rules, or licence restrictions. External code is untrusted until scanned, reviewed, and tested in isolation.

## Blockchain boundary

This protocol creates a deterministic anchor manifest containing release ID, protocol registry hash, audit coverage, commit SHAs, changelog IDs, learning-log IDs, and timestamp. The manifest is **not an on-chain transaction**. Actual blockchain anchoring remains pending an authorized wallet/network execution and independent transaction verification.
