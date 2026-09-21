#ifndef BIUPIU_NATIVE_RENDER_H
#define BIUPIU_NATIVE_RENDER_H
#include <stdint.h>
#ifdef __cplusplus
extern "C" {
#endif
typedef uint64_t biupiu_render_device_id; typedef uint64_t biupiu_render_target_id;
typedef enum { BIUPIU_GPU_NONE=0, BIUPIU_GPU_VULKAN=1, BIUPIU_GPU_DX12=2 } biupiu_gpu_backend;
typedef struct { biupiu_gpu_backend backend; uint32_t api_major,api_minor; uint64_t vram_bytes; uint8_t compute,ray_tracing,hdr; } biupiu_gpu_caps;
typedef struct { uint32_t width,height; uint32_t format; uint32_t samples; uint8_t hdr; } biupiu_render_target_desc;
typedef struct { biupiu_render_device_id device; biupiu_render_target_id target; uint32_t frame_index; } biupiu_render_context;
int biupiu_render_probe(biupiu_gpu_backend backend, biupiu_gpu_caps* out);
int biupiu_render_create_device(biupiu_gpu_backend backend,biupiu_render_device_id* out);
int biupiu_render_create_target(biupiu_render_device_id device,const biupiu_render_target_desc* desc,biupiu_render_target_id* out);
int biupiu_render_begin(const biupiu_render_context* ctx);
int biupiu_render_end(const biupiu_render_context* ctx);
int biupiu_render_destroy_device(biupiu_render_device_id device);
#ifdef __cplusplus
}
#endif
#endif
