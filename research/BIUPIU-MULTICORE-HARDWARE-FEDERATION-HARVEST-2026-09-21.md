# Biupiu Multicore Hardware Federation + Global OEM Harvest — 2026-09-21

## Execution scope
Federated harvest for AMD, Intel, Apple, foreign-language OEM ecosystems, public government/research sources, OpenBooks and GitHub. The harvest is an evidence/resource registry: it does **not** copy proprietary source, restricted material, credentials, vendor blobs, or undocumented bypasses into Biupiu.

## Canonical promotion pipeline
DISCOVER -> SOURCE VERIFY -> LICENCE/REDISTRIBUTION CHECK -> SECURITY REVIEW -> CAPABILITY NORMALISATION -> ADAPTER CONTRACT -> STATIC/UNIT TEST -> RUNTIME/DEVICE TEST -> REGRESSION -> PROVENANCE -> PROMOTE.

Translation or search relevance never equals technical validation.

## Processor federation

### AMD
Harvest targets:
- Zen-family x86-64 architecture descriptors.
- AOCL/BLAS-style dynamic dispatch patterns.
- AVX2/FMA3 and AVX-512 capability detection.
- AMD compiler target selection and architecture-specific optimisation.

Primary source evidence: AMD AOCL documentation describes dynamic dispatch across Zen/Zen2/Zen3/Zen4/Zen5 and generic x86-64 fallback; AMD AOCC documents `-march=znver1...` through `znver5`. 
Reference: https://docs.amd.com/r/en-US/57404-AOCL-user-guide/On-Non-AMD-Zen-Architectures
Reference: https://docs.amd.com/r/en-US/57222-AOCC-user-guide/Target-Selection

Biupiu rule: use runtime capability dispatch, never hard-code an AMD-only path into the durable C ABI.

### Intel
Harvest targets:
- AVX/AVX2/AVX-512/AVX10 capability classes.
- AMX matrix acceleration.
- oneDNN ISA dispatch.
- oneTBB NUMA/hybrid-core scheduling patterns.
- oneAPI/SYCL heterogeneous execution concepts.
- multi-stack GPU scheduling concepts where relevant to compute adapters.

Primary source evidence: Intel oneDNN documents ISA-specific optimisation and CPU/GPU abstraction; current release notes document AVX10.2/AMX paths. Intel oneTBB updates expose NUMA awareness and hybrid-core constraints.
References:
https://www.intel.com/content/www/us/en/developer/tools/oneapi/onednn.html
https://www.intel.com/content/www/us/en/developer/articles/release-notes/onednn/2026.html
https://www.intel.com/content/www/us/en/developer/articles/release-notes/oneapi-toolkit/2026.html

### Apple
Harvest targets:
- arm64/Apple Silicon CPU capability boundary.
- Accelerate/BNNS/vImage.
- Metal compute/graphics boundary.
- iOS/iPadOS/macOS shared capability model.
- universal macOS arm64+x86_64 build strategy.
- Mac Catalyst / iOS-on-Mac compatibility.
- runtime feature detection instead of platform assumptions.

Primary source evidence: Apple documents Accelerate for vectorised CPU computation, Metal for Apple GPU compute/graphics, and universal binaries for arm64+x86_64 macOS. Apple also documents iOS apps on Apple-silicon Macs and platform capability differences.
References:
https://developer.apple.com/accelerate/
https://developer.apple.com/metal/
https://developer.apple.com/documentation/apple-silicon/porting-your-macos-apps-to-apple-silicon
https://developer.apple.com/documentation/apple-silicon/running-your-ios-apps-in-macos

## Cross-compatibility matrix

| Capability | AMD x86-64 | Intel x86-64 | Apple arm64 | Biupiu contract |
|---|---|---|---|---|
| Baseline ISA | x86-64 | x86-64 | arm64 | required |
| SIMD | SSE/AVX family | SSE/AVX family | NEON/Apple vector units | capability-dispatched |
| Matrix acceleration | model-dependent | AMX on supported parts | platform/model dependent | optional accelerator |
| CPU math | AOCL/BLAS compatible paths | oneMKL/oneDNN compatible paths | Accelerate/BNNS | adapter only |
| GPU compute | vendor/runtime dependent | oneAPI/Xe where available | Metal | separate GPU adapter |
| NUMA/hybrid scheduling | runtime/OS dependent | hybrid/NUMA-aware runtime | SoC shared-memory model | scheduler abstraction |
| macOS | Intel Macs supported historically | Intel Macs | Apple Silicon native | universal build |
| iOS/iPadOS | N/A | N/A | native arm64 | iOS adapter |
| Durable ABI | C | C | C ABI/Objective-C/Swift bridge | C ABI |
| Native high performance | C/C++ | C/C++ | C/C++/Swift/Metal | C++/platform adapter |
| Verification state | source contract | source contract | source contract | runtime/device verification OPEN |

## iOS functionality added to the architecture
The canonical iOS target now maps to:
UI/application -> Swift/SwiftUI/UIKit boundary -> C ABI -> Rust/C++ services -> DMS/Intelligence.

Platform-specific services must remain behind capability adapters:
- camera/sensors/location
- secure storage/keychain
- Metal
- Accelerate
- background execution constraints
- notifications
- device identity/attestation where publicly supported.

No claim of an App Store-ready iOS build is made by this harvest.

## Foreign-language/OEM federation
Search axes added for Chinese, Japanese and Korean sources plus European/global technical sources. Discovery sources include public GitHub repositories, vendor documentation, standards, OEM developer portals and community indexes.

Observed public GitHub patterns include:
- T-Head/Xuantie RISC-V BSP references through RT-Thread.
- Nuclei RISC-V BSP references through RT-Thread.
- oneAPI samples and vendor-neutral acceleration examples.
- community Android/OEM tooling.

OEM rule: public interface and licence first; OEM-specific code is an adapter, never a core dependency.

## Government / research harvest
Reviewed public source routes for MIT, NASA, DARPA, NSA and U.S. homeland cybersecurity/CISA. DARPA SSITH is particularly relevant to hardware/firmware security architecture: it explicitly targets hardware vulnerabilities and classes such as buffer errors, information leakage, resource management, numeric errors and privilege/access-control weaknesses.
Reference: https://www.darpa.mil/research/programs/ssith

Government/research material is treated as evidence and architecture input only. Restricted material is not harvested.

## OpenBooks + GitHub
OpenBooks is retained as a discovery source for openly accessible technical books/material. GitHub is retained as the implementation discovery layer. Search results are registered by provenance; code is not copied into the proprietary runtime merely because it is public.

## Multi-core security module federation
Canonical Biupiu security modules:
1. CPU feature discovery
2. execution-domain isolation
3. privilege boundary
4. memory permission boundary
5. secure/verified boot contract
6. device capability gating
7. scheduler/resource policy
8. provenance/audit logging
9. fault containment
10. fail-closed actuation policy.

## Multi-core optimisation module federation
Canonical optimisation modules:
1. ISA runtime dispatch
2. vector width selection
3. cache-aware tiling
4. NUMA topology discovery
5. hybrid-core affinity
6. work stealing/task scheduling
7. accelerator offload
8. memory locality
9. deterministic/reproducible mode
10. telemetry-driven tuning.

## Conflict resolution / extermination pass
Resolved at architecture level:
- Vendor-specific APIs are forbidden from becoming the durable core ABI.
- ISA-specific optimisations are optional dispatch paths, not assumptions.
- iOS/macOS code is separated from the common C ABI.
- Third-party code remains external until licence/security/build/test gates pass.
- Security policy remains authoritative over performance optimisation.
- Runtime capability detection outranks compile-time branding.
- No harvested source is promoted solely from search relevance.

## Repository housekeeping result
- New harvest registry: this document.
- New native dispatch contract: `core/multilang/cpu/multicore_dispatch.h`.
- Cross-platform matrix to be updated with Apple/iOS and processor capability dispatch.
- Existing open-gate register remains authoritative for runtime/CI/device/UE5 evidence.
