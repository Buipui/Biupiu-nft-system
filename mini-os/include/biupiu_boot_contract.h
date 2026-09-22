#ifndef BIUPIU_BOOT_CONTRACT_H
#define BIUPIU_BOOT_CONTRACT_H

#include <stdint.h>
#include <stddef.h>

#define BIU_BOOT_MAGIC UINT64_C(0x4249555049554241)
#define BIU_BOOT_CONTRACT_VERSION 1u

typedef enum {
    BIU_BOOT_BIOS = 1,
    BIU_BOOT_UEFI = 2,
    BIU_BOOT_DEVICE_TREE = 3
} biu_boot_firmware_t;

typedef enum {
    BIU_CPU_X86_64 = 1,
    BIU_CPU_ARM64 = 2,
    BIU_CPU_RISCV64 = 3,
    BIU_CPU_X86_LEGACY = 4
} biu_boot_arch_t;

typedef struct {
    uint64_t base;
    uint64_t length;
    uint32_t type;
    uint32_t flags;
} biu_memory_region_t;

typedef struct {
    uint64_t magic;
    uint32_t version;
    uint32_t size;
    biu_boot_firmware_t firmware;
    biu_boot_arch_t arch;
    uint64_t memory_map;
    uint64_t memory_regions;
    uint64_t framebuffer;
    uint64_t framebuffer_size;
    uint64_t acpi_or_dt;
    uint64_t command_line;
    uint64_t initrd;
    uint64_t initrd_size;
    uint64_t firmware_table;
    uint64_t provenance_id;
} biu_boot_info_t;

static inline int biu_boot_info_valid(const biu_boot_info_t *boot) {
    if (boot == NULL ||
        boot->magic != BIU_BOOT_MAGIC ||
        boot->version < BIU_BOOT_CONTRACT_VERSION ||
        boot->size < sizeof(biu_boot_info_t)) {
        return 0;
    }

    if (boot->firmware < BIU_BOOT_BIOS ||
        boot->firmware > BIU_BOOT_DEVICE_TREE) {
        return 0;
    }

    if (boot->arch < BIU_CPU_X86_64 ||
        boot->arch > BIU_CPU_X86_LEGACY) {
        return 0;
    }

    if (boot->memory_regions != 0u && boot->memory_map == 0u) {
        return 0;
    }

    return 1;
}

#endif
