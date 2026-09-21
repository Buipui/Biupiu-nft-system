#ifndef BIUPIU_MINI_FEDERATION_H
#define BIUPIU_MINI_FEDERATION_H
#include <stdint.h>
#include "biupiu_mini_os.h"
#ifdef __cplusplus
extern "C" {
#endif
typedef enum { BIUPIU_COMPUTE_CPU=0, BIUPIU_COMPUTE_VECTOR=1, BIUPIU_COMPUTE_GPU=2, BIUPIU_COMPUTE_NPU=3 } biupiu_compute_class;
typedef struct { uint32_t unit_id; uint32_t compute_class; uint32_t capacity; uint32_t available; } biupiu_compute_unit;
typedef struct { uint32_t workload_id; uint32_t cost; uint32_t preferred_class; uint32_t minimum_class; } biupiu_mini_workload;
biupiu_mini_status biupiu_mini_select_compute(const biupiu_compute_unit*, uint32_t, const biupiu_mini_workload*, uint32_t*);
#ifdef __cplusplus
}
#endif
#endif
