#ifndef BIUPIU_VISUAL_MEMORY_H
#define BIUPIU_VISUAL_MEMORY_H
#include <stdint.h>
#ifdef __cplusplus
extern "C" {
#endif

typedef uint64_t biupiu_memory_handle;
typedef enum { BIUPIU_MEMORY_BUFFER = 1, BIUPIU_MEMORY_IMAGE = 2 } biupiu_memory_resource_type;
typedef enum { BIUPIU_MEMORY_CPU = 1, BIUPIU_MEMORY_UPLOAD = 2, BIUPIU_MEMORY_GPU_LOCAL = 3, BIUPIU_MEMORY_READBACK = 4 } biupiu_memory_domain;

typedef struct {
  uint64_t size_bytes;
  uint64_t alignment_bytes;
  biupiu_memory_resource_type resource_type;
  biupiu_memory_domain domain;
  uint32_t flags;
} biupiu_memory_request;

typedef struct {
  uint64_t capacity_bytes;
  uint64_t reserved_bytes;
  uint64_t live_bytes;
  uint64_t allocation_count;
  uint64_t peak_live_bytes;
} biupiu_memory_stats;

typedef struct {
  uint64_t size_bytes;
  uint64_t alignment_bytes;
  uint32_t resource_type;
  uint32_t domain;
  uint32_t flags;
  uint8_t live;
} biupiu_memory_info;

int biupiu_memory_system_init(uint64_t capacity_bytes);
void biupiu_memory_system_shutdown(void);
int biupiu_memory_allocate(const biupiu_memory_request* request, biupiu_memory_handle* out_handle);
int biupiu_memory_release(biupiu_memory_handle handle);
int biupiu_memory_get_stats(biupiu_memory_stats* out);
int biupiu_memory_get_info(biupiu_memory_handle handle, biupiu_memory_info* out);
int biupiu_memory_validate(void);
void* biupiu_memory_map(biupiu_memory_handle handle);
int biupiu_memory_unmap(biupiu_memory_handle handle);

#ifdef __cplusplus
}
#endif
#endif
