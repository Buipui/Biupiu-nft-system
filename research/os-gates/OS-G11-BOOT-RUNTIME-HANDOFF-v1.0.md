# OS-G11 Boot / Runtime Handoff v1.0
Status: CONTRACT IMPLEMENTED; runtime OPEN

Firmware/bootloader supplies normalized BootInfo to the Core. BootInfo must identify memory, CPU/architecture, firmware mode, framebuffer/console where available, storage/device descriptors and boot arguments. Runtime takes authority only after validation.