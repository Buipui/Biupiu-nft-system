# VIS-NATIVE-11 — Host Provider & GPU Capability Gate v1.0

Status: SOURCE IMPLEMENTATION COMPLETE / HOST EXECUTION PENDING

## Scope
Add real host capability probing and optional SDK discovery without promoting unavailable providers.

## Implemented
- Native host probe reports CPU thread count and compile-time ISA flags.
- Vulkan probe is real when the Vulkan SDK/loader is discovered: creates a Vulkan instance, enumerates physical devices, API version and device-local memory.
- DX12 probe is real on Windows when D3D12 is linked: creates a D3D12 device and checks ray-tracing support.
- Provider discovery is explicit for OpenUSD, OpenTimelineIO, OpenSubdiv, MaterialX, OpenColorIO, OpenImageIO and OpenEXR.
- Provider states remain fail-closed: discovery/linkage evidence is required before HOST_READY.
- CMake keeps all external providers optional so the first-party native core remains buildable without third-party SDKs.

## Evidence
REGISTERED: host probe API and provider matrix.
IMPLEMENTED: host probe source, provider discovery wiring, smoke test.
HOST_TESTED: pending GitHub Actions execution.
REGRESSION_PASS: pending CMake/CTest execution.
VERIFIED: not claimed.

## Promotion rule
A provider may move from CONTRACT_ONLY to HOST_READY only after the CI/host evidence shows the SDK was discovered, linked and its runtime probe succeeded. Compile-time macro presence alone is not sufficient for runtime GPU claims.
