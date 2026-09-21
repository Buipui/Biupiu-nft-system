#include "../include/biupiu_visual_acceleration.h"
#include "../include/biupiu_visual_scheduler.h"
#include <cassert>
int main(){biupiu_acceleration_caps c{};assert(biupiu_acceleration_probe(&c)==0);assert(c.cpu_threads>0);assert(biupiu_scheduler_init(0)==0);assert(biupiu_scheduler_worker_count()>0);biupiu_task_desc d{BIUPIU_TASK_CPU,1,0};biupiu_task_id id=0;assert(biupiu_scheduler_submit(&d,&id)==0&&id>0);biupiu_scheduler_shutdown();assert(biupiu_scheduler_worker_count()==0);return 0;}
