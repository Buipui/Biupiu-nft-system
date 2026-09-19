# Biupiu G01 Boot Foundation v1.0

Date: 19 September 2026
Status: IMPLEMENTATION CONTRACT EXECUTED

Research confirms a clean separation between firmware initialization and payload/OS handoff. coreboot's current architecture uses staged boot, hardware initialization, then payload handoff; UEFI/EDK II provides a separate firmware environment. Biupiu therefore keeps firmware adapters outside the kernel and defines one normalized boot handoff. citeturn0search0turn0search1turn0search17

## Boot flow
Firmware -> Biupiu Boot Adapter -> Normalized BootInfo -> Architecture HAL -> Kernel Entry -> Memory Init -> Early Console -> Interrupt/Timer Init -> Scheduler -> Device Discovery -> VFS -> Service Manager -> Userland.

## Initial implementation target
First executable milestone is a hosted/VM-safe x86_64 boot harness. It must validate BootInfo parsing and kernel-entry contracts before privileged hardware code is enabled.

## Payload strategy
Biupiu may consume ELF payloads and UEFI/firmware handoff data through adapters. coreboot documentation confirms ELF payload support and payload separation; these are architectural references, not copied code. citeturn0search2turn0search8

## Verification
No physical firmware flashing is part of this gate. QEMU/OVMF/UEFI and hosted tests precede hardware flashing.
