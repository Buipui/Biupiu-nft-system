# Buipui Mini OS — Android External Federation Capability Registry

## Sources / capability families

### AOSP / Pixel
Harvested as open-source architecture references:
- AOSP Mainline modular system model: stable API/AIDL boundaries, APEX/APK modularity, atomic update/rollback.
- Pixel/GKI kernel architecture: generic kernel + vendor modules behind KMI.
- Pixel device/kernel manifests are treated as device-specific build inputs, not copied into the generic Mini OS app.

Native integration target:
- capability registry
- stable AIDL/API boundaries
- GKI/vendor separation
- device-profile adapters
- fail-closed feature detection

### Android Auto
Native Android Car App APIs are the supported application boundary. Projection and Automotive targets remain distinct capabilities.

### Motorola MA2 / MA1 family
The external accessory is treated as a wireless Android Auto transport/reference device. No proprietary Motorola firmware or binary is embedded. Integration is an accessory transport adapter boundary.

### AAWireless TWO
Capability adapter boundary:
- wireless Android Auto transport discovery
- connection state
- transport diagnostics
- accessory profile metadata

No proprietary AAWireless firmware/binaries are embedded.

### Carlinkit 5.0 (2Air)
Capability adapter boundary:
- wireless projection transport
- accessory discovery
- connection diagnostics
- profile/firmware metadata

No proprietary Carlinkit firmware/binaries are embedded.

### Vector automotive framework
Vector tooling is proprietary. Buipui therefore integrates the **interface concepts** needed for CAN/CAN-FD/LIN/Ethernet simulation, SIL/HIL test orchestration, trace/diagnostic adapters and virtual ECU boundaries. Proprietary Vector libraries are not copied into the repository.

### LSPosed / modern ART-hooking ecosystem
LSPosed is GPL-3 and is a Zygisk/ART-hooking framework with LSPlant at its core. Buipui integration is isolated behind an optional instrumentation adapter. The native Android build does not silently enable root, Zygisk or application hooking.

### GSM Flags 2.0
Identity could not be established with sufficient confidence from the external federation search. It is registered as an unresolved source identifier rather than inventing an implementation. Integration remains OPEN pending the exact project/package/repository reference.

## Governance
- External proprietary code/binaries: NOT COPIED.
- Open-source code: license review required before vendoring.
- Capability adapters may be implemented natively from public Android APIs/protocols.
- Root/hooking functionality is opt-in and isolated from the normal Mini OS execution path.
- Safety-critical automotive control remains behind the existing verified adapter boundary.


### Simulator federation
The Android build registers governed capability identities for:
- Project Chrono / vehicle-multiphysics
- OpenStudio / architecture-building-design
- EnergyPlus / building-energy
- OpenSim / movement-biomechanics-environment agents

The Android boundary is capability discovery and job/state exchange. Desktop/server simulator binaries are not embedded. Runtime promotion requires Android-compatible native build, ABI/dependency verification, smoke, regression and device evidence.
