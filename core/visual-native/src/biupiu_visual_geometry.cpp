#include "../include/biupiu_visual_geometry.h"
#include <atomic>
#include <mutex>
#include <unordered_map>
struct Mesh{uint32_t vertices,indices;};static std::mutex m;static std::unordered_map<uint64_t,Mesh> meshes;static std::atomic<uint64_t> next_id{1};
extern "C" int biupiu_mesh_validate(const biupiu_mesh_desc*d){if(!d||!d->positions||!d->indices||!d->vertex_count||!d->index_count)return 1;if(d->index_count%3)return 2;for(uint32_t i=0;i<d->index_count;++i)if(d->indices[i]>=d->vertex_count)return 3;return 0;}
extern "C" int biupiu_mesh_create(const biupiu_mesh_desc*d,biupiu_mesh_id*out){if(!out)return 1;int e=biupiu_mesh_validate(d);if(e)return e;auto id=next_id++;std::lock_guard<std::mutex>l(m);meshes.emplace(id,Mesh{d->vertex_count,d->index_count});*out=id;return 0;}
extern "C" int biupiu_mesh_destroy(biupiu_mesh_id id){std::lock_guard<std::mutex>l(m);return meshes.erase(id)?0:2;}
