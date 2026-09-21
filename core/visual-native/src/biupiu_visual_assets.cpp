#include "../include/biupiu_visual_assets.h"
#include <atomic>
#include <cmath>
#include <cstdint>
#include <cstring>
#include <limits>
#include <mutex>
#include <unordered_map>
namespace {
std::mutex g_mutex;
std::unordered_map<uint64_t,biupiu_image_info> g_images;
std::atomic<uint64_t> g_next_id{1};
uint64_t fnv1a(const uint8_t*p,size_t n){uint64_t h=1469598103934665603ull;for(size_t i=0;i<n;++i){h^=p[i];h*=1099511628211ull;}return h;}
}
extern "C" int biupiu_image_validate(const biupiu_image_desc*d){
 if(!d||!d->width||!d->height||!d->channels)return 1;
 if(d->channels>16||d->format==0)return 2;
 const uint64_t pixels=uint64_t(d->width)*d->height;
 if(pixels>uint64_t(std::numeric_limits<uint64_t>::max())/d->channels)return 3;
 return 0;
}
extern "C" int biupiu_image_create(const biupiu_image_desc*d,biupiu_image_id*out){
 if(!out)return 1;*out=0;int v=biupiu_image_validate(d);if(v)return v;
 const uint64_t bytes=uint64_t(d->width)*d->height*d->channels*(d->hdr?4u:1u);
 biupiu_image_info info{};info.id=g_next_id++;info.desc=*d;info.state=BIUPIU_ASSET_CPU_READY;info.byte_size=bytes;
 info.content_hash=fnv1a(reinterpret_cast<const uint8_t*>(d),sizeof(*d));
 std::lock_guard<std::mutex>l(g_mutex);g_images.emplace(info.id,info);*out=info.id;return 0;
}
extern "C" int biupiu_image_get(biupiu_image_id id,biupiu_image_info*out){
 if(!out||!id)return 1;std::lock_guard<std::mutex>l(g_mutex);auto it=g_images.find(id);if(it==g_images.end())return 2;*out=it->second;return 0;
}
extern "C" int biupiu_image_set_state(biupiu_image_id id,biupiu_asset_state state){
 if(state<BIUPIU_ASSET_UNLOADED||state>BIUPIU_ASSET_GPU_READY)return 1;std::lock_guard<std::mutex>l(g_mutex);auto it=g_images.find(id);if(it==g_images.end())return 2;
 if(state==BIUPIU_ASSET_UNLOADED)return 3;
 if(it->second.state==BIUPIU_ASSET_UNLOADED)return 4;
 it->second.state=state;return 0;
}
extern "C" int biupiu_image_destroy(biupiu_image_id id){std::lock_guard<std::mutex>l(g_mutex);return g_images.erase(id)?0:2;}
extern "C" int biupiu_color_transform_validate(const biupiu_color_transform*t){if(!t||!t->display||!*t->display)return 1;if(!std::isfinite(t->exposure)||!std::isfinite(t->gamma)||t->gamma<=0)return 2;return 0;}
