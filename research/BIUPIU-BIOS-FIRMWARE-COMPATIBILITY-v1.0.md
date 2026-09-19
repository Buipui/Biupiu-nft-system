# Biupiu BIOS/Firmware Compatibility v1.0

Date: 19 September 2026
Status: ARCHITECTURE EXECUTED; HARDWARE VALIDATION OPEN

## Objective
Make BIOS and modern firmware a first-class base-level compatibility boundary for Biupiu OS, while keeping firmware implementation separate from the OS kernel.

## Firmware layers
1. Legacy PC BIOS / INT 10h, 13h, 15h, 16h, 19h services as compatibility targets.
2. DOS boot/runtime boundary: MBR/boot sector, CONFIG.SYS/FDCONFIG.SYS, AUTOEXEC.BAT/FDAUTO.BAT, DOS kernel and shell.
3. Linux/x86 boot protocol: real-mode handoff, kernel header, command line, initrd and boot-loader contract.
4. UEFI/EFI: EFI executable handoff, EFI system partition, runtime services and firmware configuration interfaces.
5. Firmware reference projects: coreboot, SeaBIOS and TianoCore EDK II remain external references; no source is copied into Biupiu without a dedicated licence/security gate.

## Canonical Biupiu boot abstraction
Firmware -> Boot Discovery -> Boot Contract -> Hardware/Memory Map -> Kernel Loader -> Initramfs/Runtime -> Biupiu OS Core -> Compatibility Services -> DOS/Linux/other user-space adapters.

## Base-level contracts to add
- boot target and architecture descriptor
- firmware capability descriptor
- memory-map contract
- CPU feature contract
- framebuffer/display contract
- storage/partition contract
- timer/clock contract
- interrupt controller contract
- PCI/device enumeration contract
- ACPI/firmware-table discovery contract
- UEFI variable/runtime-service boundary
- boot parameters and initramfs contract
- serial/console early-boot contract
- secure/verified boot policy boundary
- recovery/fallback boot contract
- deterministic firmware/runtime provenance record

## Architecture targets
x86_16/real mode compatibility, i386, x86_64, ARM64 and future RISC-V adapter targets. BIOS-specific services are isolated to legacy x86 adapters; modern platforms use UEFI/device-tree/platform firmware contracts.

## Important distinction
BIOS is firmware, not the operating-system kernel. Biupiu should expose a stable firmware abstraction rather than embedding BIOS assumptions into the Core OS.

## Gate
DISCOVER PASS -> ARCHITECTURE PASS -> CONTRACTS DEFINED -> IMPLEMENTATION OPEN -> HARDWARE/VM VALIDATION OPEN.
