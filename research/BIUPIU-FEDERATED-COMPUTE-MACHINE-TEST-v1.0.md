# Biupiu Federated Compute + Machine Runtime Test v1.0
Date: 2026-09-21

## Main OS
Capability registration -> range validation -> workload requirements -> heterogeneous compute selection -> telemetry.

## Mini-OS
Native C++ ABI -> compute-unit topology -> minimum/preferred class selection -> fail-closed behavior. Rust mirrors the same selection semantics.

## Test cases
1. Valid capability accepted.
2. Out-of-range capability rejected.
3. GPU-required workload selects GPU.
4. NPU-required workload fails closed when unavailable.
5. Mini-OS C++ contract selects GPU and rejects unavailable NPU.
6. Mini-OS Rust unit tests mirror selection semantics.

## Verification boundary
IMPLEMENTED — STATIC TESTS REGISTERED — LIVE CI/HARDWARE VERIFICATION PENDING.
