# Biupiu OS — Unix / Open-Systems Harvest & Integration v1.0

**Date:** 19 September 2026  
**Checkpoint:** OS-UNIX-HARVEST-01  
**Status:** RESEARCH HARVESTED; ARCHITECTURE INTEGRATED; RUNTIME VALIDATION OPEN

## Purpose

This record captures the Unix/open-operating-system research pass requested for Biupiu OS. It separates reusable architectural principles from third-party source code. External repositories remain references unless their individual licence, dependency, security and compatibility gates permit incorporation.

## Research families

### UNIX / Unix-like

- Unix process model, hierarchical filesystems, user/kernel separation and composable system services.
- xv6: educational reimplementation of Unix Version 6, useful for understanding a small complete kernel, process, memory, filesystem and system-call path. The MIT repository notes that the x86 version is no longer maintained and points to the RISC-V effort.
- NetBSD/OpenBSD: large Unix-like source trees useful for portability, build systems, device support, regression testing and mature userland organisation.

### Microkernel / fault isolation

- seL4: small microkernel with a strong verification/testing ecosystem; useful as a reference for minimal trusted computing bases, isolation, capability-oriented design and formal verification boundaries.
- MINIX 3: reference for modular microkernel organisation, service separation and driver fault isolation.
- QNX: reference for microkernel + message-passing IPC + cooperating system processes. QNX explicitly describes modularity as the key objective rather than kernel size alone.

### Modern Unix-like experimentation

- Redox OS: Rust-based microkernel Unix-like OS. Its own documentation states that it draws from MINIX, seL4, Plan 9, Linux, FreeBSD and OpenBSD and combines a microkernel with a broader user-space OS.
- Redox provides a useful reference for modern language/tooling choices, modular components, a unified resource API and an integrated build system.

## Open textbook harvest

OpenStax's operating-systems material was used as the open-textbook reference layer. It covers the standard OS boundary between user mode, kernel mode and hardware; process management; memory; filesystems; reliability; security; and monolithic versus microkernel designs.

The open-textbook material is used for conceptual verification, not as copied implementation.

## Integration decisions

1. **Do not clone a complete Unix implementation into Biupiu OS.**
2. Retain Unix-like concepts where they improve interoperability and developer usability.
3. Keep the Biupiu Core OS authoritative over hardware, memory, process/resource authority, permissions and release state.
4. Treat the AI/intelligence layer as a bounded user/service layer, not as an unrestricted kernel authority.
5. Keep the kernel/boot foundation small enough to test independently.
6. Use explicit IPC/service contracts so optional components can be replaced or disabled.
7. Preserve a POSIX-compatibility boundary as an adapter target rather than making POSIX the definition of the entire Biupiu architecture.
8. Add capability/isolation and provenance requirements to the service model.
9. Use VM-first validation before physical firmware/hardware promotion.
10. Preserve checkpoint/revert semantics around every integration stage.

## Proposed Biupiu OS layered model

Firmware / Boot
-> BootInfo contract
-> Architecture HAL
-> Memory + interrupt + scheduling primitives
-> Core IPC / capability boundary
-> Filesystem / storage services
-> Device / network services
-> Compatibility layer (POSIX/DOS/Linux adapters where appropriate)
-> Biupiu service bus
-> Intelligence / MATH / Digital Twin / Simulation services
-> Biupiu World and department applications

## New architectural rules

### Core authority
The Core OS owns authoritative machine state, permissions, memory/resource isolation, service registration, validation and promotion.

### Service authority
Higher-level modules request capabilities through explicit contracts. Failure of an optional service must not imply permission to modify the Core OS.

### Intelligence authority
AI can retrieve, classify, propose, simulate and prepare changes. It cannot silently promote an unverified kernel/firmware change.

### Compatibility authority
Compatibility layers are adapters. They must not redefine the canonical internal contracts.

### Checkpoint authority
A verified checkpoint is the recovery boundary. Experimental branches may diverge, but promotion requires smoke, integration, regression and provenance evidence.

## Candidate implementation queue

- OS-G03: scheduler/process contract
- OS-G04: IPC/message contract
- OS-G05: capability/permission contract
- OS-G06: interrupt/timer contract
- OS-G07: storage/filesystem contract
- OS-G08: device/driver service boundary
- OS-G09: POSIX compatibility boundary
- OS-G10: service bus
- OS-G11: boot/runtime handoff
- OS-G12: VM smoke-test harness
- OS-G13: regression/checkpoint manifest

## Evidence boundary

This pass establishes research and architecture. It does **not** claim that a native kernel, scheduler, filesystem, driver stack or physical BIOS/UEFI boot has been successfully executed on the development host.

Runtime closure remains a separate checkpoint requiring build output, boot evidence, test results and provenance.

## Source register

- OpenStax, Introduction to Computer Science, OS chapter: https://openstax.org/books/introduction-computer-science/pages/6-1-what-is-an-operating-system
- MIT PDOS xv6: https://github.com/mit-pdos/xv6-public
- Redox OS: https://github.com/redox-os/redox
- seL4: https://github.com/seL4/seL4
- seL4 Microkit: https://github.com/seL4/microkit
- NetBSD source: https://github.com/NetBSD/src
- OpenBSD source: https://github.com/openbsd/src
- QNX system architecture documentation: https://qnx.com/developers/docs/8.0/com.qnx.doc.neutrino.sys_arch/

## Checkpoint result

**OS-UNIX-HARVEST-01: ARCHITECTURE INTEGRATED.**

**Runtime implementation and VM/host validation: OPEN.**


## Ubuntu compatibility addition — 19 September 2026
The Biupiu OS compatibility plan now explicitly includes **Ubuntu/Linux compatibility**.

### Compatibility target
- Ubuntu user-space and package ecosystem compatibility is an adapter target, not the canonical Biupiu kernel architecture.
- Support should be tested against supported Ubuntu LTS environments first, with version-specific compatibility matrices rather than assuming universal compatibility.
- Ubuntu's kernel documentation confirms that Ubuntu uses Linux kernels with release-specific flavours/variants, module sets, hardware enablement and structured regression/SRU testing. citeturn0search1turn0search3turn0search9
- The compatibility layer should therefore isolate Ubuntu-specific assumptions behind adapters for boot, filesystem, device interfaces, packages, services and Linux/POSIX APIs.

### Homebrew/Linux developer compatibility
The developer background in custom ROM/Linux work is recorded as a design input for usability: the OS should provide a familiar Linux-oriented development path where practical, while keeping Biupiu's native contracts independent of Linux internals.

### Proposed Ubuntu bridge
Boot/runtime → Linux/POSIX compatibility → Ubuntu user-space adapter → package/service adapter → Biupiu native services.

Ubuntu compatibility is **planned/integrated at architecture level**; runtime compatibility is still OPEN until an Ubuntu VM/host test produces evidence.
