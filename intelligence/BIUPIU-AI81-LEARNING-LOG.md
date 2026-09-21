# AI-81 Learning Log — Historical Search Protocol Audit

## Learning events

1. **Semantic collision detected:** shared words such as search, harvest, federation, research, and audit can represent different retrieval goals. Decision: require a semantic fingerprint rather than lexical matching.
2. **Provenance retention:** a protocol definition must retain path, heading, commit, date context, and surrounding text reference. Decision: no detached normalized summary may replace the source reference.
3. **Promotion separation:** discovery and implementation are different states. Decision: enforce the staged promotion chain and block status jumps.
4. **Coverage honesty:** default-branch visibility is not proof of complete historical coverage across deleted branches or inaccessible objects. Decision: every audit reports its coverage and limitations.
5. **Blockchain integrity:** a prepared hash manifest is not an executed transaction. Decision: distinguish `MANIFEST_PREPARED`, `TRANSACTION_SUBMITTED`, and `TRANSACTION_VERIFIED`.

## Algorithmic controls

- semantic fingerprint: intent + source lanes + retrieval unit + evidence model + promotion gate + consumer
- duplicate handling: same fingerprint = candidate duplicate; changed scope or evidence rules = distinct version/family
- contradiction handling: preserve both records, link `conflicts_with`, and block automatic promotion
- learning rule: failures and corrections remain append-only; superseded instructions are never silently deleted

## Status

- Governance contract: IMPLEMENTED
- Machine-readable registry: IMPLEMENTED
- Historical exhaustive enumeration: PENDING coverage verification
- Runtime federation adapter: PENDING
- Automated benchmark/test harness: PENDING
- Blockchain transaction: PENDING authorized execution
