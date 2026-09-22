# Biupiu Verified Harvest Changelog — 2026-09-22

## CHG-2026-09-22-001
- **Change:** Added `BIUPIU-VERIFIED-HARVEST-AND-PROMOTION-PROTOCOL-v1.0.md`.
- **Reason:** Standardise evidence-based harvesting, repository cross-linking, version comparison, quarantine, regression testing and promotion.
- **Implementation status:** REGISTERED / SPECIFICATION ADDED.
- **Runtime status:** NOT EXECUTED in this session.
- **Bug fixes:** No runtime bug fix claimed; no test failure was independently reproduced.
- **Learning update:** Schema defined for maintenance and failure-learning events; no autonomous learning run claimed.
- **Blockchain update:** Anchoring boundary defined; no on-chain write performed.
- **Open gates:** Repository-wide module inventory, version comparison, dependency audit, test execution, security/licence review and cross-system regression remain pending.


## CHG-2026-09-22-002
- **Change:** Reconciled distributed module-harvest testing protocols into a canonical registry and hardened the executable harvest promotion gate.
- **Reason:** Recent module testing rules were present but not surfaced together, and the native gate did not enforce every documented promotion stage.
- **Implementation:** Added `research/BIUPIU-HARVEST-MODULE-TESTING-PROTOCOL-REGISTRY-2026-09-22.json`; extended `federation-harvest-gate.ts` and its test harness; extended cross-system CI workflow.
- **New enforced evidence:** version comparison, dependency check, normalisation, integration test, rollback reference.
- **Verification:** source-level consistency PASS; CI execution OPEN; no runtime/device pass claimed.
- **Learning:** gap recorded as a governance/indexing and enforcement mismatch; fix becomes regression input.
