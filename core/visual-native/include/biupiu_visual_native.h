#ifndef BIUPIU_VISUAL_NATIVE_H
#define BIUPIU_VISUAL_NATIVE_H
#include <stdint.h>
#ifdef __cplusplus
extern "C" {
#endif
#define BIUPIU_VISUAL_API_V1 1u
typedef uint64_t biupiu_visual_handle;
typedef uint64_t biupiu_visual_job;
typedef uint64_t biupiu_visual_asset_id;
typedef enum { BIUPIU_VISUAL_OK=0, BIUPIU_VISUAL_INVALID_ARGUMENT=1, BIUPIU_VISUAL_UNSUPPORTED=2, BIUPIU_VISUAL_PROVIDER_UNAVAILABLE=3, BIUPIU_VISUAL_IO_ERROR=4, BIUPIU_VISUAL_VALIDATION_FAILED=5, BIUPIU_VISUAL_CANCELLED=6 } biupiu_visual_status;
typedef enum { BIUPIU_RENDER_NATIVE=0, BIUPIU_RENDER_VULKAN=1, BIUPIU_RENDER_DX12=2, BIUPIU_RENDER_METAL=3, BIUPIU_RENDER_OPENGL=4, BIUPIU_RENDER_PROVIDER=5 } biupiu_render_backend;
typedef struct {
  uint32_t api_version;
  uint32_t feature_flags;
  uint32_t max_texture_size;
  uint32_t max_msaa_samples;
  uint64_t dedicated_video_memory_bytes;
  uint8_t ray_tracing;
  uint8_t compute;
  uint8_t hdr;
  uint8_t reserved;
} biupiu_visual_capabilities;
typedef struct {
  biupiu_visual_asset_id scene_asset;
  biupiu_render_backend backend;
  uint32_t width, height, frame_start, frame_end;
  double frame_rate;
  uint32_t flags;
} biupiu_render_request;
typedef struct {
  biupiu_visual_asset_id animation_asset;
  uint32_t frame_start, frame_end;
  double frame_rate;
  uint32_t flags;
} biupiu_animation_request;
typedef struct {
  biupiu_visual_asset_id sequence_asset;
  uint32_t width, height, codec, container, frame_start, frame_end;
  double frame_rate;
  uint32_t flags;
} biupiu_video_request;
biupiu_visual_status biupiu_visual_get_capabilities(biupiu_visual_capabilities* out_capabilities);
biupiu_visual_status biupiu_visual_render_submit(const biupiu_render_request* request, biupiu_visual_job* out_job);
biupiu_visual_status biupiu_visual_animation_submit(const biupiu_animation_request* request, biupiu_visual_job* out_job);
biupiu_visual_status biupiu_visual_video_submit(const biupiu_video_request* request, biupiu_visual_job* out_job);
biupiu_visual_status biupiu_visual_job_status(biupiu_visual_job job, uint32_t* out_state);
biupiu_visual_status biupiu_visual_job_cancel(biupiu_visual_job job);
biupiu_visual_status biupiu_visual_release(biupiu_visual_handle handle);
#ifdef __cplusplus
}
#endif
#endif
