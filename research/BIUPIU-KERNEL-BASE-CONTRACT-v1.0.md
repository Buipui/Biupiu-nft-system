# Biupiu Kernel Base Contract v1.0

Date: 19 September 2026
Status: BASE CONTRACTS IMPLEMENTED

This is the hardware-independent contract boundary for the future native Biupiu kernel. It is intentionally a contract/specification layer first; hardware-specific implementations belong under architecture/ and drivers/.

## Required base interfaces
- boot_info: firmware type, boot mode, architecture, memory map, framebuffer, ACPI/DT pointers, boot parameters
- cpu: feature discovery, topology, architecture capabilities
- memory: physical-page allocation, virtual mapping, protection and allocator diagnostics
- interrupts: IRQ registration, masking, dispatch and timer source
- scheduler: task/thread identity, state transitions and time slice contract
- device: enumeration, identity, capabilities and driver binding
- storage: block device, partition and filesystem-provider contract
- vfs: path, file, directory and mount abstractions
- console: early boot serial/framebuffer console
- clock: monotonic and wall-clock services
- ipc: message/channel capability boundary
- network: interface discovery and packet/socket-provider boundary
- security: capability/permission checks and sandbox boundary
- recovery: boot slot, rollback and safe-mode contract

## Non-negotiable invariants
1. No driver may directly mutate authoritative kernel state without a kernel interface.
2. No compatibility runtime may bypass security or filesystem/device policy.
3. Physical memory ownership is explicit.
4. Interrupt handlers remain bounded and cannot perform unbounded application work.
5. Hardware discovery is recorded before driver binding.
6. Every boot records firmware, architecture and kernel provenance.
7. Failed module promotion must have a rollback path.
8. AI/automation may propose changes but cannot bypass kernel validation.

## Compatibility adapters
DOS, Linux and future Windows/UE5/Bevy integrations consume these interfaces rather than reaching directly into hardware.

## Implementation order
boot_info -> architecture HAL -> memory -> interrupts/timer -> scheduler -> device/PCI -> storage/VFS -> console -> IPC -> network -> security -> recovery -> compatibility runtimes.
