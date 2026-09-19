# Biupiu DOS Compatibility Integration v1.0

Date: 19 September 2026
Status: ARCHITECTURE + RESOURCE REGISTRY EXECUTED

Purpose: add a controlled DOS compatibility layer to Biupiu OS without replacing the authoritative Core OS.

External findings:
- Microsoft MS-DOS archive contains historical MS-DOS 1.25, 2.0 and 4.0 source/binaries and is archived/read-only.
- Microsoft published preserved 86-DOS 1.00 historical source/listing material in April 2026.
- FreeDOS is an open-source DOS-compatible operating system; FreeDOS 1.4 is the current official release.
- FreeDOS T2609 (September 2026) is a monthly test distribution with updated kernel/tools, UPX and translations.
- DOSBox-X has active 2026 releases; the 2026.08.31 release adds TeleDisk mounting and recent releases include device, filesystem, rendering and networking compatibility fixes.

Import policy:
External projects remain references/dependencies. Import only Biupiu adapter code, manifests, compatibility tests and provenance records unless a separate licence/security gate authorizes source incorporation.

Architecture:
Biupiu OS Core -> DOS Compatibility API -> Runtime Adapter -> FreeDOS / DOSBox-X / validated DOS environment -> legacy application

Host families:
Windows, Linux, macOS, Android, Web/WASM where supported, and future UE5/Bevy simulator environments through process/service adapters.

Compatibility targets:
DOS command semantics; FAT12/FAT16/FAT32 interfaces where supported; CONFIG.SYS/AUTOEXEC.BAT startup contracts; INT 21h and BIOS compatibility through runtime; 16-bit real-mode application boundary; legacy device emulation; code pages; floppy/disk images; deterministic sandboxing.

Foreign-language protocol:
Index DOS/FreeDOS internationalisation, code pages, Japanese DOS/V, multilingual command/help resources, Cyrillic/Latin/Greek legacy encodings and Unicode bridge utilities. Language resources are compatibility data, not translated source.

Safety:
Legacy binaries execute only inside explicit sandboxes. Network, filesystem, device and host-process access must be permissioned. Historical Microsoft source remains reference-only unless licence terms and compatibility review permit reuse.

Gate state:
DISCOVER PASS
STATIC/LICENCE/PROVENANCE REVIEW PASS for indexing
ARCHITECTURE PASS
SOURCE ADAPTER REGISTERED
HOST RUNTIME NOT YET VERIFIED
CI/runtime matrix OPEN
Production release OPEN

Next gate: implement platform adapters and run the DOS compatibility matrix on connected hosts.
