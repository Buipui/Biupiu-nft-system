#ifndef BIUPIU_VISUAL_SCHEDULER_H
#define BIUPIU_VISUAL_SCHEDULER_H
#include <stdint.h>
#ifdef __cplusplus
extern "C" {
#endif
typedef uint64_t biupiu_task_id;
typedef enum { BIUPIU_TASK_CPU=1, BIUPIU_TASK_GPU=2, BIUPIU_TASK_IO=4, BIUPIU_TASK_ASYNC=8 } biupiu_task_kind;
typedef struct { biupiu_task_kind kind; uint32_t priority; uint32_t affinity; } biupiu_task_desc;
int biupiu_scheduler_init(uint32_t worker_count);
int biupiu_scheduler_submit(const biupiu_task_desc* desc,biupiu_task_id* out);
uint32_t biupiu_scheduler_worker_count(void);
void biupiu_scheduler_shutdown(void);
#ifdef __cplusplus
}
#endif
#endif
