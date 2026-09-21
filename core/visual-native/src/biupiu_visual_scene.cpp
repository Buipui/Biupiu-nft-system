#include "../include/biupiu_visual_scene.h"
#include <atomic>
#include <mutex>
#include <unordered_map>
struct Scene { std::unordered_map<biupiu_node_id,biupiu_scene_node_desc> nodes; };
static std::mutex m; static std::unordered_map<biupiu_scene_id,Scene> scenes; static std::atomic<uint64_t> next_scene{1},next_node{1};
extern "C" int biupiu_visual_scene_create(biupiu_scene_id* out){if(!out)return 1;auto id=next_scene++;{std::lock_guard<std::mutex>l(m);scenes.emplace(id,Scene{});}*out=id;return 0;}
extern "C" int biupiu_visual_scene_add_node(biupiu_scene_id s,const biupiu_scene_node_desc*d,biupiu_node_id*out){if(!d||!out)return 1;std::lock_guard<std::mutex>l(m);auto it=scenes.find(s);if(it==scenes.end())return 2;auto id=next_node++;it->second.nodes.emplace(id,*d);*out=id;return 0;}
extern "C" int biupiu_visual_scene_destroy(biupiu_scene_id s){std::lock_guard<std::mutex>l(m);return scenes.erase(s)?0:2;}
