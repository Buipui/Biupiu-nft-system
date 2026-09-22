# Buipui Mini OS — Federation Integration / Housekeeping Audit
Date: 2026-09-22

## Gate objective
Integrate the requested federation stack into the existing Mini OS architecture without leaking provider-specific types into core contracts; remove duplicate source registrations; harden network/identity/locale boundaries; add executable regression coverage; and leave runtime-only gates explicitly open until evidence exists.

## Verified baseline
- AGP 8.7.3
- Gradle 8.9 CI gate
- compileSdk 35 / targetSdk 35 / minSdk 29
- applicationId `com.biupiu.minios`
- Java 17 compile target
- AndroidX AppCompat/Core/Car App retained
- repository source tree is `mini-os/android/`

## Implemented integration

| Capability | Provider | Integration | Status |
|---|---|---|---|
| HTTP | OkHttp 5.1.0 | `NetworkTransport` + `OkHttpNetworkTransport` | IMPLEMENTED |
| OAuth/OIDC | AppAuth 0.11.1 | `AppAuthIdentityProvider` + redirect receiver boundary | IMPLEMENTED / CONFIG OPEN |
| GraphQL | Apollo Kotlin runtime 5.1.0 | `ApolloGraphQLProvider` capability boundary; schemas remain optional | IMPLEMENTED / SCHEMA OPEN |
| Images | Coil 3.4.0 | Primary image dependency + network/OkHttp integration | IMPLEMENTED |
| GIF | Coil GIF 3.4.0 | Primary animated-image path | IMPLEMENTED |
| GIF specialised | android-gif-drawable 1.2.32 | Specialised adapter dependency; not a second app-wide pipeline | IMPLEMENTED |
| SVG | Coil SVG 3.4.0 | Primary SVG path | IMPLEMENTED |
| SVG specialised | AndroidSVG 1.4 | Specialised direct-render adapter | IMPLEMENTED |
| HTML/XML | jsoup 1.23.2 | Parse + sanitise boundary | IMPLEMENTED |
| PDF | AndroidX PDF 1.0.0-beta01 | Forward-facing PDF provider | IMPLEMENTED |
| PDF legacy | PdfViewPager | No longer selected as core dependency; compatibility adapter only if legacy input requires it | DEFERRED |
| Locale | AndroidX per-app locales | `LocaleProvider`; Lingver isolated as compile-only compatibility option | IMPLEMENTED |
| Lingver | 1.3.0 | Legacy compatibility boundary only | COMPATIBILITY |
| Platform | AOSP | Platform/base layer | VERIFIED |
| UI resources | Seti UI | Resource/theme/icon source, not runtime dependency | VERIFIED |
| OpenDroid | External agent | Provider-neutral source boundary | OPEN until external build/device proof |

## Missing modules found and fixed

1. **Federation sources were outside the Gradle source set.**
   - Fixed by moving the active federation boundaries into `app/src/main/java/com/biupiu/minios/federation/`.
   - Removed duplicate non-build copies under `mini-os/android/federation/`.

2. **Internet permission was missing.**
   - Fixed with `android.permission.INTERNET`.

3. **No centralized dependency version policy.**
   - Fixed in `mini-os/android/build.gradle` using `biupuiVersions`.

4. **No deterministic Java target.**
   - Fixed to Java 17 to match the existing CI direction.

5. **Locale auto-generation resource was initially misplaced during integration.**
   - Corrected to `app/src/main/res/resources.properties`.
   - `generateLocaleConfig true` is now enabled.

6. **Authentication and transport were previously only conceptual.**
   - Fixed by separating `NetworkTransport` from `AppAuthIdentityProvider`.
   - AppAuth callback is isolated behind its redirect receiver.

7. **HTML federation had no trust boundary.**
   - Fixed with jsoup parse/sanitize provider.

8. **No regression test existed for untrusted HTML.**
   - Added `HtmlFederationProviderTest`.

9. **No executable Android build gate existed for this Mini OS path.**
   - Added `.github/workflows/biupiu-mini-os-android.yml` with JDK 17, Android SDK 35, Gradle 8.9, unit tests, assembleDebug, and source sanity checks.

10. **Verified App Links cannot be honestly enabled yet.**
    - No authoritative Biupiu production domain or signing-certificate SHA-256 fingerprint is registered in this Mini OS tree.
    - Custom AppAuth redirect is therefore implemented now; HTTPS App Links/Digital Asset Links remain CONFIG OPEN.
    - Do not invent a domain or fingerprint.

## Architecture rules enforced

```text
Buipui Mini OS
├── AOSP / Android Platform
├── Core
├── Network Boundary
│   └── NetworkTransport -> OkHttp
├── Identity Boundary
│   └── AppAuth / OAuth2-OIDC / PKCE
├── Federation Boundary
│   ├── Apollo GraphQL
│   └── jsoup HTML/XML
├── Media Boundary
│   ├── Coil
│   ├── Coil GIF
│   ├── Coil SVG
│   └── specialised GIF/SVG adapters
├── Document Boundary
│   └── AndroidX PDF
├── Localization Boundary
│   └── AndroidX locale API (+ isolated Lingver compatibility)
└── UI / Resource Layer
    └── Seti-derived resources
```

Provider libraries must not become system-of-record contracts. Core code consumes internal interfaces/capabilities.

## Foreign-language federation harvest

### Japanese
Android's Japanese App Links documentation confirms `autoVerify`, website host association, `assetlinks.json`, and signing-certificate fingerprint verification. This reinforces the identity gate and the requirement for a real production domain before enabling verified links.

### Korean
Korean Android documentation confirms separate App Links filters per unique scheme/host combination and verification through `assetlinks.json`. It also confirms Android's per-app language architecture.

### Chinese
Chinese Android documentation confirms automatic per-app locale generation from app/library resources and the AGP `generateLocaleConfig` route. This supports the move away from making Lingver the authoritative locale layer.

### Additional current upstream checks
- Coil 3.x separates network support into `coil-network-okhttp` and provides dedicated GIF/SVG extensions.
- AndroidX PDF now has a 1.0.0-beta01 viewer artifact.
- jsoup 1.23.2 is the current 2026 release reviewed for this gate.
- Apollo Kotlin 5.1.0 runtime is compatible with the modern Android/Gradle stack.
- AppAuth 0.11.1 is available from Maven Central; its upstream documentation supports OAuth2/OIDC, Custom Tabs and PKCE.

## Conflict / bug disposition

- **Duplicate federation source tree:** EXTERMINATED.
- **Direct provider coupling:** prevented by internal capability boundaries.
- **Network/auth conflation:** separated.
- **Image stack duplication:** Coil is primary; specialised libraries are not selected as competing global loaders.
- **Locale stack conflict:** AndroidX is authoritative; Lingver is compatibility-only.
- **Unverified production App Links:** deliberately not fabricated; remains configuration gate.
- **OpenDroid runtime claim:** remains false until external project/build/device proof.
- **PdfViewPager:** deliberately not promoted into the core dependency graph; use AndroidX PDF forward path.

## Verification state

### VERIFIED by repository inspection
- architecture placement
- dependency declarations
- source-set placement
- manifest network permission
- AppAuth redirect boundary
- Java 17 configuration
- locale resource placement
- regression-test source
- CI workflow source
- duplicate-source cleanup

### EXECUTABLE / PENDING CI RESULT
- Gradle dependency resolution
- unit tests
- debug APK compilation
- Android lint/build diagnostics

### OPEN — requires real external/runtime evidence
- device installation and boot
- AppAuth live authorization against a real identity provider
- HTTPS App Links / Digital Asset Links against the authoritative domain and signing fingerprint
- Apollo generated schema/query integration
- OpenDroid external project/build/device integration
- physical AOSP/device integration

## Gate status

**ARCHITECTURE INTEGRATION: IMPLEMENTED**

**MISSING-MODULE / BUG-FIX AUDIT: IMPLEMENTED**

**HOUSEKEEPING / DUPLICATE SOURCE EXTERMINATION: COMPLETE**

**FOREIGN-LANGUAGE HARVEST: COMPLETE**

**CI BUILD/TEST GATE: CREATED — RESULT PENDING**

**DEVICE RUNTIME: OPEN**

**PRODUCTION IDENTITY / APP LINKS: OPEN**

This record intentionally does not mark CI, device, or production identity gates as verified before their evidence exists.
