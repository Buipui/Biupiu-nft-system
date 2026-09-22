# External Federation Integration — Android / Automotive / Instrumentation

## Gate result

### Implemented
- AOSP Mainline capability model.
- Pixel/GKI capability model.
- Android Auto public API boundary.
- Motorola MA2 accessory adapter boundary.
- AAWireless TWO accessory adapter boundary.
- Carlinkit 5.0 (2Air) accessory adapter boundary.
- Vector automotive SIL/HIL interface boundary.
- LSPosed/ART instrumentation boundary.
- Fail-closed capability registry.
- Static source-level integration test.
- External-source provenance documentation.

### Internal harvest / fault-finding rules
1. Detect duplicate APIs before adding a module.
2. Prefer existing Mini OS HAL, C ABI, Rust/C++ federation and Android capability contracts.
3. Keep proprietary firmware/tooling outside the native tree.
4. Never treat an accessory as available without device discovery.
5. Never treat an OEM/private API as an AOSP capability.
6. Never enable root/ART instrumentation by default.
7. Reject unresolved external identifiers instead of guessing.
8. Run semantic checks after every integration group.
9. Remove stale duplicate adapters during housekeeping.
10. Promote only after build + device verification.

### Current missing-module harvest
- Persistent encrypted notification store: still missing.
- Android Auto live projection/device test: missing.
- Accessory discovery tests for MA2/AAWireless TWO/2Air: missing.
- Vector live CAN/CAN-FD HIL connector: missing; proprietary host tooling is required for real Vector hardware.
- LSPosed live Zygisk/ART runtime test: missing and intentionally isolated.
- GSM Flags 2.0: unresolved identity.
- Full AOSP/Pixel platform build integration: separate platform tree/build gate, not an app-module dependency.

### Housekeeping / conflict policy
- No proprietary binary was copied.
- No external framework is allowed to override the Mini OS authority boundary.
- Public Android API code remains in the Android module; native C++/Rust contracts remain in their existing layers.
- Duplicate functionality is resolved by adapter selection rather than parallel competing implementations.

### Verification
**SOURCE STRUCTURE: PASS**
**SEMANTIC FAIL-CLOSED CHECK: PASS**
**NATIVE ANDROID BUILD: OPEN**
**LIVE DEVICE/ACCESSORY: OPEN**
**PHYSICAL AUTOMOTIVE HIL: OPEN**
