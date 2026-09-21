#include "../include/biupiu_visual_material.h"
#include <atomic>
#include <cmath>
#include <cstdint>
#include <cstring>
#include <mutex>
#include <unordered_map>

namespace {
std::mutex g_mutex;
std::unordered_map<uint64_t, biupiu_material_info> g_materials;
std::atomic<uint64_t> g_next_id{1};

uint64_t fnv1a(const uint8_t* p, size_t n) {
  uint64_t h = 1469598103934665603ull;
  for (size_t i=0;i<n;++i) { h ^= p[i]; h *= 1099511628211ull; }
  return h;
}
bool finite(float v) { return std::isfinite(v); }
}
extern "C" int biupiu_material_validate(const biupiu_material_desc* d) {
  if (!d) return 1;
  for (float v : d->base_color) if (!finite(v) || v < 0.0f || v > 1.0f) return 2;
  for (float v : d->emission) if (!finite(v) || v < 0.0f) return 3;
  if (!finite(d->metallic) || d->metallic < 0.0f || d->metallic > 1.0f) return 4;
  if (!finite(d->roughness) || d->roughness < 0.0f || d->roughness > 1.0f) return 5;
  if (!finite(d->opacity) || d->opacity < 0.0f || d->opacity > 1.0f) return 6;
  return 0;
}
extern "C" int biupiu_material_create(const biupiu_material_desc* d, biupiu_material_id* out) {
  if (!out) return 1;
  *out = 0;
  int v = biupiu_material_validate(d);
  if (v) return v;
  biupiu_material_info info{};
  info.id = g_next_id++;
  info.desc = *d;
  info.canonical_hash = fnv1a(reinterpret_cast<const uint8_t*>(&info.desc), sizeof(info.desc));
  std::lock_guard<std::mutex> lock(g_mutex);
  g_materials.emplace(info.id, info);
  *out = info.id;
  return 0;
}
extern "C" int biupiu_material_get(biupiu_material_id id, biupiu_material_info* out) {
  if (!out || id == 0) return 1;
  std::lock_guard<std::mutex> lock(g_mutex);
  auto it = g_materials.find(id);
  if (it == g_materials.end()) return 2;
  *out = it->second;
  return 0;
}
extern "C" int biupiu_material_destroy(biupiu_material_id id) {
  std::lock_guard<std::mutex> lock(g_mutex);
  return g_materials.erase(id) ? 0 : 2;
}
