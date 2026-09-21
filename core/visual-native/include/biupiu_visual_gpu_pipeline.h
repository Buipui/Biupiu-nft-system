#ifndef BIUPIU_VISUAL_GPU_PIPELINE_H
#define BIUPIU_VISUAL_GPU_PIPELINE_H
#include <stdint.h>
#ifdef __cplusplus
extern "C" {
#endif
typedef uint64_t biupiu_pipeline_id;
typedef struct { uint64_t shader; uint64_t material; uint32_t topology; uint32_t format; } biupiu_pipeline_desc;
int biupiu_pipeline_create(const biupiu_pipeline_desc* desc,biupiu_pipeline_id* out);
int biupiu_pipeline_destroy(biupiu_pipeline_id id);
#ifdef __cplusplus
}
#endif
#endif
