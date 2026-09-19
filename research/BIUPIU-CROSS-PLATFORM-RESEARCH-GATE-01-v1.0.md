# Cross-Platform Research Gate 01 — OS Portability & Integration

## Objective

Upgrade the Biupiu R&D OS from Windows + Android to Windows + macOS + Linux + Android while retaining a shared research/data contract.

## Research conclusions

1. Tauri 2 provides a direct architectural path for Windows, macOS, Linux, Android and iOS from a common application architecture.
2. Electron remains a mature alternative for Windows/macOS/Linux desktop packaging.
3. NASA OSAL is directly relevant to the adapter principle: isolate application logic from operating-system implementations.
4. NASA GMAT demonstrates a mature engineering application operating across Windows, Linux and macOS.
5. OpenUSD provides a strong cross-application interchange layer for the 3D/world pipeline.
6. Repository knowledge-graph/RAG tooling can sit behind the platform-neutral intelligence layer rather than being tied to a single desktop OS.
7. Linux should be a first-class development/CI target, not merely a server afterthought.
8. macOS must have a release-specific signing/notarization gate.

## Architecture

Shared contracts -> Orchestrator -> Platform adapters -> Native services

Shared:
- research objects
- evidence states
- audit events
- provenance
- AI tool contracts
- knowledge graph/RAG contracts
- simulation job contracts

Platform-specific:
- filesystem
- process runner
- secure storage
- GPU discovery
- notifications
- packaging
- native graphics/system APIs

## Build matrix

Windows x64/ARM64 | macOS Intel/Apple Silicon | Linux x64/ARM64 | Android ARM64

Architecture-specific binaries must be built/tested on compatible runners or supported cross-compilation toolchains. Native dependencies and macOS signing are not assumed portable across build hosts.

## Linux checks

- POSIX path/permission checks
- Bash/Python tooling
- Node/TypeScript tests
- process execution sandbox
- container/CI smoke test

## macOS checks

- Intel/Apple Silicon target matrix where supported
- filesystem permissions
- keychain adapter boundary
- app bundle/DMG packaging
- signing/notarization gate

## Windows checks

- PowerShell path/process checks
- app package/installer
- Windows credential-store adapter boundary
- x64/ARM64 build targets where supported

## Android checks

- shared API/ID compatibility
- offline cache
- mobile authentication boundary
- Android build/readiness gate

## Intelligence layer

RAG, repository indexing and knowledge-graph services remain platform-neutral. Local execution can use native binaries; remote execution can use an API/MCP service.

## Exit criteria

A platform becomes READY only after source, static, unit, smoke and packaging checks pass. Runtime claims remain PENDING until the corresponding runner actually executes them.
