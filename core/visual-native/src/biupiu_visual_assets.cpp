#include "../include/biupiu_visual_assets.h"
#include <atomic>
#include <mutex>
#include <unordered_map>
static std::mutex m;static std::unordered_map<uint64_t,biupiu_image_desc> images;static std::atomic<uint64_t> next_id{1};
extern "C" int biupiu_image_create(const biupiu_image_desc*d,biupiu_image_id*out){if(!d||!out||!d->width||!d->height||!d->channels)return 1;if(d->channels>16)return 2;auto id=next_id++;std::lock_guard<std::mutex>l(m);images.emplace(id,*d);*out=id;return 0;}
extern "C" int biupiu_image_destroy(biupiu_image_id id){std::lock_guard<std::mutex>l(m);return images.erase(id)?0:2;}
extern "C" int biupiu_color_transform_validate(const biupiu_color_transform*t){if(!t||!t->display||!*t->display)return 1;if(t->gamma<=0)return 2;return 0;}
