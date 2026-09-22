# BIUPIU Federation Fault-Check / External-Fix Learning Changelog — 2026-09-22

## CHG-2026-09-22-FAULT-001

### Scope
Internal Federation fault check, missing-module detection, repeated internal/external harvest comparison, foreign-language harvest, semantic cross-check, learning update, guided-fault integration and housekeeping.

### Missing source-level capability found
1. External fixes discovered by Federation had no dedicated learning object that explicitly records found externally / absent internally / native implementation required.
2. Repeated harvest results had no deterministic comparison primitive for explaining result-set divergence.
3. Existing open runtime/bootstrap modules remain open and were not falsely closed.

### Native implementation
- software/rnd-os-ai/src/biupiu_ai/guided_fault_finding.py
  - ExternalFixGap
  - assess_external_fix_gap
  - guide_external_fix_gap
- software/rnd-os-ai/src/biupiu_ai/learning.py
  - ExternalFixEvidence
  - score_external_fix_gap
  - make_external_fix_gap_learning_record
  - HarvestComparison
  - compare_harvest_passes
- Targeted tests added in both guided-fault and learning test modules.

### New learning algorithm
EXTERNAL-FIX-GAP-LEARNING-v1
- Detect missing internal implementation.
- Preserve external provenance.
- Compare semantic compatibility.
- Check licence/security evidence.
- Score information gain, uncertainty reduction, model disagreement, feasibility and regression safety.
- Feed unresolved gaps back into guided fault finding.
- Generate a native implementation candidate where safe.
- Never auto-promote external executable code.
- Require OS validation, regression and existing promotion gates.

### Double-search logging
Internal pass 1/pass 2: same four GitHub queries; stable top-path families observed.
External pass 1/pass 2: same multilingual fault/FMEA learning queries; different ranked result surfaces observed.
The system now records common/unique sets and requests recency/source-index review rather than guessing the reason for divergence.

### Foreign-language learning
Japanese: historical incident/design data can be used to retrieve related failure scenarios and support learning algorithms. German: structured FMEA emphasises system functions, interfaces, failure effects and corrective-action tracking. Chinese: FMEA/FMECA material emphasizes systematic failure-mode, cause and effect analysis and maintenance of failure knowledge. citeturn2search2turn2search46turn1search0

### Semantic code cross-check
OpenTelemetry semantic conventions reinforce stable cross-language naming and correlation; NASA SFMEA and IEC 60812 reinforce systematic failure-mode, dependency, interface, assumption and mitigation analysis. citeturn0search0turn0search2turn0search5turn2search13

### Exterminate / housekeeping
- No external executable code copied into native core.
- Unverified external candidates remain reference/quarantine state.
- Existing open runtime/device/HIL gates retained.
- Duplicate knowledge is linked rather than silently deleted.
- New learning evidence is cross-linked to guided fault finding and Federation harvest records.

Status: SOURCE IMPLEMENTED / TARGETED TESTS ADDED / RUNTIME & CI OPEN / PROMOTION FAIL-CLOSED.
