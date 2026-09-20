# XENG-02 — Engine Discovery / Runtime Verification Gate

**Execution status:** PROTOCOL IMPLEMENTED

## Completed
- Added deterministic engine capability probing contract.
- Added asset fingerprint comparison for geometry/topology/material/source drift.
- Added connected-host discovery protocol.
- Preserved registered/integrated/connected/verified status separation.
- Added controlled UE5 -> Unity -> Lumion round-trip definition.

## Cannot be falsely marked complete
The repository connector cannot inspect or execute the user's locally installed UE5, Unity, Lumion, Blender, Visual Studio/VS Code or XR hardware. Therefore host connection and runtime verification remain OPEN.

## Next executable host evidence
`DISCOVER -> PROBE -> ROUND-TRIP -> DRIFT CHECK -> XR SMOKE TEST -> RECORD -> PROMOTE`

## Next gate
**XENG-03 — controlled canonical asset round-trip and provenance drift test.**
