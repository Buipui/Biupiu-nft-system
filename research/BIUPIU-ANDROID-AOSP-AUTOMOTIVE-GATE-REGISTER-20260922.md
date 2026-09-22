# Biupiu Android / AOSP / Automotive Federation Gate Register — 2026-09-22

## Purpose
Canonical library record of the current gate state following the external AOSP/Pixel, Android Auto, automotive accessory, Vector and LSPosed federation harvest.

## Closed gates
| Gate | State | Evidence boundary |
|---|---|---|
| External federation harvest | CLOSED | Sources and capability identities recorded |
| Internal missing-module harvest | CLOSED | Missing runtime/device/platform work explicitly inventoried |
| Native adapter integration | CLOSED | Native registry and adapter source implemented |
| Guided fault finding | CLOSED | Duplicate/proprietary/OEM/physical false-positive checks passed |
| Semantic code checks | CLOSED | Fail-closed source-level semantic checks passed |
| Conflict/duplicate housekeeping | CLOSED | Duplicate authority and stale-adapter rules applied |
| Fail-closed safety boundaries | CLOSED | Unresolved/physical/proprietary capabilities cannot become usable automatically |
| Changelog / integration documentation | CLOSED | Canonical records updated |

## Open verification gates
| Gate | State | Reason |
|---|---|---|
| Android/Gradle actual build | OPEN | Requires executable Android SDK/Gradle environment |
| Live Android Auto projection | OPEN | Requires Android Auto-capable device/runtime |
| Motorola MA2 hardware verification | OPEN | Requires physical accessory |
| AAWireless TWO hardware verification | OPEN | Requires physical accessory |
| Carlinkit 5.0 (2Air) hardware verification | OPEN | Requires physical accessory |
| Vector CAN/CAN-FD HIL | OPEN | Requires Vector tooling/interface and HIL hardware |
| LSPosed/Zygisk/ART runtime | OPEN | Requires supported rooted test environment; intentionally not enabled by default |
| Persistent encrypted notification store | OPEN | Current implementation is not yet live encrypted persistent storage |
| Full AOSP/Pixel platform build | OPEN | Requires full Android platform source/build/device tree; not an app dependency |
| GSM Flags 2.0 | OPEN / UNRESOLVED | Identity could not be established confidently; no speculative integration |

## Architectural status
**Implementation phase: CLOSED.**

**Runtime/device/platform verification phase: OPEN.**

A gate is promoted to VERIFIED only after actual execution evidence exists. Repository/source inspection does not substitute for device, hardware, CI or platform-build evidence.

## Digital-first promotion rule
DEFINE CAPABILITY -> IMPLEMENT NATIVE CONTRACT -> SEMANTIC CHECK -> FAULT FIND -> HOUSEKEEP -> BUILD/CI -> RUNTIME -> DEVICE/HARDWARE -> REGRESSION -> PROMOTION.

## Canonical source records
- `mini-os/android/federation/AndroidCapabilityRegistry.md`
- `mini-os/android/EXTERNAL-FEDERATION-INTEGRATION.md`
- `research/BIUPIU-OS-DMS-SUBSYSTEM-MASTER-INDEX-v1.0.md`
- `research/BIUPIU-SYSTEM-CROSS-LINK-DIGEST-v1.1.md`
- `CHANGELOG.md`

**Status: REGISTERED / IMPLEMENTED SOURCE LAYER / SOURCE-LEVEL VERIFIED / RUNTIME VERIFICATION OPEN.**


## Gate 46 — Mini OS functional-first semantic repair — 22 September 2026

Internal interface/code reconciliation found a semantic mismatch in the Android capability registry: ADAPTER_ONLY capabilities were previously returned as usable by isUsable(). This could turn source-level adapter registration into a runtime capability claim, contrary to the Native Coding Philosophy and verification ladder.

### Corrective implementation
- isUsable() now means positive runtime-usable evidence only.
- isAdapterRegistered() explicitly represents source/contract availability without runtime claims.
- Android Auto projection is classified as ADAPTER_ONLY until Android Car APIs provide live evidence.
- Godot/Vulkan adapters remain adapter registrations and do not become live capabilities from source presence.
- Registry snapshots are defensive copies before exposure.
- Notification history lifecycle was corrected so Android context initialization occurs after Activity/service creation rather than in Activity field initializers.
- Notification history was upgraded from process-local memory to encrypted Android Keystore-backed persistence with bounded storage and fail-closed unreadable-state handling.
- Notification title/null handling was hardened.

### Build gate
A dedicated Mini OS Android Gradle workflow was added with Java 17, Gradle 8.9, Android SDK 35, compile and JVM-test stages. AGP 8.7.x requires Gradle 8.9 and supports API 35. citeturn0search2turn0search0

The repository still intentionally does not vendor an unverified Gradle wrapper JAR. The dedicated CI gate therefore provisions the pinned Gradle toolchain directly. This preserves the repository rule that generated/binary build inputs require provenance and verification.

### Verification state
SOURCE SEMANTIC REPAIR: IMPLEMENTED
INTERFACE/IMPLEMENTATION RECONCILIATION: COMPLETED
FUNCTIONAL NOTIFICATION PATH: IMPLEMENTED
CI BUILD GATE: REGISTERED / EXECUTION PENDING OBSERVED RESULT
ANDROID DEVICE/EMULATOR: OPEN
GPU/GODOT/VULKAN RUNTIME: OPEN
FULL AOSP/PIXEL PLATFORM BUILD: OPEN

No runtime or release claim is made until the corresponding execution evidence exists.
