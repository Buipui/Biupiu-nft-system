# Biupiu G02 Architecture HAL + Memory Contract v1.0

Date: 19 September 2026
Status: CONTRACT IMPLEMENTED; RUNTIME VALIDATION OPEN

## Scope
Define architecture-neutral contracts for CPU discovery and memory ownership before privileged implementations.

## Initial targets
- Primary: x86_64 hosted/VM harness
- Secondary: ARM64 and RISC-V64 contract compatibility
- Legacy: x86 real-mode adapter only

## Required contracts
- CPU feature and topology discovery
- Physical memory region classification
- Page allocation and release
- Virtual mapping and unmapping
- Page protection flags
- Overflow/alignment validation
- Zero-size and invalid-range rejection
- Explicit ownership and lifecycle tracking

## Promotion criteria
No architecture HAL is promoted until compile checks, contract tests, VM tests, and memory-safety checks pass. No physical hardware changes are authorized in this gate.
