#ifndef BIUPIU_VISUAL_ANIMATION_H
#define BIUPIU_VISUAL_ANIMATION_H
#include <stdint.h>
#ifdef __cplusplus
extern "C" {
#endif
typedef uint64_t biupiu_animation_id;
typedef struct { double time; double value[4]; } biupiu_keyframe;
typedef enum { BIUPIU_INTERP_STEP=0, BIUPIU_INTERP_LINEAR=1 } biupiu_interpolation;
int biupiu_animation_create(biupiu_animation_id* out);
int biupiu_animation_add_key(biupiu_animation_id id,const biupiu_keyframe* key,biupiu_interpolation interpolation);
int biupiu_animation_sample(biupiu_animation_id id,double time,double out_value[4]);
int biupiu_animation_destroy(biupiu_animation_id id);
#ifdef __cplusplus
}
#endif
#endif
