# Biupiu Coding Matrix Changelog — 2026-09-22

## CHG-2026-09-22-MLANG-001

Scope: native multilingual OS, Intelligence translation, federation harvest, coding philosophy.

### Added
- BCP-47-compatible locale contract with language/script/region preservation.
- Shared support-level vocabulary aligned to CLDR-style capability levels.
- Deterministic locale fallback chain.
- Native Android language selector.
- Native Windows language selector/registry.
- Smart Farming cross-link to the shared language contract.
- Intelligence translation tests for script/region preservation and fallback.
- Foreign-language coding-philosophy federation harvest record.

### Corrected
- Native Python language normalisation previously discarded script/region information.
- Locale identity is now preserved through the Intelligence translation boundary.

### External knowledge incorporated
- Unicode CLDR locale identity, fallback and support-level principles.
- FLORES/NLLB controlled multilingual evaluation principles.
- i18next variant/script/region fallback patterns.
- Multilingual Kotlin/Android runtime-selection patterns.
- Foreign-language OEM/localisation research as reference-only evidence.

### Native authority rule
External resources remain reference/candidate inputs. No external executable implementation was promoted merely because it was foreign-language, popular, translated or documented.

### Verification
- Semantic source review: PASS.
- Native test additions: IMPLEMENTED.
- CI run: OPEN pending observed workflow result.
- Android runtime/device: OPEN.
- Windows runtime: OPEN.
- Full translation quality: OPEN pending controlled benchmark and linguistic validation.

### Learning
Recorded as a governed learning event candidate. Reusable learning includes:
- locale metadata preservation,
- deterministic fallback testing,
- support-level classification,
- multilingual regression vectors,
- foreign-language source/provenance retention.

### Blockchain
Anchor-ready metadata may include:
release/change ID, affected paths, source commits, harvest record hash, test manifest hash and learning-event ID.
No private data, credentials, raw model output or source code is placed on-chain.
