#ifndef BIUPIU_VISUAL_MATERIAL_H
#define BIUPIU_VISUAL_MATERIAL_H
#include <stdint.h>
#ifdef __cplusplus
extern "C" {
#endif
typedef struct {
  float base_color[4];
  float metallic;
  float roughness;
  float emission[3];
  float opacity;
} biupiu_material_desc;
typedef uint64_t biupiu_material_id;
typedef struct {
  biupiu_material_id id;
  biupiu_material_desc desc;
  uint64_t canonical_hash;
} biupiu_material_info;
int biupiu_material_validate(const biupiu_material_desc* desc);
int biupiu_material_create(const biupiu_material_desc* desc, biupiu_material_id* out);
int biupiu_material_get(biupiu_material_id id, biupiu_material_info* out);
int biupiu_material_destroy(biupiu_material_id id);
#ifdef __cplusplus
}
#endif
#endif
