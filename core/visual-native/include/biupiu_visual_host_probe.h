#ifndef BIUPIU_VISUAL_HOST_PROBE_H
#define BIUPIU_VISUAL_HOST_PROBE_H
#include <stdint.h>
#ifdef __cplusplus
extern "C" {
#endif
typedef struct {
  uint32_t struct_size;
  uint32_t cpu_threads;
  uint8_t avx2;
  uint8_t avx512;
  uint8_t neon;
  uint8_t vulkan_loader;
  uint8_t vulkan_device;
  uint32_t vulkan_api_major;
  uint32_t vulkan_api_minor;
  uint32_t vulkan_device_count;
  uint64_t vulkan_vram_bytes;
  uint8_t dx12_loader;
  uint8_t dx12_device;
  uint8_t dx12_ray_tracing;
  uint8_t dx12_hdr;
} biupiu_visual_host_caps;

typedef struct {
  const char* name;
  const char* version;
  uint8_t discovered;
  uint8_t linked;
} biupiu_visual_provider_probe;

int biupiu_visual_host_probe(biupiu_visual_host_caps* out);
int biupiu_visual_provider_probe_all(biupiu_visual_provider_probe* out, uint32_t capacity, uint32_t* written);
#ifdef __cplusplus
}
#endif
#endif
