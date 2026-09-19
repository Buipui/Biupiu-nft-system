# Biupiu R&D OS — Cross-Platform Build Matrix v1.0

| Platform | Dev | CI | Package | Release gate |
|---|---:|---:|---|---|
| Windows | READY | REQUIRED | MSIX/installer or Tauri bundle | build + smoke |
| macOS | READY | REQUIRED | App bundle/DMG | build + signing + notarization |
| Linux | READY | REQUIRED | AppImage/deb/rpm/Flatpak as appropriate | build + smoke |
| Android | EXISTING | REQUIRED | APK/AAB | Android build + smoke |
| Web/PWA | EXISTING | REQUIRED | static/PWA | browser smoke |

## CI policy

Every change to the cross-platform OS should exercise:
- TypeScript compilation
- unit/contract tests
- platform capability tests
- Linux shell/static checks
- package metadata validation

Native packaging is a separate matrix job because native dependencies and Apple signing requirements vary by host.

## Release labels

DISCOVERY -> DEVELOPMENT -> CI-PASS -> PLATFORM-READY -> PACKAGING-READY -> RELEASE

A CI pass alone does not imply production readiness.
