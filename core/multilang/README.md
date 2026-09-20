# Biupiu Multi-Language Core Boundary

This directory is the executable architecture seed for the C/C++/Rust core-language protocol.

## Contract
Hardware/platform -> C ABI -> Rust/C++ services -> OS validation -> DMS -> Intelligence.

## Rules
- The C ABI is the durable interoperability boundary.
- Rust owns safety-sensitive kernel invariants where practical.
- C++ remains the native high-performance/simulation/geometry layer.
- C++ ABI/STL types do not cross the durable ABI.
- Third-party dependencies remain external until licence, security, build, smoke and regression gates pass.
- Generated or translated code must be treated as untrusted until compiled and tested.

## Verification
The Rust boundary is a source-level prototype. It is not yet a host-runtime or hardware validation result.

Required next tests:
1. cargo check/test
2. C header compile test
3. Rust/C ABI link test
4. C++ compile test against the contract
5. sanitizers/fuzz/property tests
6. cross-platform CI
7. regression and provenance record
