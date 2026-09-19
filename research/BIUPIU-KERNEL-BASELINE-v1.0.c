/* Biupiu OS kernel base contract skeleton.
 * Contract layer only: no privileged hardware operations are implemented here.
 * Architecture-specific HALs must satisfy these interfaces.
 */
#include <stdint.h>
#include <stddef.h>

typedef enum { BIU_FW_BIOS, BIU_FW_UEFI, BIU_FW_DEVICE_TREE, BIU_FW_UNKNOWN } biu_firmware_t;
typedef enum { BIU_ARCH_X86, BIU_ARCH_X86_64, BIU_ARCH_ARM64, BIU_ARCH_RISCV64, BIU_ARCH_UNKNOWN } biu_arch_t;

typedef struct {
    biu_firmware_t firmware;
    biu_arch_t arch;
    uint64_t memory_map;
    uint64_t memory_map_count;
    uint64_t framebuffer;
    uint64_t acpi_or_dt;
    uint64_t boot_params;
} biu_boot_info_t;

typedef struct {
    void* (*alloc_pages)(size_t pages);
    void  (*free_pages)(void* ptr, size_t pages);
    int   (*map)(uint64_t virt, uint64_t phys, size_t pages, uint64_t flags);
    int   (*unmap)(uint64_t virt, size_t pages);
} biu_memory_ops_t;

typedef struct {
    int (*register_irq)(uint32_t irq, void (*handler)(void*), void* context);
    int (*mask_irq)(uint32_t irq);
    int (*unmask_irq)(uint32_t irq);
} biu_interrupt_ops_t;

typedef struct {
    int (*enumerate)(void* inventory);
    int (*bind)(uint64_t device_id, uint64_t driver_id);
} biu_device_ops_t;

typedef struct {
    int (*open)(const char* path, uint64_t flags);
    int (*read)(int fd, void* buffer, size_t length);
    int (*write)(int fd, const void* buffer, size_t length);
    int (*close)(int fd);
} biu_vfs_ops_t;

/* Compatibility runtimes must enter through validated OS interfaces. */
typedef struct {
    int (*launch)(const char* image, const char* args);
    int (*sandbox_check)(uint64_t capability_mask);
} biu_runtime_ops_t;

/* Core invariant: compatibility/AI layers do not directly own kernel state. */
int biu_kernel_validate_boot(const biu_boot_info_t* boot);
int biu_kernel_register_memory(const biu_memory_ops_t* ops);
int biu_kernel_register_interrupts(const biu_interrupt_ops_t* ops);
int biu_kernel_register_devices(const biu_device_ops_t* ops);
int biu_kernel_register_vfs(const biu_vfs_ops_t* ops);
int biu_kernel_register_runtime(const biu_runtime_ops_t* ops);
