# Biupiu Android / Native Boot Cross-Thread Reconciliation — 2026-09-22

## Scope

Cross-reference of the earliest native boot foundation with the later Android/AOSP and Mini-OS tracks.

### Historical anchors

1. **19 September 2026 — native kernel foundation**
   - `97cd8b23556c7a10c6d440e47951769ee8df8741`
   - Base kernel contract skeleton.
   - Original architecture order: BOOT -> HAL -> MEMORY -> IRQ -> SCHEDULER -> DEVICES -> VFS -> runtimes.

2. **19 September 2026 — G01 boot contract**
   - `d984ba10aedfb708afdbf5009ff8e4159ad8fdf8`
   - Normalised boot information contract.

3. **21 September 2026 — Android/Mini-OS integration**
   - Native Android shell, Mini-OS native contracts and Android federation adapters were added as separate layers.
   - The repository keeps source implementation separate from runtime/device proof.

## Reconciliation changes

- Canonical boot ABI is now `mini-os/include/biupiu_boot_contract.h`.
- Historical `research/BIUPIU-G01-BOOT-CONTRACT.h` remains a compatibility include and no longer defines a second ABI.
- `research/BIUPIU-KERNEL-BASELINE-v1.0.c` consumes the canonical ABI instead of redefining boot enums and structures.
- Boot validation now checks the contract version, firmware class, CPU architecture and the memory-map/count relationship.
- Android native CMake include paths were corrected so the scientific bridge resolves the canonical C++ header through the configured include directory.
- The Android shell remains a client/UI boundary; Mini-OS remains the experimental native layer. Android source presence is not treated as proof of a bootable physical OS.

## Coding-matrix rules applied

- One authoritative contract per interface.
- Interfaces before implementations.
- Fail closed on invalid or unresolved capability state.
- External/federated material remains an adapter/reference boundary until licence, dependency, security, build, runtime and regression evidence exists.
- Source-level semantic success does not promote a gate to runtime/device verification.
- Native Android uses the Gradle -> CMake/NDK build boundary for C/C++ code.

## Verification boundary

**Source cleanup: IMPLEMENTED.**

**Static/CI verification: OPEN until an observed workflow result exists.**

**Android APK build: OPEN.**

**Cuttlefish/AOSP boot: OPEN.**

**Physical-device boot/hardware validation: OPEN.**

This record preserves the historical distinction between contract implementation and actual boot/runtime evidence.
