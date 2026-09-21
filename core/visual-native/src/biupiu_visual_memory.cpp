#include "../include/biupiu_visual_memory.h"
#include <algorithm>
#include <cstddef>
#include <cstdint>
#include <cstdlib>
#include <limits>
#include <mutex>
#include <unordered_map>
#if defined(_MSC_VER)
#include <malloc.h>
#endif

namespace {
struct Allocation { biupiu_memory_info info{}; void* storage = nullptr; bool mapped = false; };
std::mutex g_mutex;
std::unordered_map<biupiu_memory_handle, Allocation> g_allocations;
uint64_t g_capacity = 0, g_reserved = 0, g_live = 0, g_peak = 0;
biupiu_memory_handle g_next = 1;

bool power_of_two(uint64_t v) { return v != 0 && (v & (v - 1)) == 0; }
void free_storage(void* p) {
#if defined(_MSC_VER)
  _aligned_free(p);
#else
  std::free(p);
#endif
}
}

extern "C" int biupiu_memory_system_init(uint64_t capacity_bytes) {
  std::lock_guard<std::mutex> lock(g_mutex);
  if (!g_allocations.empty()) return 2;
  if (capacity_bytes == 0) return 3;
  g_capacity = capacity_bytes; g_reserved = g_live = g_peak = 0; g_next = 1;
  return 0;
}

extern "C" void biupiu_memory_system_shutdown(void) {
  std::lock_guard<std::mutex> lock(g_mutex);
  for (auto& [_, a] : g_allocations) free_storage(a.storage);
  g_allocations.clear(); g_capacity = g_reserved = g_live = g_peak = 0; g_next = 1;
}

extern "C" int biupiu_memory_allocate(const biupiu_memory_request* request, biupiu_memory_handle* out_handle) {
  if (!request || !out_handle || request->size_bytes == 0 ||
      (request->alignment_bytes != 0 && !power_of_two(request->alignment_bytes)) ||
      (request->resource_type != BIUPIU_MEMORY_BUFFER && request->resource_type != BIUPIU_MEMORY_IMAGE) ||
      request->domain < BIUPIU_MEMORY_CPU || request->domain > BIUPIU_MEMORY_READBACK) return 3;

  std::lock_guard<std::mutex> lock(g_mutex);
  if (g_capacity == 0 || request->size_bytes > g_capacity - g_reserved) return 4;
  const uint64_t alignment = std::max<uint64_t>(request->alignment_bytes, alignof(std::max_align_t));
  if (!power_of_two(alignment) || alignment > static_cast<uint64_t>(std::numeric_limits<size_t>::max())) return 5;

  void* storage = nullptr;
#if defined(_MSC_VER)
  storage = _aligned_malloc(static_cast<size_t>(request->size_bytes), static_cast<size_t>(alignment));
  if (!storage) return 6;
#else
  if (posix_memalign(&storage, static_cast<size_t>(alignment), static_cast<size_t>(request->size_bytes)) != 0) return 6;
#endif

  biupiu_memory_handle handle = g_next++;
  if (handle == 0) handle = g_next++;
  Allocation a{};
  a.info.size_bytes = request->size_bytes; a.info.alignment_bytes = alignment;
  a.info.resource_type = static_cast<uint32_t>(request->resource_type);
  a.info.domain = static_cast<uint32_t>(request->domain); a.info.flags = request->flags; a.info.live = 1;
  a.storage = storage;
  g_allocations.emplace(handle, a);
  g_reserved += request->size_bytes; g_live += request->size_bytes;
  g_peak = std::max(g_peak, g_live); *out_handle = handle;
  return 0;
}

extern "C" int biupiu_memory_release(biupiu_memory_handle handle) {
  std::lock_guard<std::mutex> lock(g_mutex);
  auto it = g_allocations.find(handle);
  if (it == g_allocations.end() || !it->second.info.live) return 2;
  free_storage(it->second.storage);
  g_reserved -= it->second.info.size_bytes; g_live -= it->second.info.size_bytes;
  g_allocations.erase(it);
  return 0;
}

extern "C" int biupiu_memory_get_stats(biupiu_memory_stats* out) {
  if (!out) return 3;
  std::lock_guard<std::mutex> lock(g_mutex);
  out->capacity_bytes = g_capacity; out->reserved_bytes = g_reserved; out->live_bytes = g_live;
  out->allocation_count = static_cast<uint64_t>(g_allocations.size()); out->peak_live_bytes = g_peak;
  return 0;
}

extern "C" int biupiu_memory_get_info(biupiu_memory_handle handle, biupiu_memory_info* out) {
  if (!out) return 3;
  std::lock_guard<std::mutex> lock(g_mutex);
  auto it = g_allocations.find(handle);
  if (it == g_allocations.end()) return 2;
  *out = it->second.info; return 0;
}

extern "C" int biupiu_memory_validate(void) {
  std::lock_guard<std::mutex> lock(g_mutex);
  uint64_t sum = 0;
  for (const auto& [handle, a] : g_allocations) {
    if (handle == 0 || !a.info.live || !a.storage || a.info.size_bytes == 0 || !power_of_two(a.info.alignment_bytes)) return 2;
    if (a.info.size_bytes > std::numeric_limits<uint64_t>::max() - sum) return 3;
    sum += a.info.size_bytes;
  }
  if (sum != g_live || g_reserved != g_live || g_live > g_capacity) return 4;
  return 0;
}

extern "C" void* biupiu_memory_map(biupiu_memory_handle handle) {
  std::lock_guard<std::mutex> lock(g_mutex);
  auto it = g_allocations.find(handle);
  if (it == g_allocations.end() || it->second.mapped) return nullptr;
  it->second.mapped = true; return it->second.storage;
}

extern "C" int biupiu_memory_unmap(biupiu_memory_handle handle) {
  std::lock_guard<std::mutex> lock(g_mutex);
  auto it = g_allocations.find(handle);
  if (it == g_allocations.end() || !it->second.mapped) return 2;
  it->second.mapped = false; return 0;
}
