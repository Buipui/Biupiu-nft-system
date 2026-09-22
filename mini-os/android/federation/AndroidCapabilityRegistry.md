# Android Capability Registry — 2026-09-22

## New federation records

| Capability | State | Native treatment |
|---|---|---|
| Motorola MA1 | DEVICE_REQUIRED | Native transport boundary; no firmware copied |
| AAWireless TWO | DEVICE_REQUIRED | Existing transport boundary retained |
| Ottocast U2-Air | DEVICE_REQUIRED | Native transport boundary; no firmware copied |
| Motorola MA2 | DEVICE_REQUIRED | Existing transport boundary retained |
| Carlinkit 5.0 (2Air) | DEVICE_REQUIRED | Existing transport boundary retained |
| SnapPerf | REFERENCE_ONLY | Root/kernel tuning reference; not enabled by default |
| dex2oat Optimizer | REFERENCE_ONLY | ART compilation reference; no global properties injected |
| AX Manager & Nexacore Combo | UNRESOLVED | Exact project identity not established; fail closed |
| GSM Flags 2.0 | UNRESOLVED | Existing unresolved identity retained |

## Selection rule

External products/modules are capability references, not binaries to vendor into Mini OS. Public protocol/API behavior can inform a native adapter. Proprietary firmware, private APIs, root hooks and vendor binaries remain outside the authoritative tree.

## Evidence

- AAWireless describes its adapter as a wireless Android Auto bridge and provides an app for configuration, updates and troubleshooting. citeturn1search0
- AAWireless' 2026 comparison material identifies MA1 alongside AAWireless TWO/TWO+ and MA2 as wireless Android Auto adapters. citeturn1search5
- Ottocast documents U2-AIR as a Bluetooth/Wi-Fi wireless adapter for wired CarPlay/Android Auto-capable vehicles. citeturn1search1turn1search2
- SnapPerf identifies itself as a Snapdragon-only rooted Android performance module supporting Magisk, KernelSU and APatch; it is therefore isolated from the normal non-root Mini OS path. citeturn1search4
- The dex2oat optimizer reference is an ART optimization module for Magisk/KernelSU/APatch and can change compilation behavior; no such system-wide change is promoted without target-version testing. citeturn0search2

## Verification boundary

SOURCE STRUCTURE: PASS
SEMANTIC FAIL-CLOSED CHECK: PASS
ANDROID/GRADLE BUILD: OPEN
DEVICE/ACCESSORY RUNTIME: OPEN
ROOT/ART PERFORMANCE RUNTIME: OPEN
