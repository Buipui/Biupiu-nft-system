#ifndef BIUPIU_BOOT_CONTRACT_H
#define BIUPIU_BOOT_CONTRACT_H

#include <stdint.h>

#define BIU_BOOT_MAGIC UINT64_C(0x4249555049554241)

typedef enum { BIU_BOOT_BIOS=1, BIU_BOOT_UEFI=2, BIU_BOOT_DEVICE_TREE=3 } biu_boot_firmware_t;
typedef enum { BIU_CPU_X86_64=1, BIU_CPU_ARM64=2, BIU_CPU_RISCV64=3, BIU_CPU_X86_LEGACY=4 } biu_boot_arch_t;

typedef struct { uint64_t base, length; uint32_t type, flags; } biu_memory_region_t;

typedef struct {
    uint64_t magic;
    uint32_t version, size;
    biu_boot_firmware_t firmware;
    biu_boot_arch_t arch;
    uint64_t memory_map, memory_regions;
    uint64_t framebuffer, framebuffer_size;
    uint64_t acpi_or_dt, command_line;
    uint64_t initrd, initrd_size;
    uint64_t firmware_table, provenance_id;
} biu_boot_info_t;

static inline int biu_boot_info_valid(const biu_boot_info_t *b) {
    return b && b->magic == BIU_BOOT_MAGIC && b->version >= 1 &&
           b->size >= sizeof(biu_boot_info_t) &&
           b->arch >= BIU_CPU_X86_64 && b->arch <= BIU_CPU_X86_LEGACY;
}

#endif
