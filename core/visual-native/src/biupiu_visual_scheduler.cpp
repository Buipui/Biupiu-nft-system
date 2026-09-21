#include "../include/biupiu_visual_scheduler.h"
#include <algorithm>
#include <atomic>
#include <thread>
static std::atomic<uint32_t> workers{0},next_task{1};
extern "C" int biupiu_scheduler_init(uint32_t n){if(!n)n=std::max(1u,std::thread::hardware_concurrency());workers.store(n);return 0;}
extern "C" int biupiu_scheduler_submit(const biupiu_task_desc*d,biupiu_task_id*out){if(!d||!out||!workers.load())return 1;if(!d->kind)return 2;*out=next_task++;return 0;}
extern "C" uint32_t biupiu_scheduler_worker_count(void){return workers.load();}
extern "C" void biupiu_scheduler_shutdown(void){workers.store(0);}
