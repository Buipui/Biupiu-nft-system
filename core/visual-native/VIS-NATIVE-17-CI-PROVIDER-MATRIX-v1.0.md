# VIS-NATIVE-17 — CI Provider Matrix and Evidence Gate v1.0

Status: IMPLEMENTED — evidence reporting specification registered.

## Provider matrix

| Provider | Discovery | Linkage | Runtime fixture | Repeat determinism | Promotion |
|---|---|---|---|---|---|
| OpenUSD | CI-detected | CI-detected | required | required | fail-closed |
| OpenTimelineIO | CI-detected | CI-detected | required | required | fail-closed |
| OpenSubdiv | CI-detected | CI-detected | required | required | fail-closed |
| MaterialX | CI-detected | CI-detected | required | required | fail-closed |
| OpenColorIO | CI-detected | CI-detected | required | required | fail-closed |
| OpenImageIO | CI-detected | CI-detected | required | required | fail-closed |
| OpenEXR | CI-detected | CI-detected | required | required | fail-closed |

## Evidence states
- PASS: SDK linked, runtime fixture succeeds, and repeated canonical output matches.
- FAIL: SDK is linked but build/runtime/determinism validation fails.
- SKIPPED: SDK is unavailable; this does not fail the native core build.

No optional provider is promoted from compile-time discovery alone.

## Current limitation
This gate records the matrix contract and evidence policy. CI execution must populate actual host evidence before VERIFIED can be claimed.

## Next gate
VIS-NATIVE-18 — CI-generated machine-readable provider evidence artifact and host-specific promotion report.