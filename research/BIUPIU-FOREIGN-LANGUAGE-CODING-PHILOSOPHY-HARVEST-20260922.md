# Biupiu Foreign-Language Coding & Multilingual Engineering Federation Harvest — 2026-09-22

Status: HARVESTED / CROSS-REFERENCED / NATIVE PATTERNS IMPLEMENTED WHERE SAFE / RUNTIME PROMOTION PENDING

## External evidence harvested

| Source lane | Observed principle | Biupiu use |
|---|---|---|
| Unicode CLDR / UTS #35 | Locale identity must distinguish language, script and region; software internationalisation depends on locale data and algorithms. | Adopt BCP-47-compatible locale identity and preserve script/region in the native language router. |
| Unicode CLDR support levels | Language support is incremental: display, input, selection, i18n, UI and advanced language services are distinct capabilities. | Add explicit support-level metadata; do not claim full language support from a selector alone. |
| FLORES-200 / NLLB evaluation | Multilingual systems require controlled, comparable evaluation sets; low-resource languages need additional verification care. | Add multilingual test-lane requirement and retain original-language evidence. |
| i18next fallback patterns | Variant/script/region fallback should be deterministic and can proceed from specific locale to broader language then configured default. | Native fallback chain: exact tag -> language family -> declared default. |
| Kotlin/Android multilingual examples | In-app language selection and Android locale resources can be tested independently of device locale. | Native OS selector added without introducing a translation-provider dependency. |
| Chinese-language Android localisation projects | Runtime language switching is a concrete implementation concern, not just translation-file management. | Treat locale selection as an OS capability and test contract. |
| German/Kotlin i18n research | Locale data, message keys and runtime formatting are separate concerns. | Keep locale identity separate from translation content and evidence metadata. |
| Japanese/Chinese/Korean OEM research lane | Script correctness and OEM/platform behaviour can diverge; source language is not a trust signal. | Preserve original-language source metadata and require executable validation before promotion. |

## Native implementation decisions

1. The shared language contract is authoritative for locale identity.
2. Android and Windows UI surfaces consume the contract rather than defining independent language registries.
3. Python Intelligence translation now preserves BCP-47-compatible script and region subtags.
4. Fallback is deterministic and observable.
5. Translation output remains translated-unverified until independently verified.
6. Foreign-language source material remains reference evidence; language never grants authority.
7. No third-party translation library or provider was copied into the executable core.
8. External implementations remain candidates/reference patterns unless licence, dependency, security, build, test and regression gates pass.

## Test vectors

- pt_BR -> pt-BR
- zh_Hant_TW -> zh-Hant-TW
- pt-BR fallback -> pt-BR -> pt -> en
- unknown xx -> rejected by Biupiu support registry
- translation without provider -> pending, not fabricated
- translated output with provider -> translated-unverified

## Promotion state

Source-level semantic checks: PASS.
Native unit-test additions: IMPLEMENTED.
CI execution: PENDING OBSERVED RESULT.
Android device/UI runtime: PENDING.
Windows runtime: PENDING.
Foreign harvested executable code promotion: NONE.

## Learning rule

Foreign-language harvesting is a retrieval and comparison mechanism. The learning layer records source language, source terminology, implementation pattern, provenance, licence state, test evidence, failure class and resulting Biupiu decision. It does not learn authority from language, popularity or translation confidence alone.
