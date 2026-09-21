# Biupiu Mini-OS

Experimental native build surface for the Native Build + Initial Task Framework.

Authority boundary: Mini-OS is not Main OS. It may reuse governed contracts and native boundary patterns, but promotion into Main OS requires the existing fail-closed promotion gates.

Initial stack:
- C ABI/HAL boundary
- Rust core services
- C++ service/geometry boundary
- Multi-AI task federation
- Deterministic verification
- DMS/provenance event bridge

Build state: scaffold implemented; host/device runtime verification pending.
