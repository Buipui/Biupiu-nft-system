#include "../include/biupiu_native_render.h"
#include <atomic>
#include <mutex>
#include <unordered_map>
struct Device{biupiu_gpu_backend backend;}; struct Target{biupiu_render_target_desc d;biupiu_render_device_id device;};
static std::mutex m;static std::unordered_map<uint64_t,Device> devices;static std::unordered_map<uint64_t,Target> targets;static std::atomic<uint64_t> next_id{1};
extern "C" int biupiu_render_probe(biupiu_gpu_backend b,biupiu_gpu_caps*out){if(!out)return 1;if(b!=BIUPIU_GPU_VULKAN&&b!=BIUPIU_GPU_DX12)return 2;*out={b,1,0,0,0,0,0};return 0;}
extern "C" int biupiu_render_create_device(biupiu_gpu_backend b,biupiu_render_device_id*out){if(!out)return 1;biupiu_gpu_caps c{};if(biupiu_render_probe(b,&c))return 2;auto id=next_id++;std::lock_guard<std::mutex>l(m);devices.emplace(id,Device{b});*out=id;return 0;}
extern "C" int biupiu_render_create_target(biupiu_render_device_id d,const biupiu_render_target_desc*desc,biupiu_render_target_id*out){if(!desc||!out||!desc->width||!desc->height)return 1;std::lock_guard<std::mutex>l(m);if(!devices.count(d))return 2;auto id=next_id++;targets.emplace(id,Target{*desc,d});*out=id;return 0;}
extern "C" int biupiu_render_begin(const biupiu_render_context*c){if(!c)return 1;std::lock_guard<std::mutex>l(m);return devices.count(c->device)&&targets.count(c->target)?0:2;}
extern "C" int biupiu_render_end(const biupiu_render_context*c){return biupiu_render_begin(c);}
extern "C" int biupiu_render_destroy_device(biupiu_render_device_id d){std::lock_guard<std::mutex>l(m);for(auto it=targets.begin();it!=targets.end();)if(it->second.device==d)it=targets.erase(it);else++it;return devices.erase(d)?0:2;}
