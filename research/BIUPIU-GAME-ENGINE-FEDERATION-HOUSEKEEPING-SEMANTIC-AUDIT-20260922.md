# Biupiu Game-Engine Federation — Housekeeping & Semantic Cross-Reference Audit
Date: 2026-09-22
Status: SOURCE-LEVEL HOUSEKEEPING COMPLETE / BUILD + RUNTIME EVIDENCE OPEN

## Scope
Internal repository cross-reference and semantic audit for the Cocos2d-x, Cocos Engine, MonoGame, Celeste reference, libGDX, Ashley ECS, raylib, Three.js, GDevelop and Babylon.js federation lanes targeting BuipuiOS and buipiu mini OS.

## Internal evidence located
- Federation protocol and authority hierarchy.
- Federation module manifest and quarantine policy.
- Mini OS federation C ABI and runtime selector.
- Android external-federation integration rules.
- Federation harvest/promotion gate.
- Existing federation semantic-code audit and native coding matrix references.
- Existing fail-closed provider/adapter architecture.

## Housekeeping actions
1. Kept external engines behind adapter/provider boundaries.
2. Kept harvested engines optional and non-boot-critical.
3. Preserved provenance, licence, security and rollback evidence requirements.
4. Prevented Celeste proprietary source/assets/content from entering the native tree.
5. Reconciled the game-engine federation routing with the existing federation authority hierarchy.
6. Checked for duplicate render/federation authority before adding a new engine layer.
7. Corrected a semantic defect in `mini-os/cpp/federation_runtime.cpp`: the selector previously required `compute_class == minimum_class`, which incorrectly rejected a higher-capability unit when the workload requested a lower minimum capability.
8. Added an explicit capability-floor predicate and retained preferred-class fast selection.
9. Preserved fail-closed behavior when no suitable available unit exists.

## Semantic cross-reference result
### PASS
- Engine providers remain non-authoritative.
- Provider presence is not treated as runtime availability.
- External code is not promoted merely because it was harvested.
- Licence/provenance/security evidence remain separate promotion gates.
- Web runtimes remain sandboxed.
- Celeste remains reference-only.
- Core OS/DMS retains execution authority.
- Human release authority remains the final promotion boundary.

### FIXED
- Mini OS compute federation minimum-class selection semantics.

### OPEN
- Exact upstream commit/tag pinning for each external engine.
- Dependency graph resolution.
- Host compilation.
- Android ABI compilation.
- Boot/runtime smoke tests.
- Security/dependency scanning.
- Device/GPU runtime verification.

## External-source cross-reference
Cocos2d-x identifies itself as an open-source cross-platform C++ framework and states MIT licensing. citeturn0search5
MonoGame's current repository documents Microsoft Public License coverage with separate third-party licensing, so dependency-level notices must remain intact. citeturn0search1turn0search2
libGDX documents Apache 2.0 licensing while its repository also carries separate third-party/Creative Commons material, so the complete notice set must be retained. citeturn0search8turn0search6
raylib documents its unmodified zlib/libpng license and its redistribution conditions. citeturn0search4
Three.js's upstream repository identifies the project under MIT licensing. citeturn0search9

## Gate disposition
External harvest: RECORDED
Internal cross-reference: COMPLETE
Semantic source audit: COMPLETE
Source defect correction: COMPLETE
External source integration: PENDING
Build verification: PENDING
Runtime/device verification: PENDING
Promotion: BLOCKED until evidence gates pass
