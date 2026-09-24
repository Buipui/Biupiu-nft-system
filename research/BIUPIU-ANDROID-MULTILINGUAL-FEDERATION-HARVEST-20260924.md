# Biupiu Android Multilingual Federation Harvest — 2026-09-24

## Scope
Deep external-language harvest for the Biupiu Mini OS / native Android coding framework, followed by repository cross-reference against the Native Coding Philosophy, Multilanguage Native Coding Matrix, Android build manifests and verification gates.

## External reference lanes

### German
Android's German-language internationalization documentation confirms Android uses ICU and CLDR for Unicode/internationalization and distinguishes platform/API-level behaviour. The same source documents ICU4C availability through the NDK boundary on supported Android versions.

### Japanese
The Japanese AOSP build documentation confirms Soong is the Android platform build authority and that Android.bp is its declarative module format. Feature/build flags are explicitly supported for isolating untested code from tested code.

### Simplified Chinese
The Chinese Android internationalization documentation independently confirms ICU/CLDR as the Unicode/i18n foundation and the expanded framework support from Android 7.0/API 24 onward.

### Korean
The Korean AOSP build documentation independently confirms the Soong + Kati + Ninja build chain and Android.bp as the platform build description.

## Coding-framework reconciliation

The external-language findings reinforce these Biupiu rules:

1. Language/localization metadata is part of the contract, not UI decoration.
2. BCP-47 locale identity must remain explicit at durable boundaries.
3. Unicode normalization, bidi-control and confusable-character checks remain mandatory before executable promotion.
4. Android platform build logic remains separate from application Gradle build logic.
5. Capability/API presence must not be interpreted as runtime/device capability.
6. Feature/build flags may isolate unverified code paths; unverified paths must remain visibly gated.
7. Native C/C++ Android code remains behind the NDK CMake boundary and must preserve ABI, ownership and fail-closed rules.
8. Foreign-language source material is reference evidence unless provenance, licence, compatibility, semantic and runtime gates promote it.
9. Translation is a linked derivative; original technical identifiers remain preserved.
10. No external executable code or proprietary binary is copied into the Biupiu repository solely from this harvest.

## Repository cross-reference

Canonical governance:
- `research/BIUPIU-NATIVE-CODING-PHILOSOPHY-AND-ENGINEERING-MATRIX-v1.0.md`
- `research/BIUPIU-MULTILANGUAGE-NATIVE-CODING-MATRIX-v1.0.md`
- `intelligence/BIUPIU-AI-CODING-HARD-GATE-v1.0.json`

Android authorities:
- `apps/android` — canonical native R&D OS Android shell
- `mini-os/android` — Mini OS Android federation build
- `.github/workflows/biupiu-mini-os-android.yml`
- `.github/workflows/biupiu-systemwide-module-audit.yml`

## Implementation update

The canonical `apps/android` shell now externalizes its application label through Android string resources and adds locale variants for:
- English
- German (`de`)
- Japanese (`ja`)
- Simplified Chinese (`zh-rCN`)
- Korean (`ko`)
- Russian (`ru`)

This is intentionally a small semantic change: it establishes a verified resource boundary without pretending the entire UI has been translated.

## Gate state

- Foreign-language external harvest: **REFERENCE PASS**
- Coding-framework reconciliation: **PASS**
- Provenance/licence boundary: **PASS**
- Android resource localization scaffold: **IMPLEMENTED**
- Static repository gate: **TRIGGERED BY COMMIT**
- Gradle/Android SDK build: **OPEN UNTIL FRESH CI RESULT**
- APK artifact verification: **OPEN UNTIL FRESH CI RESULT**
- Emulator/device runtime: **OPEN**
- OEM/physical hardware verification: **OPEN**

Promotion rule: implementation is not runtime verification. No Android build/device gate is marked verified without execution evidence.
