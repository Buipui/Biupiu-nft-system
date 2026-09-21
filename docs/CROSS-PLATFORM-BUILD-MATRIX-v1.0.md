# Biupiu R&D OS — Cross-Platform Build Matrix v1.1

| Platform | CPU families | Dev | CI | Package | Release gate |
|---|---|---:|---:|---|---|
| Windows | x86-64 AMD/Intel | READY | REQUIRED | MSIX/installer or Tauri bundle | build + smoke |
| macOS | arm64 Apple / x86-64 Intel | READY | REQUIRED | App bundle/DMG | build + signing + notarization |
| Linux | x86-64 AMD/Intel, arm64 | READY | REQUIRED | AppImage/deb/rpm/Flatpak as appropriate | build + smoke |
| Android | arm64 / supported x86_64 | EXISTING | REQUIRED | APK/AAB | Android build + smoke |
| iOS/iPadOS | arm64 Apple Silicon | ARCHITECTURE ADDED | REQUIRED | Xcode archive/IPA | build + device smoke |
| Web/PWA | browser/host independent | EXISTING | REQUIRED | static/PWA | browser smoke |

## Native acceleration layer
- AMD: Zen/AVX capability dispatch through the common C ABI.
- Intel: AVX/AVX10/AMX capability dispatch through the common C ABI.
- Apple: arm64 + Accelerate/Metal adapters.
- Generic fallback: portable C/C++.

## CI policy
Every cross-platform change should exercise TypeScript compilation, unit/contract tests, platform capability tests, Linux shell/static checks and package metadata validation.

Native packaging is a separate matrix job because native dependencies and Apple signing requirements vary by host.

## Release labels
DISCOVERY -> DEVELOPMENT -> CI-PASS -> PLATFORM-READY -> PACKAGING-READY -> RELEASE

A CI pass alone does not imply production readiness.
