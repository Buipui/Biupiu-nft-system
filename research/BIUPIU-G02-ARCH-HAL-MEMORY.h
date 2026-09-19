#ifndef BIUPIU_G02_ARCH_HAL_MEMORY_H
#define BIUPIU_G02_ARCH_HAL_MEMORY_H

#include <stdint.h>
#include <stddef.h>

#define BIU_PAGE_SIZE 4096ULL
#define BIU_PAGE_ALIGN_MASK (BIU_PAGE_SIZE - 1ULL)

#define BIU_MEM_AVAILABLE 1U
#define BIU_MEM_RESERVED 2U
#define BIU_MEM_ACPI 3U
#define BIU_MEM_MMIO 4U

#define BIU_MAP_READ  (1ULL << 0)
#define BIU_MAP_WRITE (1ULL << 1)
#define BIU_MAP_EXEC  (1ULL << 2)
#define BIU_MAP_USER  (1ULL << 3)

struct biu_memory_region {
    uint64_t base;
    uint64_t length;
    uint32_t type;
    uint32_t flags;
};

struct biu_arch_info {
    uint16_t architecture;
    uint16_t word_size;
    uint32_t cpu_count;
    uint64_t feature_flags;
};

struct biu_memory_ops {
    int (*init)(const struct biu_memory_region *regions, size_t count);
    void *(*alloc_pages)(size_t count);
    int (*free_pages)(void *address, size_t count);
    int (*map)(uint64_t virtual_address, uint64_t physical_address, size_t pages, uint64_t flags);
    int (*unmap)(uint64_t virtual_address, size_t pages);
};

static inline int biu_range_page_aligned(uint64_t address, size_t pages) {
    if ((address & BIU_PAGE_ALIGN_MASK) != 0 || pages == 0) return 0;
    if (pages > (SIZE_MAX / BIU_PAGE_SIZE)) return 0;
    return 1;
}

static inline int biu_mapping_flags_valid(uint64_t flags) {
    return (flags & ~(BIU_MAP_READ | BIU_MAP_WRITE | BIU_MAP_EXEC | BIU_MAP_USER)) == 0;
}

#endif
