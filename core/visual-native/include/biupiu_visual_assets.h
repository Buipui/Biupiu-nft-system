#ifndef BIUPIU_VISUAL_ASSETS_H
#define BIUPIU_VISUAL_ASSETS_H
#include <stdint.h>
#ifdef __cplusplus
extern "C" {
#endif
typedef uint64_t biupiu_image_id;
typedef struct { uint32_t width,height,channels; uint32_t format; uint8_t hdr; } biupiu_image_desc;
typedef struct { float exposure; float gamma; const char* display; } biupiu_color_transform;
int biupiu_image_create(const biupiu_image_desc* desc,biupiu_image_id* out);
int biupiu_image_destroy(biupiu_image_id id);
int biupiu_color_transform_validate(const biupiu_color_transform* t);
#ifdef __cplusplus
}
#endif
#endif
