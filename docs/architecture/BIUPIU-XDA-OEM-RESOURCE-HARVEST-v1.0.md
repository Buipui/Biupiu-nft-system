# Biupiu OEM Developer Resource Harvest — XDA / Android Ecosystem Gate v1.0

## Purpose
Use XDA Developers and related Android community material as a discovery channel for OEM/device integration patterns, while keeping authoritative implementation boundaries with Android and vendor developer documentation.

## XDA result
Direct XDA retrieval was unavailable during this gate (HTTP 502), so no XDA page was treated as verified source evidence. The repository already contains an XDA-compatible device-adaptation architecture based on public Android/OEM concepts.

## Integrated resource classes
- Device-tree/platform configuration references
- Kernel-source and device-kernel references
- Vendor HAL boundaries
- OEM power/background execution behaviour
- Camera/media stack differences
- Bluetooth/Wi-Fi connectivity behaviour
- USB device/host modes
- NFC and secure-element boundaries
- Sensor and hardware capability discovery
- Boot/recovery/device adaptation references
- GMS/non-GMS distribution boundaries
- OEM security/attestation boundaries

## Existing Biupiu integration points
- `OemCompatibilityRegistry` — vendor-neutral OEM profiles.
- `OemResourceRegistry` — maps resource classes to Biupiu adapter boundaries.
- `HardwareCapabilityRegistry` — hardware capability vocabulary.
- `BiupiuPlatformAdapter` — platform abstraction boundary.
- `PlatformTarget` — Android/desktop/iOS/Web target model.
- Secure session — Android Keystore/security boundary.
- Distribution — OEM stores remain distribution, not core architecture.

## Governance
XDA/community material is a discovery/reference input, not an automatic code source. No proprietary OEM blobs, private APIs, copyrighted source, credentials, bypasses, or device-specific binary payloads are imported by this gate.

For every future OEM integration:
1. identify the public technical interface;
2. verify vendor/Android documentation;
3. inspect licence and redistribution terms;
4. isolate the implementation behind the common Biupiu contract;
5. add capability detection;
6. test on the target device;
7. promote only after CI/device evidence.

## Status
- Resource architecture: **IMPLEMENTED**
- OEM module registry: **IMPLEMENTED**
- XDA live-source verification: **NOT VERIFIED — retrieval unavailable**
- Vendor-specific runtime implementation: **NOT VERIFIED**
- Physical OEM device testing: **PENDING**
- Binary/vendor blob integration: **NOT PERFORMED**

## Next promotion gate
Android OEM matrix build + emulator/device smoke tests, followed by target-device capability/HAL validation.
