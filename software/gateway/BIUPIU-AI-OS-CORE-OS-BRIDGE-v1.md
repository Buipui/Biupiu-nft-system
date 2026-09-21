# Biupiu AI OS ↔ Biupiu Core OS Bridge v1

The AI OS is a separate subsystem. The Core OS owns machine resources and final execution authority.

## Message flow
AI OS → authenticated request → DMS/policy gate → Core OS command bus
Core OS → execution result/telemetry → DMS → AI OS

## Required modules
1. Identity/session
2. Capability registry
3. Request/response schema
4. DMS authorization
5. Command router
6. Telemetry/event ledger
7. Health/watchdog
8. Rollback controller
9. Learning event sink
10. Repository synchronizer

## Execution classes
- READ: repository/state inspection
- SIMULATE: sandboxed computation
- WRITE: mutable state; explicit approval
- PRIVILEGED: OS/device/security changes; explicit approval

## Android target
Use a native bound service/Binder interface or equivalent platform IPC. The first live target is a local authenticated bridge, not an unrestricted shell.

## Live criteria
- authenticated request
- schema-valid request
- granted capability
- allowlisted command
- returned result
- recorded event
- observable failure
- rollback path for mutable operations

This is a gate specification, not proof that a physical Android runtime is already live.
