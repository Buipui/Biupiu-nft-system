#include "../include/biupiu_visual_animation.h"
#include <algorithm>
#include <atomic>
#include <mutex>
#include <unordered_map>
#include <vector>
struct Track{biupiu_keyframe k;biupiu_interpolation i;}; static std::mutex m;static std::unordered_map<uint64_t,std::vector<Track>> tracks;static std::atomic<uint64_t> next_id{1};
extern "C" int biupiu_animation_create(biupiu_animation_id*out){if(!out)return 1;auto id=next_id++;std::lock_guard<std::mutex>l(m);tracks.emplace(id,std::vector<Track>{});*out=id;return 0;}
extern "C" int biupiu_animation_add_key(biupiu_animation_id id,const biupiu_keyframe*k,biupiu_interpolation i){if(!k)return 1;std::lock_guard<std::mutex>l(m);auto it=tracks.find(id);if(it==tracks.end())return 2;it->second.push_back({*k,i});std::sort(it->second.begin(),it->second.end(),[](const Track&a,const Track&b){return a.k.time<b.k.time;});return 0;}
extern "C" int biupiu_animation_sample(biupiu_animation_id id,double t,double*out){if(!out)return 1;std::lock_guard<std::mutex>l(m);auto it=tracks.find(id);if(it==tracks.end()||it->second.empty())return 2;auto&v=it->second;if(t<=v.front().k.time){std::copy(v.front().k.value,v.front().k.value+4,out);return 0;}if(t>=v.back().k.time){std::copy(v.back().k.value,v.back().k.value+4,out);return 0;}for(size_t j=1;j<v.size();++j)if(t<=v[j].k.time){auto&a=v[j-1],&b=v[j];if(a.i==BIUPIU_INTERP_STEP){std::copy(a.k.value,a.k.value+4,out);return 0;}double u=(t-a.k.time)/(b.k.time-a.k.time);for(int n=0;n<4;++n)out[n]=a.k.value[n]+(b.k.value[n]-a.k.value[n])*u;return 0;}return 3;}
extern "C" int biupiu_animation_destroy(biupiu_animation_id id){std::lock_guard<std::mutex>l(m);return tracks.erase(id)?0:2;}
