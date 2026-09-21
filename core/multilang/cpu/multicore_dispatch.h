#ifndef BIUPIU_MULTICORE_DISPATCH_H
#define BIUPIU_MULTICORE_DISPATCH_H

/*
 * Biupiu portable multicore capability contract.
 * Hardware-specific implementations remain behind this interface.
 * This header deliberately avoids vendor-specific ABI types.
 */

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef enum {
    BIUPIU_CPU_ARCH_UNKNOWN = 0,
    BIUPIU_CPU_ARCH_X86_64,
    BIUPIU_CPU_ARCH_ARM64,
    BIUPIU_CPU_ARCH_RISCV64
} biupiu_cpu_arch_t;

typedef struct {
    biupiu_cpu_arch_t arch;
    uint32_t logical_cpus;
    uint32_t physical_cpus;
    uint32_t numa_nodes;
    uint32_t feature_bits;
} biupiu_cpu_capabilities_t;

/* Portable capability bits. Vendor-specific names stay out of the ABI. */
enum {
    BIUPIU_CPU_SIMD_BASE       = 1u << 0,
    BIUPIU_CPU_SIMD_WIDE       = 1u << 1,
    BIUPIU_CPU_MATRIX_ACCEL    = 1u << 2,
    BIUPIU_CPU_HYBRID_CORES    = 1u << 3,
    BIUPIU_CPU_NUMA            = 1u << 4,
    BIUPIU_CPU_SECURE_BOOT     = 1u << 5,
    BIUPIU_CPU_HW_ISOLATION    = 1u << 6
};

/* Return 0 on success and populate the supplied structure. */
int biupiu_cpu_detect(biupiu_cpu_capabilities_t *out);

/* Select an implementation class without exposing vendor ABI details. */
int biupiu_cpu_select_kernel(const biupiu_cpu_capabilities_t *caps);

/* Return a stable feature-class mask for provenance and simulation. */
uint32_t biupiu_cpu_feature_mask(const biupiu_cpu_capabilities_t *caps);

#ifdef __cplusplus
}
#endif

#endif
