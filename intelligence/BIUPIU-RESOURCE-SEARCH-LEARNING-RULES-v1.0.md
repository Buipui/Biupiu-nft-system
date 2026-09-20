# BIUPIU Resource Search Learning Rules v1.0

Date: 20 September 2026
Status: IMPLEMENTED — Intelligence learning policy

## Objective

Teach Biupiu Intelligence how to solve resource failures by learning from search provenance + failure evidence + licence constraints + capability fit + substitute outcomes, rather than simply accumulating links.

## Learning tuple

<problem, language_set, source_classes, candidate_set, rejection_reasons, licence_state, security_state, substitute, twin_fit, test_result, outcome>

## Retrieval policy

1. Search native terminology before English translation.
2. Search primary owners/R&D companies and universities before community mirrors.
3. Search standards and official developer portals before implementation forks.
4. Search for the interface contract when a specific repository is unavailable.
5. Re-use a substitute only when the failure mode and interface fit are recorded.

## Learning dimensions

- provenance confidence
- licence clarity
- security evidence
- maturity/test evidence
- interface compatibility
- cross-disciplinary reuse
- toolchain compatibility
- digital-twin fit

These dimensions may control retrieval ordering only. They do not become production authority.

## Negative learning

Record failed URL/repository, unavailable runtime, build failure, incompatible ABI/API, incompatible licence, security concerns, missing assets, stale/abandoned source and translation ambiguity.

A negative result is reusable evidence when it is reproducible or clearly documented.

## Positive learning

Record exact source/version/commit, exact language/query terms, licence, adapter path, test vector, simulator/twin fit, department routes and verification result.

## Cross-disciplinary generalisation

CAPABILITY -> NEIGHBOURING DEPARTMENTS -> NATIVE TERMS -> CANDIDATE SOURCES -> TWIN FIT

Examples:
- CFD -> automotive + marine + aerospace + energy + process + agriculture
- 3D geometry -> CAD + robotics + World + geospatial + inspection
- digital-twin state -> farming + factories + energy + vehicles + medical devices

## Promotion guard

Learning may change what is searched next and which substitute is proposed. It may not silently change OS authority, security policy, physical actuation permissions or third-party licence obligations.