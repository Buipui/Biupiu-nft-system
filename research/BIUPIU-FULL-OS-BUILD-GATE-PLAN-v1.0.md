# Biupiu Full OS Build Gate Plan v1.0

Date: 19 September 2026
Status: EXTERMINATE PROTOCOL + BUILD GATES PREPARED

## Mission
Build a working, multi-platform Biupiu OS from firmware boundary through kernel, services, compatibility runtimes, graphics, networking, security, package/module system, AI integration and developer/user environments.

## Exterminate protocol
Before implementing a subsystem:
1. Identify the required capability.
2. Search official/proprietary public releases and historically published/dumped architecture material first.
3. Search authoritative open-source implementations second.
4. Compare architectures and retain only the minimum useful design/code patterns.
5. Record provenance and evidence.
6. Implement Biupiu-native interfaces rather than copying an implementation blindly.
7. Compile/test in an isolated branch or VM.
8. Promote only after regression, security and dependency checks.

Exterminate means removing duplicate, obsolete or conflicting abstractions from the Biupiu architecture; it does not mean deleting useful provenance or source history.

## Search protocol update: PUBLIC-RELEASE-FIRST
The research engine must classify sources in this order:
A. Official public software release/source archive
B. Official public binary/package/SDK/firmware release
C. Publicly released historical dump/reconstruction
D. Official project source repository
E. Mature open-source implementation
F. Community implementation/reference

A source being public does NOT automatically grant unrestricted reuse. Public-release discovery bypasses unnecessary rediscovery; it does not bypass applicable copyright, patent, trademark, security or redistribution requirements. Source can be indexed and architecturally studied before a reuse decision.

## Full OS gates
G00 Scope + architecture freeze
G01 Firmware/boot abstraction
G02 Architecture HAL: x86_64, ARM64, RISC-V64; legacy x86 adapter
G03 Memory manager
G04 Interrupts + timers
G05 Scheduler/process/thread model
G06 Device/PCI + driver framework
G07 Storage/partition/VFS
G08 Console/input/framebuffer
G09 IPC/service manager
G10 Networking
G11 Security/capabilities/sandbox
G12 Recovery/update/rollback
G13 Package/module/ABI system
G14 Native userland + shell
G15 DOS compatibility
G16 Linux compatibility/service integration
G17 Graphics/GPU API abstraction
G18 Audio/media
G19 Virtualisation/emulation
G20 AI/Intelligence service boundary
G21 Digital Twin/simulation service boundary
G22 Developer SDK/toolchain
G23 Installer/images/boot media
G24 CI + VM hardware matrix
G25 Physical hardware validation
G26 Performance/power/thermal validation
G27 Security audit
G28 Release candidate
G29 Production release

## Multi-platform strategy
Native core: x86_64, ARM64, RISC-V64.
Legacy: x86 real-mode/BIOS/DOS adapter.
Firmware: BIOS + UEFI + Device Tree/platform firmware.
Virtual: QEMU/OVMF and other validated hypervisors.
Host development: Windows + Linux + macOS.
Mobile/embedded: Android/Linux-derived and ARM64 platform adapters where practical.
UE5/Bevy: service/process integration, never kernel coupling.

## Definition of done
A platform is not marked working until it boots, initializes memory, schedules work, discovers devices, mounts storage, exposes console/input, passes IPC/security tests, can launch user-space, records provenance, and survives recovery/regression tests.
