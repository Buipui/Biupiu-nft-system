#ifndef BIUPIU_VISUAL_MATERIAL_H
#define BIUPIU_VISUAL_MATERIAL_H
#include <stdint.h>
#ifdef __cplusplus
extern "C" {
#endif
typedef struct { float base_color[4]; float metallic; float roughness; float emission[3]; float opacity; } biupiu_material_desc;
typedef uint64_t biupiu_material_id;
int biupiu_material_create(const biupiu_material_desc* desc,biupiu_material_id* out);
int biupiu_material_destroy(biupiu_material_id id);
#ifdef __cplusplus
}
#endif
#endif
