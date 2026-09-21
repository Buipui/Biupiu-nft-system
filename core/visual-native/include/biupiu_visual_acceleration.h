#ifndef BIUPIU_VISUAL_ACCELERATION_H
#define BIUPIU_VISUAL_ACCELERATION_H
#include <stdint.h>
#ifdef __cplusplus
extern "C" {
#endif
typedef struct { uint8_t simd,avx2,avx512,neon; uint8_t vulkan,dx12,compute,ray_tracing; uint32_t cpu_threads; uint64_t vram_bytes; } biupiu_acceleration_caps;
int biupiu_acceleration_probe(biupiu_acceleration_caps* out);
#ifdef __cplusplus
}
#endif
#endif
