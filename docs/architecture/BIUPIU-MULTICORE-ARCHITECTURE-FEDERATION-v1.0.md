# Biupiu Multicore Architecture Federation v1.0

## Canonical stack

Hardware CPU/SoC
-> Firmware/boot contract
-> C ABI/HAL
-> CPU capability discovery
-> scheduler/resource policy
-> Rust safety boundary
-> C++ simulation/geometry/compute
-> platform acceleration adapters
-> OS runtime
-> DMS/Digital Twin
-> Intelligence
-> applications/simulators.

## Core design rule

The processor is a capability provider, not the owner of the OS architecture.

AMD, Intel, Apple and future RISC-V implementations therefore converge on the same durable Biupiu contracts while retaining native acceleration internally.

## Processor dispatch

- x86-64: runtime feature detection; AMD Zen and Intel AVX-family paths are optional.
- arm64: Apple Silicon/iOS/macOS path through C ABI + native Apple adapters.
- riscv64: future adapter target.
- Generic fallback: portable C/C++ path.

## Security precedence

SECURITY POLICY -> CORRECTNESS -> DETERMINISM -> PERFORMANCE.

Performance optimisation may not bypass a security or validation gate.

## Build matrix extension

Desktop:
- Windows x86-64
- Linux x86-64/arm64
- macOS x86-64/arm64

Mobile:
- Android arm64/x86_64 where supported by the runtime
- iOS/iPadOS arm64

Research/embedded:
- ARM64
- RISC-V64
- vendor-specific SoC profiles behind adapters.

## iOS bridge

The iOS layer is a platform shell, not a second core:
Swift/SwiftUI/UIKit
-> C ABI
-> Rust/C++
-> DMS/Intelligence.

Metal and Accelerate are optional acceleration providers.

## Multi-core optimisation policy

Use:
- runtime CPU feature dispatch;
- topology-aware scheduling;
- NUMA locality;
- cache-aware workloads;
- SIMD/vector kernels;
- optional matrix/accelerator paths;
- deterministic mode for scientific validation.

Do not:
- require a vendor ISA for correctness;
- embed OEM SDK assumptions into the durable ABI;
- promote benchmark claims without measured evidence.

## Multi-core security policy

All execution domains pass through:
identity -> capability -> resource authority -> memory/IO boundary -> audit/provenance.

Actuation remains fail-closed.

## Gate status

ARCHITECTURE: IMPLEMENTED
SOURCE CONTRACT: ADDED
EXTERNAL RESOURCE HARVEST: REGISTERED
RUNTIME COMPILATION: PENDING
CI: PENDING
REAL HARDWARE: PENDING
iOS DEVICE: PENDING
macOS DEVICE: PENDING
AMD/INTEL HOST BENCHMARK: PENDING
