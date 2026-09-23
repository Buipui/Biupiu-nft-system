# BIUPIU MULTILANGUAGE NATIVE CODING MATRIX v1.0

Date: 2026-09-22
Status: HARD-CODED GOVERNANCE EXTENSION
Authority: subordinate to BIUPIU-NATIVE-CODING-PHILOSOPHY-AND-ENGINEERING-MATRIX-v1.0.md

## 1. Universal language-neutral rules

Every native implementation MUST preserve the same semantics regardless of programming language:
- explicit ownership and authority;
- typed/validated boundaries;
- deterministic state transitions where practical;
- explicit units, assumptions and uncertainty;
- structured errors; no silent failure;
- provenance and version identity;
- observable correlation/event IDs;
- tests at the smallest useful boundary;
- regression evidence before reuse;
- reversible changes and rollback references;
- licence/dependency/security checks for external material.

A language-specific idiom may differ. The contract meaning may not.

## 2. Language selection matrix

| Language | Preferred Biupiu role | Hard rules |
|---|---|---|
| Python | Intelligence, ML, research tooling, orchestration, data validation | type public APIs; explicit dataclasses/contracts; deterministic core where practical; pytest; no hidden global state; units/tolerances for numerical work |
| TypeScript | OS contracts, federation, web/runtime adapters | strict typing; explicit interfaces; runtime boundary validation; no implicit any in authoritative modules; tests for contracts; pinned dependencies |
| JavaScript | legacy/runtime glue and browser surfaces | minimize new authoritative JS; validate external input; isolate side effects; test browser/runtime paths |
| C | ABI/HAL/device interfaces | explicit lifetime/error semantics; bounded memory; no undefined behaviour; stable C ABI across language boundaries |
| C++ | high-performance simulation, geometry, graphics, scientific engines | RAII; explicit ownership; versioned serialization; avoid ABI leakage across durable boundaries; numerical tests |
| Rust | new memory/concurrency/security-sensitive native services | Result/error handling; safe-by-default; documented unsafe blocks; tests; C ABI where durable interoperability is required |
| Kotlin | Android/native mobile UI and services | lifecycle-safe components; structured concurrency; domain/data/UI separation; explicit state; unit tests |
| C# | Windows shell/desktop/native integrations | nullable/reference safety where enabled; explicit async/error paths; interface-driven services; tests |
| Solidity | EVM provenance/accounting/registry boundaries | minimal privilege; explicit access control; invariant/failure tests; pinned dependencies; deployment != compilation |
| YAML/JSON/Schema | contracts/configuration/manifests | schema version; validation; no executable semantics hidden in configuration; deterministic canonical representation |
| Shell/CI | build/test/release automation | fail-closed; quote variables; explicit exit codes; no secret leakage; reproducible versions |

## 3. Cross-language boundary

Durable interfaces MUST use language-neutral representations:
- versioned JSON/JSON Schema or equivalent canonical contract;
- explicit enums/states;
- stable IDs;
- ISO-8601 timestamps;
- hashes for content identity;
- BCP-47 locale tags for language identity;
- explicit units;
- provenance references;
- correlation/trace identifiers.

Do not pass language-specific object layouts across durable boundaries.

## 4. Semantic equivalence test

For a cross-language implementation, test the same fixture against each implementation:
INPUT -> NORMALISE -> VALIDATE -> EXECUTE -> OUTPUT -> ERROR/STATE

Expected equivalence means:
- same accepted/rejected inputs;
- same state transition;
- equivalent error class;
- same provenance identity;
- equivalent numerical result within declared tolerance.

Differences must be documented, not silently normalised.

## 5. Coding-style federation harvest

External language-specific guidance is harvested as REFERENCE/PATTERN only. NASA's current software-engineering material explicitly calls for coding standards and verification of adherence, including structure, error handling, module size, library use, types, naming and automated assessment. citeturn0search12turn0search10

OpenTelemetry's semantic-convention model is adopted as a pattern for consistent cross-language names and machine-readable meaning; its language implementations follow a common specification, while language-specific implementations remain implementation details. citeturn0search0turn0search7

Biupiu therefore uses:
SEMANTIC CONTRACT -> LANGUAGE ADAPTER -> LANGUAGE TEST -> CROSS-LANGUAGE FIXTURE -> FEDERATION REGRESSION.

## 6. Clean-up policy

Native cleanup is staged:
1. detect;
2. classify;
3. cross-reference older work;
4. preserve lineage;
5. repair smallest semantic defect;
6. run language-native tests;
7. run cross-language contract tests;
8. run regression;
9. update learning evidence;
10. only then remove redundant code.

No mass rewrite is performed solely to make style uniform.

## 7. AI coding hard rule

Before AI-generated or AI-assisted code is accepted into a native path, the AI coding gate MUST check:
REQUIREMENT -> OWNER -> LANGUAGE -> CONTRACT -> PROVENANCE -> SECURITY -> DEPENDENCIES -> SEMANTICS -> TEST -> REGRESSION -> ROLLBACK -> PROMOTION

If a required field/evidence item is missing, the code remains a PROPOSAL or QUARANTINED candidate.

## 8. Verification status

This matrix is a governance contract. It does not claim that every language/runtime has passed execution. Runtime, device, hardware, blockchain and physical verification remain separate gates.

## 8. Foreign-language artifact integrity

Foreign-language harvesting is a first-class research input, not an error condition. The repository must preserve:
- original source text/code;
- source language and BCP-47 locale where known;
- transliteration/translation only as a linked derivative;
- original technical identifiers where required by the source language;
- provenance and source location;
- semantic mapping into the Biupiu canonical vocabulary.

Automated checks must distinguish legitimate multilingual content from accidental misspellings or Unicode hazards. Executable identifiers receive stricter review than prose. Unicode normalization, bidi controls and confusable characters are checked before promotion.

Rule: never repair a foreign-language identifier by English spell-check inference. Cross-reference the source language and canonical contract first.

## 9. Repository-wide spelling/semantic gate

intelligence/BIUPIU-REPOSITORY-SPELLING-SEMANTIC-AUDIT.py checks high-confidence spelling errors, Unicode hazards, canonical registry references, native-code paths and multilingual metadata. Blocking findings prevent promotion; review findings require semantic inspection.
