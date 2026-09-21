#ifndef BIUPIU_VISUAL_SCENE_H
#define BIUPIU_VISUAL_SCENE_H
#include <stdint.h>
#ifdef __cplusplus
extern "C" {
#endif
typedef struct { double x,y,z; } biupiu_vec3;
typedef struct { double x,y,z,w; } biupiu_quat;
typedef struct { biupiu_vec3 position; biupiu_quat rotation; biupiu_vec3 scale; } biupiu_transform;
typedef uint64_t biupiu_scene_id; typedef uint64_t biupiu_node_id;
typedef struct { biupiu_scene_id scene; biupiu_node_id parent; biupiu_transform local; const char* name; } biupiu_scene_node_desc;
int biupiu_visual_scene_create(biupiu_scene_id* out_scene);
int biupiu_visual_scene_add_node(biupiu_scene_id scene,const biupiu_scene_node_desc* desc,biupiu_node_id* out_node);
int biupiu_visual_scene_destroy(biupiu_scene_id scene);
#ifdef __cplusplus
}
#endif
#endif
