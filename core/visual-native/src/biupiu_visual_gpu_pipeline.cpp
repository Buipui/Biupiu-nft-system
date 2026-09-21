#include "../include/biupiu_visual_gpu_pipeline.h"
#include <atomic>
#include <mutex>
#include <unordered_map>
static std::mutex m;static std::unordered_map<uint64_t,biupiu_pipeline_desc> pipes;static std::atomic<uint64_t> next_id{1};
extern "C" int biupiu_pipeline_create(const biupiu_pipeline_desc*d,biupiu_pipeline_id*out){if(!d||!out||!d->shader||!d->material)return 1;auto id=next_id++;std::lock_guard<std::mutex>l(m);pipes.emplace(id,*d);*out=id;return 0;}
extern "C" int biupiu_pipeline_destroy(biupiu_pipeline_id id){std::lock_guard<std::mutex>l(m);return pipes.erase(id)?0:2;}
