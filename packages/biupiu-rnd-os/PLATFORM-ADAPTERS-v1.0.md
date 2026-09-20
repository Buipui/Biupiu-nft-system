# Biupiu R&D OS — Cross-Platform Adapter Contract v1.0

## Target matrix

| Target | Role | Primary runtime |
|---|---|---|
| Windows | high-performance desktop/R&D workstation | Tauri/Web + Node/Rust adapters |
| macOS | desktop/R&D workstation and Apple development host | Tauri/Web + native Apple integration |
| Linux | development, server, CI, scientific/HPC and automation host | Tauri/Web + POSIX/Rust/Python |
| Android | mobile control/client | Android + shared contracts |
| Web | browser fallback | PWA |

The shared orchestration and data contracts remain platform-neutral. OS-specific capabilities are exposed through adapters rather than scattered throughout the application.

### Adapter boundaries

- filesystem
- process execution
- networking
- secure credential/key storage
- notifications
- GPU/compute discovery
- repository operations
- simulation runners
- Blender/OpenUSD/graphics tooling
- device/sensor bridges

### Linux engineering baseline

Linux is a first-class development and validation target. CI should run shell/static checks on Ubuntu and exercise POSIX path handling, executable permissions, environment discovery and Python/Node tooling.

### macOS engineering baseline

macOS is a first-class desktop target. Production distribution must account for Apple code signing and notarization; CI may build unsigned artifacts for development, while release signing remains on an appropriately configured Apple runner.

### Windows engineering baseline

Windows remains a first-class desktop target. PowerShell and Windows path handling must be covered by CI.

### Android

Android consumes the same canonical IDs, research contracts and API schemas. Heavy simulation/rendering may remain on desktop/server nodes and be exposed through controlled jobs.

### Runtime strategy

Tauri 2 is the preferred desktop/mobile shell candidate where native footprint and system integration matter. Electron remains an alternative/reference for the mature Chromium/Node desktop model.

### Security

No platform adapter may receive private keys, tokens or credentials through source-controlled configuration. Secrets belong in platform secure storage or a server-side secret boundary.

### Acceptance

A platform is not marked RELEASED merely because source code compiles. It requires platform-specific build, smoke, filesystem, process, networking and packaging checks.
## PowerShell Gateway integration — 20 September 2026
The Windows platform adapter now routes approved host automation through the DOS-derived Biupiu PowerShell Gateway.
Boundary: Biupiu OS Core -> DOS command contract -> PowerShell Gateway -> allowlisted Windows operation -> evidence -> Digital Twin.
PowerShell is not a runtime authority. Host execution remains evidence-gated and platform-specific.
Gateway repository implementation: IMPLEMENTED.
Windows host runtime verification: PENDING / UNVERIFIED.