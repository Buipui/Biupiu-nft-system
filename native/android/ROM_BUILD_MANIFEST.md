# Buipui Native Android ROM — AOSP Foundation Gate

Status: ARCHITECTURE-INTEGRATED / BUILD-NOT-YET-VERIFIED
Gate: Native Android Foundation
Target: AOSP-based Android distribution + installable APK layer

## Build contract
1. AOSP is the open-source Android foundation.
2. Buipui native components are integrated only at the layer where their privileges and lifecycle require them.
3. Every major component must have both a ROM integration path and, where technically appropriate, an APK/testable path.
4. Kernel code is restricted to kernel-appropriate security, hardware, performance and isolation functions.
5. No component is marked verified until it compiles, boots and passes its relevant functional/security test.

## Target layers
- Kernel
- Device tree / vendor / HAL
- Android framework
- System services
- System UI
- Privileged/system APKs
- Ordinary APKs
- Native C/C++ libraries
- Build / OTA / recovery
- Security and audit infrastructure

## Initial Buipui native modules
- Buipui System Core
- Buipui Intelligence bridge
- Multi-AI orchestration service
- DMS service
- Security/audit service
- Diagnostics/health service
- Acceleration/runtime service
- Repository/index bridge
- Buipui Control Centre APK
- Buipui Intelligence APK
- Buipui DMS APK

## Required verification states
DESIGNED -> INTEGRATED -> COMPILED -> BOOT-VERIFIED -> FUNCTION-VERIFIED -> SECURITY-VERIFIED -> DEVICE-VERIFIED

## Immediate next engineering gate
Acquire/select a concrete AOSP release and target device, establish the AOSP manifest/device configuration, then perform an unmodified AOSP build before adding Buipui changes. This provides the clean baseline required for regression attribution.
