# BIUPIU-AI78 — Linux/Unix/DOS/C++ Runtime Integration Gate v1.0

Date: 2026-09-21
Parent: AI-77
Status: IMPLEMENTED / RUNTIME TEST DEFINED / CI EVIDENCE PENDING

## Objective
Move the hardened Linux/Biupiu Core architecture into a controlled, executable userspace runtime smoke gate using the system's Linux/Unix/POSIX foundation and C++ userspace layer.

## Compatibility contract
- Linux remains the kernel authority.
- Unix/POSIX interfaces are the portability boundary for core userspace services.
- C++17+ is the native Biupiu Core userspace implementation target.
- DOS compatibility is treated as a legacy/tooling boundary, not as a kernel authority or security bypass.
- Kernel-internal APIs are not treated as stable application interfaces; Linux documents the userspace syscall ABI separately.
- Platform-specific security features are capability-detected and never assumed available.

## Executable smoke coverage
1. Linux kernel identification through uname.
2. POSIX API availability.
3. C++17 compiler/runtime availability.
4. /proc and /sys visibility.
5. Safe fork/wait process lifecycle.
6. Read-only userspace OS metadata access.
7. Deterministic synthetic-fault containment path.

## Security boundary
This gate performs no malware execution, privilege escalation, secret handling, kernel mutation, contract deployment, network attack, or physical actuation. It is a userspace smoke test only.

## Federation integration
OBSERVE -> CLASSIFY -> ROUTE -> HARVEST -> CROSS-CHECK -> SANDBOX -> TEST -> LEARN -> EVIDENCE -> PROMOTION CHECK -> TRUST LOG -> UPDATE INDEX -> REGRESSION -> NEXT TASK

AI-78 specifically supplies the TEST/EVIDENCE input for the Linux/C++ runtime boundary.

## Gate status
Architecture: IMPLEMENTED
C++ smoke harness: IMPLEMENTED
CI workflow: IMPLEMENTED
Runtime result: PENDING until GitHub Actions evidence is observed
Kernel hardening proof: PENDING
LSM/seccomp/Landlock runtime proof: PENDING
Boot verification: PENDING
Update/rollback proof: PENDING
HIL/hardware proof: PENDING
Production certification: BLOCKED

## Research basis
Linux documents a stable userspace syscall ABI and explicitly distinguishes it from unstable in-kernel interfaces. Linux also provides exported userspace headers. Landlock is runtime-versioned and should be capability-detected rather than assumed.

## Result
AI-78 establishes the executable Linux/C++ bridge without changing the authority model. A passing CI run will verify the basic Linux/POSIX/C++ runtime path, but will not by itself certify kernel hardening or production readiness.
