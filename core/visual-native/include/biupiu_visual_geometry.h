#ifndef BIUPIU_VISUAL_GEOMETRY_H
#define BIUPIU_VISUAL_GEOMETRY_H
#include <stdint.h>
#ifdef __cplusplus
extern "C" {
#endif
typedef uint64_t biupiu_mesh_id;
typedef struct { const float* positions; uint32_t vertex_count; const uint32_t* indices; uint32_t index_count; } biupiu_mesh_desc;
int biupiu_mesh_create(const biupiu_mesh_desc* desc,biupiu_mesh_id* out);
int biupiu_mesh_destroy(biupiu_mesh_id id);
int biupiu_mesh_validate(const biupiu_mesh_desc* desc);
#ifdef __cplusplus
}
#endif
#endif
