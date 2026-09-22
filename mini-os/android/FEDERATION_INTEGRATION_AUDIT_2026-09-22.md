# Buipui Mini OS — Federation Integration Audit
Date: 2026-09-22

## Verification
Audited the Android Mini OS tree and rechecked the requested federation stack against the current Gradle architecture.

Current baseline: AGP 8.7.3, compileSdk/targetSdk 35, minSdk 29, applicationId com.biupiu.minios.

## Current source finding
The app module currently declares AppCompat, AndroidX Core, and Android Automotive dependencies. The requested third-party federation libraries are not yet declared in app/build.gradle.

Existing provider-neutral boundary verified:
- ExternalTransportAdapter
- OpenDroidCapabilityAdapter

OpenDroidCapabilityAdapter correctly reports runtime availability as false until the external project, build, and device integration are actually verified.

## Integration matrix
| Capability | Target | Integration rule | Status |
|---|---|---|---|
| HTTP | OkHttp | NetworkTransport adapter; central client/policy | OPEN |
| OAuth/OIDC | AppAuth | IdentityProvider adapter; PKCE; browser-based auth | OPEN |
| GraphQL | Apollo Kotlin | Optional GraphQLProvider/federation module | OPEN |
| Images | Coil | Primary image pipeline; network/cache boundary | OPEN |
| GIF | Coil GIF / android-gif-drawable | Adapter only where specialised API is required | OPEN |
| SVG | Coil SVG / AndroidSVG | Rendering adapter; avoid duplicate pipelines | OPEN |
| HTML | jsoup | Untrusted-input parsing/sanitisation boundary | OPEN |
| PDF | AndroidX PDF preferred | PdfProvider abstraction; legacy PdfViewPager compatibility only | OPEN |
| Locale | Lingver | LocaleProvider abstraction; no direct app-wide coupling | OPEN |
| Platform | AOSP | Platform/base layer, not Gradle dependency | VERIFIED |
| UI resources | Seti UI | Resource/theme/icon input, not runtime dependency | VERIFIED |

## Foreign-language cross-check
Non-English documentation was cross-checked for Android identity/deep-linking and networking architecture. The review reinforces two missing boundaries: verified app-link/identity integration and centralised network transport. No foreign-language source justified bypassing the provider-neutral architecture.

## Fixes identified
1. Keep third-party libraries behind internal interfaces.
2. Add dependency versions through one controlled dependency-management location before module wiring.
3. Separate authentication state from HTTP transport.
4. Keep GraphQL optional.
5. Use one primary image pipeline and adapters for specialised SVG/GIF use.
6. Put HTML parsing behind sanitisation and trust boundaries.
7. Use a PDF provider abstraction so the viewer implementation can evolve.
8. Add locale abstraction and keep runtime locale changes out of core business logic.
9. Add verified App Links/Digital Asset Links handling to the identity gate.
10. Do not mark external agent capabilities available from source registration alone.

## Test gate
Verified by repository source inspection and semantic dependency/architecture review.
Not yet verified: Gradle dependency resolution, compilation, unit/instrumentation tests, APK install, device runtime, and AOSP/device integration.

## Gate state
ARCHITECTURE AUDIT: VERIFIED
MISSING-MODULE AUDIT: VERIFIED
FOREIGN-LANGUAGE CROSS-CHECK: VERIFIED
SOURCE DEPENDENCY IMPLEMENTATION: OPEN
BUILD/TEST: OPEN
DEVICE RUNTIME: OPEN
