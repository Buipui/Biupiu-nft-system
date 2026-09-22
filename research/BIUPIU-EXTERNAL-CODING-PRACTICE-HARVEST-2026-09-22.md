# BIUPIU EXTERNAL CODING-PRACTICE FEDERATION HARVEST — 2026-09-22

## Trigger
Repository/changelog audit identified an authority hierarchy mismatch, permissive licence default in learning promotion, incorrect drift scoring semantics, and an incomplete Core OS validation requirement in federation F01.

## External findings
NIST SSDF: automated testing, static analysis, dynamic analysis, fuzzing, previous-bug regression tests, included-component verification and provenance.
Android Open Source Project: native memory-safety analysis, ASan/UBSan, fuzzing, CFI, least privilege/process isolation and Rust for new native platform work where practical.
CISA/FBI: memory-safe-language transition, compiler/runtime hardening, sanitizer testing, fuzzing/static/manual testing and root-cause recurrence prevention.

## Internal integration
External material was converted into Biupiu engineering rules rather than copied as executable code.

## Implemented fixes
- software/rnd-os-ai/src/biupiu_ai/authority_hierarchy.py
- software/rnd-os-ai/src/biupiu_ai/federation_protocol.py
- software/rnd-os-ai/src/biupiu_ai/learning.py
- software/rnd-os-ai/tests/test_authority_hierarchy.py
- software/rnd-os-ai/tests/test_federation_authority_gate.py
- software/rnd-os-ai/tests/test_learning_governance_semantics.py

## Evidence
SOURCE SEMANTIC REVIEW: COMPLETED
TARGETED REGRESSION TESTS: IMPLEMENTED
CODING-MATRIX CROSS-REFERENCE: COMPLETED
EXTERNAL PRACTICE HARVEST: COMPLETED
INTERNAL HARVEST: COMPLETED
HOST EXECUTION: UNAVAILABLE IN CURRENT TOOL ENVIRONMENT
CI EXECUTION: PENDING OBSERVED RUN
ANDROID DEVICE EXECUTION: PENDING
HARDWARE EXECUTION: PENDING

No runtime pass is claimed from source inspection alone.
