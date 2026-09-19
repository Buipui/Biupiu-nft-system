# Biupiu Host-Safe Integration Gate v1.0

**Gate:** GPU-SYS-03  
**Date:** 19 September 2026  
**Purpose:** prepare the repository for safe local Windows/UE5/Android validation without installing or replacing system components.

## Execution policy
This gate is repository-side only. It creates validation contracts and diagnostics; it does not install drivers, replace the OS, modify boot configuration, alter GPU drivers, or execute third-party binaries.

## Preflight contract
1. Confirm the existing known-good Biupiu OS/Core Simulator starts.
2. Confirm the experimental module can be disabled independently.
3. Record the current repository commit as the rollback anchor.
4. Validate configuration before launch.
5. Detect available graphics APIs and GPU features rather than assuming them.
6. Load optional graphics/physics/upscaling modules only after capability checks.
7. Keep a native/fallback rendering path available.
8. Keep the existing physics implementation available if a new solver cannot initialise.
9. Keep native resolution/scaling available if FSR/XeSS is unavailable.
10. Write diagnostics to a separate test log; never overwrite authoritative configuration.
11. Abort only the affected experimental module on failure.
12. Require explicit promotion after successful runtime and benchmark tests.

## Test matrix
| Area | Safe preliminary test | Failure action |
|---|---|---|
| Core OS | start/stop smoke test | preserve core |
| Graphics | API capability detection | native/fallback renderer |
| Vulkan | loader/device detection | DX12/native fallback |
| DX12 | feature-level/device detection | Vulkan/native fallback |
| Ray tracing | capability query only | disable RT |
| Physics | solver initialisation test | existing solver |
| Upscaling | SDK availability/capability test | native scaling |
| Frame generation | capability test only | disable FG |
| Asset loading | read-only sample load | reject bad asset |
| AI layer | interface/permission test | keep AI disabled |
| Android | package/config validation only | preserve current build |
| Repository | integrity/index test | stop promotion |

## Explicit no-brick boundary
The test harness must never flash firmware, change BIOS/UEFI, replace GPU drivers, modify Windows system files, alter bootloader configuration, delete user data, overwrite the known-good Core OS, silently replace dependencies, execute arbitrary downloaded binaries, or expose secrets.

## Promotion rule
A successful repository test does not equal a successful hardware test.
`STATIC PASS -> FALLBACK PASS -> LOCAL RUNTIME PASS -> BENCHMARK PASS -> LICENCE REVIEW -> EXPLICIT PROMOTION`

## Gate status
Repository safety contract: READY.  
Local Windows/UE5 runtime: NOT YET EXECUTED.  
Android runtime: NOT YET EXECUTED.  
System-driver/OS modification: PROHIBITED by this gate.