# Linux Kernel ↔ Biupiu OS Core Contract v1.0

Status: IMPLEMENTED / STATIC VERIFIED / RUNTIME PENDING

Linux remains the kernel. Biupiu OS Core is a governed privileged system-control layer unless a future, separately verified kernel component is explicitly introduced.

## Authority order
1. Hardware/firmware root of trust
2. Linux kernel and kernel security mechanisms
3. Biupiu Core policy/control services
4. Domain services/components
5. Biupiu Intelligence
6. Applications and research workloads

A higher layer cannot grant authority that a lower security boundary has denied.

## Required interfaces
syscall/process; LSM/security policy; capability/credential; IPC/message schema; filesystem/mount namespace; network namespace/firewall; device/IOMMU where supported; audit/provenance; update/rollback.

## Core rule
Biupiu Core may orchestrate policy, lifecycle, evidence, health, routing and recovery; it must not bypass kernel enforcement.

## AI rule
Biupiu Intelligence may propose classifications, tests, remediation and configuration candidates. Promotion into authoritative OS policy requires deterministic validation and the existing governed promotion chain.

## Failure behavior
Missing authority, invalid evidence, policy conflict, failed regression, unexpected kernel state or unsafe actuation request => fail closed, log, quarantine where applicable, and require the next governed gate.

## Future kernel work
Any Biupiu-specific kernel patch/module must pass source review, reproducible build, signed-module policy, static analysis, kernel self-tests, boot test, security regression, fuzzing where appropriate, and hardware/HIL validation before promotion.
