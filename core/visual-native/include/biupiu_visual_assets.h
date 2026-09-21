#ifndef BIUPIU_VISUAL_ASSETS_H
#define BIUPIU_VISUAL_ASSETS_H
#include <stdint.h>
#ifdef __cplusplus
extern "C" {
#endif
typedef uint64_t biupiu_image_id;
typedef enum { BIUPIU_ASSET_UNLOADED=0, BIUPIU_ASSET_CPU_READY=1, BIUPIU_ASSET_GPU_READY=2 } biupiu_asset_state;
typedef struct { uint32_t width,height,channels; uint32_t format; uint8_t hdr; } biupiu_image_desc;
typedef struct { float exposure; float gamma; const char* display; } biupiu_color_transform;
typedef struct { biupiu_image_id id; biupiu_image_desc desc; biupiu_asset_state state; uint64_t byte_size; uint64_t content_hash; } biupiu_image_info;
int biupiu_image_validate(const biupiu_image_desc* desc);
int biupiu_image_create(const biupiu_image_desc* desc,biupiu_image_id* out);
int biupiu_image_get(biupiu_image_id id,biupiu_image_info* out);
int biupiu_image_set_state(biupiu_image_id id,biupiu_asset_state state);
int biupiu_image_destroy(biupiu_image_id id);
int biupiu_color_transform_validate(const biupiu_color_transform* t);
#ifdef __cplusplus
}
#endif
#endif
