/* Biupiu OS kernel baseline contract.
 * The boot ABI is shared with Mini-OS; architecture-specific HALs implement
 * the privileged operations behind these interfaces.
 */
#include "../mini-os/include/biupiu_boot_contract.h"
#include <stdint.h>
#include <stddef.h>

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
