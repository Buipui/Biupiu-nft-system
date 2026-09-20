# BIUPIU FIREFLY SYSTEM INTEGRATION CONTRACT v1.0
## 20 September 2026

### Scope
Canonical integration boundary for Adobe Firefly across Biupiu OS, Biupiu AI, Intelligence, Blockchain provenance and Gate-Learning.

### Hard-coded integration rules
1. Firefly is a creative-generation service, never an authoritative OS state source.
2. Requests enter through an explicit Creative AI adapter; outputs are quarantined until validation.
3. Biupiu AI may propose prompts, variants and transformations, but cannot bypass OS validation, licence checks or release authority.
4. Every executed Firefly job records intent, tool/version context when available, result state, asset reference, validation state and failure evidence.
5. Failures become regression/test cases; successful repetition alone is not treated as learning.
6. Only approved hashes, identifiers and manifests may be anchored on-chain; private research, secrets and unpublished IP remain off-chain.
7. Generated assets receive a stable internal Research/Asset ID before release promotion.
8. IMPLEMENTED, EXECUTED, VERIFIED and PROMOTED remain separate states.
9. Contradictory status records resolve in favour of newest directly observed execution evidence; historical records remain immutable.
10. Production, release and IP decisions remain human-controlled.
11. Secrets, credentials and private keys never enter prompts, metadata or blockchain records.
12. Failed generation, invalid asset, policy/tool error or repository-sync failure blocks promotion but does not delete evidence.

### Integration pipeline
USER/AI INTENT -> FIREFLY ADAPTER -> GENERATION -> ASSET ID -> SAFETY/LICENCE/FORMAT VALIDATION -> VISUAL QA -> PROVENANCE MANIFEST -> INTELLIGENCE LEARNING EVENT -> OPTIONAL HASH ANCHOR -> RELEASE/PROMOTION

### Subsystem mappings
- Biupiu OS: Creative AI Adapter and validation boundary.
- Biupiu AI: prompt orchestration, candidate generation and non-authoritative recommendations.
- Biupiu Intelligence: event ledger, evidence classification, regression retrieval and diagnostics.
- Blockchain: optional immutable commitment layer after approval.
- Learning Algorithm: failure-to-test conversion, regression memory and promotion history.
- Biupiu World / Visual Systems: Firefly output enters the same asset ID, visual QA and provenance workflow.

### Visual Index
Firefly-generated visual assets are indexed by: Asset ID -> source/generation context -> visual category -> dimensions/format -> visual QA -> licence/IP status -> research linkage -> hash -> release state.

**Status: ARCHITECTURE INTEGRATED / DOCUMENTED. Runtime cross-system execution remains a separate verification gate.**
