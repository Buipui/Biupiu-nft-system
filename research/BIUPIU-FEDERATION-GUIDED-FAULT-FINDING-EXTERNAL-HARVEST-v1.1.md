# BIUPIU FEDERATION GUIDED FAULT-FINDING EXTERNAL HARVEST v1.1 — 22 September 2026

Status: HARVESTED / NORMALISED / REFERENCE-ONLY / EXECUTABLE PROMOTION BLOCKED

## Purpose
Federation searched internal repository evidence first, then external multilingual sources for more efficient guided fault finding, bug-fix matrices, diagnostic workflows and verification patterns.

## Internal-first harvest
Existing native assets were reused before introducing new concepts:
- `software/rnd-os-ai/src/biupiu_ai/guided_fault_finding.py`
- `software/rnd-os-ai/src/biupiu_ai/learning.py`
- federation protocol/registry and harvest promotion gates
- learning federation bridge
- system cross-link and fault/healing records
- render health/failure-learning paths

The native guided path remains:
OBSERVE -> CLASSIFY -> OWNERSHIP -> EVIDENCE -> ISOLATE -> REPAIR PROPOSAL -> INDEPENDENT VALIDATION -> REGRESSION -> LEARNING -> CONTROLLED REUSE.

## External federation harvest

| Source/pattern | Language/region lane | Harvested principle | Biupiu treatment |
|---|---|---|---|
| NASA Software Assurance / IV&V | English / US | objective evidence, independent verification, traceable/testable requirements, nominal + off-nominal testing, security and OSS review | REFERENCE/PATTERN |
| IEC 60812 / JSA FMEA material | Japanese / international | structured failure-mode/effect analysis, documented failure treatment and maintenance | REFERENCE/PATTERN |
| Unicode CLDR / UTS #35 / BCP 47 | international | canonical locale identity, machine-readable validation, deterministic language matching/fallback | REFERENCE/PATTERN |
| WF Diagnostics | English / open-source | bounded diagnostic tasks, closed command allowlist, timeouts, read-only AI analysis and separate remediation authority | REFERENCE/PATTERN |
| Self-healing-agent / similar research repos | English / open-source | failure signal -> triage -> known-fix lookup -> verify -> log/learn | REFERENCE/PATTERN |
| E2E-Self-Heal | Korean/Japanese/Chinese documentation surface | diagnose -> constrained patch -> live verification -> retry cap -> human-reviewable boundary | REFERENCE/PATTERN |
| REPAIR.ai / self-healing agent patterns | English | deterministic fast path plus hypothesis/repair path, adversarial failure injection and explicit verification | REFERENCE/PATTERN |

External material is not treated as Biupiu authority and no external executable code was promoted.

## New native implementation
Added a deterministic `FaultFixRule` matrix to the native guided fault-finding module. Each supported class now maps to:
1. diagnostic evidence action;
2. bounded repair action;
3. independent validation action;
4. mandatory regression;
5. human-controlled promotion.

Unknown fault classes fail closed. Security faults remain quarantined and cannot be auto-repaired.

## Verification
Source semantics: IMPLEMENTED.
Regression test source: IMPLEMENTED.
Repository CI/build/security/runtime/HIL: OPEN until independently observed.
External code promotion: BLOCKED.

## Sources
- NASA Software Assurance / IV&V requirements describe objective evidence, traceable/testable requirements, source-code assurance and testing of nominal/off-nominal conditions. 
- Japan Standards Association material describes FMEA as identifying failure modes/effects and documenting required treatments; IEC 60812:2018 is identified as active in the JSA listing.
- Unicode CLDR provides locale data, BCP 47 validation data and deterministic language matching/fallback patterns.
- Public GitHub diagnostic/self-healing projects were used only as architecture-pattern references.

## Governance
TRACEABILITY + PROVENANCE + TESTING + SECURITY + REPRODUCIBILITY + REGRESSION + OBSERVABILITY + HUMAN RELEASE CONTROL remain mandatory.
