# BIUPIU OPEN DROID DEEP EXTERNAL FEDERATION HARVEST — 2026-09-22

Status: **SOURCE HARVEST COMPLETE / NATIVE ADAPTER IMPLEMENTED / BUILD + DEVICE RUNTIME OPEN**

## 1. Identity correction

The previously registered identifier `opendroid.ui-engine` is not sufficiently supported as the identity of a standalone UI engine.

Current external evidence identifies **OpenDroid** as an open-source autonomous Android AI agent. Its documented architecture contains accessibility automation, action executors, agent/plan/intent/vision logic, LLM provider routing, memory, security, Android services/notifications/voice, Room/DataStore repositories, Hilt dependency injection, and a Compose-based UI layer. The repository is Apache License 2.0.

Therefore Biupiu records two distinct concepts:

- `opendroid.ui-engine`: **UNRESOLVED / BLOCKED** — retained for backward-compatible identity tracking; no standalone engine authority is inferred.
- `opendroid.android-agent` and its module capabilities: **ADAPTER_ONLY** — reference/provider boundaries requiring independent integration, licence, build, security, regression and device verification.
- `opendroid.compose-ui`: **ADAPTER_ONLY** — UI surface reference, not a replacement for the Biupiu UI/OS authority.

## 2. External evidence

Primary external source:
- OpenDroid repository: https://github.com/yashab-cyber/opendroid
- OpenDroid README architecture and licence: Apache-2.0; Clean Architecture; Dagger-Hilt; accessibility/actions/core/LLM/memory/security/service/voice/data/Room/DataStore/DI/UI/Compose.
- OpenDroid roadmap/release evidence: v1.0.7, minSdk 26, target/compile SDK 36, Gradle 9.7, AGP 9.3.1, Kotlin 2.4.0, JDK 21, Room schema v9, JVM + androidTest coverage and CI.
- OpenDroid release notes identify hardware-backed Android Keystore AES-256-GCM credential storage, Room migrations, LiteRT compatibility work, and failure-marker/fallback corrections.

Biupiu treatment: **reference and adapter evidence only**. No external source code, APK, signing key, model weights, API credential or proprietary component is copied into the Biupiu tree.

## 3. Module harvest

| External module | Biupiu role | Main OS | Mini OS | State |
|---|---|---|---|---|
| Accessibility automation | UI automation/screen interaction boundary | provider | adapter | ADAPTER_ONLY |
| Action dispatcher/executors | structured action boundary | provider | adapter | ADAPTER_ONLY |
| AgentLoop / PlanManager | planning boundary | provider | adapter | ADAPTER_ONLY |
| IntentClassifier / VisionEngine | perception/classification boundary | provider | adapter | ADAPTER_ONLY |
| LLM provider layer | model/provider routing | provider | adapter | ADAPTER_ONLY |
| Memory / knowledge graph | agent-state reference | provider | adapter | ADAPTER_ONLY |
| Android Keystore security | credential-security pattern | security reference | adapter | ADAPTER_ONLY |
| Foreground service | Android lifecycle boundary | platform adapter | adapter | ADAPTER_ONLY |
| Notification listener | notification intelligence boundary | platform adapter | adapter | ADAPTER_ONLY |
| Wake word / speech / TTS | voice boundary | provider | adapter | ADAPTER_ONLY |
| Room DB | local persistence boundary | data adapter | adapter | ADAPTER_ONLY |
| DataStore repositories | preferences/state boundary | data adapter | adapter | ADAPTER_ONLY |
| Hilt DI | dependency wiring pattern | architecture reference | adapter | ADAPTER_ONLY |
| Compose UI | UI surface | UI adapter | UI adapter | ADAPTER_ONLY |
| ViewModels | presentation state boundary | UI adapter | UI adapter | ADAPTER_ONLY |
| Theme/components/screens | presentation surface | UI adapter | UI adapter | ADAPTER_ONLY |

## 4. Internal harvest / duplicate check

Existing Biupiu architecture already provides:
- Android capability registry and fail-closed states.
- Native coding philosophy and engineering matrix.
- Federation protocol and provider-adapter boundary.
- Main OS Python federation registry.
- Mini OS Android federation registry.
- Native semantic-code audit.
- Guided fault-finding and evidence/provenance contracts.
- Existing graphics/Vulkan adapter authority.
- Existing Android AICore/AppFunctions federation.
- Existing LLM-family and ExecuTorch/PyTorch provider boundaries.

No second UI authority was created. OpenDroid is therefore integrated as an external provider family and Compose UI surface reference, while Biupiu OS/DMS remains authoritative.

## 5. Semantic and conflict checks

### Corrected conflict
The prior `opendroid.ui-engine` entry could be read as an actual standalone engine despite insufficient identity evidence. It remains unresolved and blocked, while the supported OpenDroid agent/module identities are registered separately.

### Fail-closed rules
- Provider registration does not imply runtime availability.
- Compose UI is not treated as OS authority.
- Accessibility automation requires explicit Android permission/service/runtime evidence.
- Keystore capability requires actual Android Keystore/device validation.
- Room/DataStore require Android build/runtime verification.
- LLM provider credentials remain outside source control.
- External APKs and binaries are not imported as trusted runtime dependencies.
- OpenDroid runtime is not marked verified until an independently reproducible integration build and device test exists.

## 6. External bug/fix literature harvested

The external OpenDroid record documents several engineering patterns relevant to Biupiu:
- dedicated configuration fields and URL normalization for provider endpoints;
- race-condition correction in Settings state persistence;
- hardware-backed credential storage with AES-256-GCM;
- sequential Room migrations and migration tests;
- provider-specific failure-marker matching and fallback handling;
- explicit CI lanes for unit tests, lint, assembleDebug, connected Android tests and release packaging.

Biupiu adopts these only as **patterns to validate**, not as claims that the external implementation is bug-free or as copied code.

## 7. Coding philosophy / matrix application

Applied rules:
1. External identity must be evidence-backed.
2. Architecture claims are separated from executable authority.
3. Adapter boundaries isolate third-party implementations.
4. Security-sensitive state is fail-closed.
5. Provenance/licence/build/device verification remain separate gates.
6. Existing Biupiu contracts are reused instead of duplicating authorities.
7. UI is presentation, not system authority.
8. Runtime-dependent claims remain open until executed.

## 8. Native implementation

Added:
- `mini-os/android/federation/OpenDroidCapabilityAdapter.java`
- OpenDroid module registry in `AndroidCapabilityRegistry.java`
- OpenDroid module/fail-closed tests in `AndroidCapabilityRegistryTest.java`
- Main OS provider entries in `software/rnd-os-ai/src/biupiu_ai/federation_registry.py`

The adapter exposes a deterministic module set and deliberately returns unavailable until external build/device evidence exists.

## 9. Verification boundary

**IMPLEMENTED**
- Identity correction.
- External literature record.
- Internal gap reconciliation.
- Main OS provider registration.
- Mini OS capability registration.
- Native adapter boundary.
- Semantic fail-closed tests.
- Index/cross-reference target identified.

**SOURCE-LEVEL VERIFIED BY INSPECTION**
- No standalone OpenDroid UI-engine authority is inferred.
- Adapter returns false until runtime proof.
- Unresolved legacy identifier remains blocked.
- Module set is explicit and deterministic.

**OPEN**
- Android/Gradle build of Biupiu Mini OS.
- OpenDroid dependency integration build.
- AccessibilityService/device permission test.
- Compose rendering/runtime test.
- Room/DataStore migration/runtime test.
- Keystore hardware-backed verification.
- LLM provider integration/regression.
- Live Android device regression.
- Full repository semantic audit execution and CI result.

## 10. Promotion path

`EXTERNAL EVIDENCE -> IDENTITY CLASSIFICATION -> LICENCE/PROVENANCE -> MODULE CONTRACT -> ADAPTER -> SEMANTIC TEST -> BUILD -> DEVICE TEST -> REGRESSION -> CORE OS/DMS VALIDATION -> HUMAN PROMOTION`

No OpenDroid module is promoted directly into authoritative Biupiu OS execution from literature alone.
