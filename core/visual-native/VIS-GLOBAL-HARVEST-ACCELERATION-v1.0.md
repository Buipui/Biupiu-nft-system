# Biupiu Global Harvest / Acceleration Protocol v1.0
**Status:** SOURCE IMPLEMENTATION COMPLETE / HARDWARE PROVIDER VALIDATION OPEN
## Harvest layers
CPU SIMD/threads; adaptive task scheduling; Vulkan/DX12 provider probing; compute/ray tracing capability; asynchronous IO; parallel rendering; OpenUSD/OTIO/OpenSubdiv providers; C++20 core/C ABI; Rust isolated services; Python tooling.
## Evidence rule
Compile-time ISA flags are not hardware verification. GPU capability fields remain zero until real host API probes succeed. OEM binaries are never promoted from dumps alone.
## Smoke criteria
Capability probe succeeds; CPU thread count is non-zero; scheduler initializes; task submission succeeds; shutdown returns worker count to zero.
