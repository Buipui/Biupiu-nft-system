# Biupiu Cross-Platform Architecture — Gate 20

## Objective
Keep Biupiu business rules, capability contracts, entitlement logic, diagnostics, and data schemas shared while isolating platform-specific UI, security, storage, rendering, device, and distribution adapters.

## Target layers
1. **Biupiu Core** — domain models, capability registry, entitlement rules, diagnostics, serialization.
2. **Shared services** — API contracts, offline/cache contracts, synchronization, localization, telemetry schema.
3. **Platform adapters** — Android, Windows, macOS, Linux, Unix/POSIX, iOS, Web.
4. **Department packages** — farming, metallurgy, digital twin, research and later modules.
5. **Distribution shells** — Google Play and OEM Android stores, Microsoft distribution, Apple distribution, Linux packages, direct enterprise deployment.

## Platform strategy
Kotlin Multiplatform is the preferred shared-code path where it reduces duplication. Compose Multiplatform is the preferred shared UI path for Android/desktop/iOS where appropriate. Platform-specific APIs remain behind explicit adapters.

Official Android documentation currently identifies KMP as production-ready for shared business logic and lists Android, JVM and iOS as Tier 1, macOS/Linux as Tier 2, and Windows as Tier 3 for the relevant Jetpack multiplatform support. Compose Multiplatform currently supports Android, iOS, macOS, Windows, Linux and Web, subject to its own compatibility matrix.

## OEM stores
Store publication is treated as a distribution layer, not a separate application architecture. The Android artifact must remain a standards-compliant AAB/APK with configurable package metadata, signing, permissions, privacy declarations and store-specific listing assets.

## Unix
“Unix compatibility” is not treated as one binary target. POSIX/Unix variants require an adapter and CI/build profile per supported operating system. Unsupported APIs must fail at compile-time or through explicit capability detection rather than silent assumptions.

## Missing modules identified at Gate 20
- shared KMP core module
- common serialization/data contracts
- platform secure-storage adapters
- platform filesystem/cache adapters
- cross-platform networking/API client
- navigation/UI shell abstraction
- device capability abstraction
- rendering/Digital Twin adapter contract
- automated matrix CI for target platforms
- signing/package manifests per distribution channel
- OEM-specific Android compatibility tests
- release/upgrade/migration framework
- accessibility/localization test matrix

## Gate rule
Do not claim a platform is production-ready merely because its target compiles. Each target requires build, launch, capability, persistence, security, and regression verification.
