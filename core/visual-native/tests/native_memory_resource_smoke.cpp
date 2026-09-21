#include "../include/biupiu_visual_memory.h"
#include <cassert>
#include <cstdint>
#include <cstring>

int main() {
  assert(biupiu_memory_system_init(4096) == 0);
  biupiu_memory_request request{256, 64, BIUPIU_MEMORY_BUFFER, BIUPIU_MEMORY_CPU, 0};
  biupiu_memory_handle handle = 0;
  assert(biupiu_memory_allocate(&request, &handle) == 0 && handle != 0);

  biupiu_memory_info info{};
  assert(biupiu_memory_get_info(handle, &info) == 0);
  assert(info.live == 1 && info.size_bytes == 256 && info.alignment_bytes == 64);

  void* mapped = biupiu_memory_map(handle);
  assert(mapped != nullptr);
  std::memset(mapped, 0xA5, 256);
  assert(biupiu_memory_unmap(handle) == 0);
  assert(biupiu_memory_validate() == 0);

  biupiu_memory_stats stats{};
  assert(biupiu_memory_get_stats(&stats) == 0);
  assert(stats.live_bytes == 256 && stats.allocation_count == 1 && stats.peak_live_bytes == 256);

  biupiu_memory_request too_large = request; too_large.size_bytes = 4096;
  biupiu_memory_handle rejected = 0;
  assert(biupiu_memory_allocate(&too_large, &rejected) != 0);

  assert(biupiu_memory_release(handle) == 0);
  assert(biupiu_memory_release(handle) != 0);
  assert(biupiu_memory_validate() == 0);
  assert(biupiu_memory_get_stats(&stats) == 0 && stats.live_bytes == 0 && stats.allocation_count == 0 && stats.peak_live_bytes == 256);
  biupiu_memory_system_shutdown();
  return 0;
}
