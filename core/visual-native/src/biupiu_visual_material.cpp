#include "../include/biupiu_visual_material.h"
#include <atomic>
#include <mutex>
#include <unordered_map>
static std::mutex m;static std::unordered_map<uint64_t,biupiu_material_desc> mats;static std::atomic<uint64_t> next_id{1};
extern "C" int biupiu_material_create(const biupiu_material_desc*d,biupiu_material_id*out){if(!d||!out)return 1;if(d->roughness<0||d->roughness>1||d->metallic<0||d->metallic>1||d->opacity<0||d->opacity>1)return 2;auto id=next_id++;std::lock_guard<std::mutex>l(m);mats.emplace(id,*d);*out=id;return 0;}
extern "C" int biupiu_material_destroy(biupiu_material_id id){std::lock_guard<std::mutex>l(m);return mats.erase(id)?0:2;}
