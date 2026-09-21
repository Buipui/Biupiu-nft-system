#ifndef BIUPIU_VISUAL_RENDER_GRAPH_H
#define BIUPIU_VISUAL_RENDER_GRAPH_H
#include <stdint.h>
#ifdef __cplusplus
extern "C" {
#endif
typedef uint64_t biupiu_render_graph_id;
typedef uint64_t biupiu_render_pass_id;
typedef enum { BIUPIU_PASS_CPU=1, BIUPIU_PASS_GPU=2, BIUPIU_PASS_IO=4 } biupiu_render_pass_kind;
typedef struct { biupiu_render_pass_kind kind; uint32_t priority; uint32_t resource_reads; uint32_t resource_writes; } biupiu_render_pass_desc;
typedef struct { uint32_t pass_count; uint32_t dependency_count; uint64_t execution_hash; } biupiu_render_graph_info;
int biupiu_render_graph_create(biupiu_render_graph_id* out);
int biupiu_render_graph_add_pass(biupiu_render_graph_id graph,const biupiu_render_pass_desc* desc,biupiu_render_pass_id* out);
int biupiu_render_graph_add_dependency(biupiu_render_graph_id graph,biupiu_render_pass_id before,biupiu_render_pass_id after);
int biupiu_render_graph_compile(biupiu_render_graph_id graph);
int biupiu_render_graph_execute(biupiu_render_graph_id graph,uint32_t frame_index,uint64_t* execution_hash);
int biupiu_render_graph_get_info(biupiu_render_graph_id graph,biupiu_render_graph_info* out);
int biupiu_render_graph_destroy(biupiu_render_graph_id graph);
#ifdef __cplusplus
}
#endif
#endif