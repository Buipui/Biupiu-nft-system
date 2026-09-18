# Biupiu Application Bundling Foundation v1.0

Gate 9 establishes separate application entry points for Android and Windows while keeping the Biupiu package layer shared.

## Targets

- Android: `apps/android/`
- Windows desktop: `apps/windows/`
- Shared application contract: `apps/shared/biupiu-app-contract.json`
- Shared TypeScript packages: `packages/*`

## Architecture

Native clients consume the same stable application contract and package responsibilities:

`Access → Main Hub → R&D OS → Department packages`

The native shells are client surfaces. Server/API authorization remains the final security boundary.

## Build status

This gate creates the application project foundations and CI structural verification. It does **not** claim that a signed Android APK, Windows installer, or production backend has been built.

## Next gate

Add real Android/Windows runtime adapters, dependency locking, native build runners and artifact publication after the shared contract is accepted.
