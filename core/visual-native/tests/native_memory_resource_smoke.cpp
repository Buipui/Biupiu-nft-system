#include "../include/biupiu_visual_memory.h"
#include <cstdint>
#include <cstring>

static int require_true(bool v) { return v ? 0 : 1; }

int main() {
  if (require_true(biupiu_memory_system_init(4096) == 0)) return 1;
  biupiu_memory_request request{256, 64, BIUPIU_MEMORY_BUFFER, BIUPIU_MEMORY_CPU, 0};
  biupiu_memory_handle handle = 0;
  if (require_true(biupiu_memory_allocate(&request, &handle) == 0 && handle != 0)) return 2;

  biupiu_memory_info info{};
  if (require_true(biupiu_memory_get_info(handle, &info) == 0)) return 3;
  if (require_true(info.live == 1 && info.size_bytes == 256 && info.alignment_bytes == 64)) return 4;

  void* mapped = biupiu_memory_map(handle);
  if (require_true(mapped != nullptr)) return 5;
  std::memset(mapped, 0xA5, 256);
  if (require_true(biupiu_memory_unmap(handle) == 0)) return 6;
  if (require_true(biupiu_memory_validate() == 0)) return 7;

  biupiu_memory_stats stats{};
  if (require_true(biupiu_memory_get_stats(&stats) == 0)) return 8;
  if (require_true(stats.live_bytes == 256 && stats.allocation_count == 1 && stats.peak_live_bytes == 256)) return 9;

  biupiu_memory_request too_large = request;
  too_large.size_bytes = 4096;
  biupiu_memory_handle rejected = 0;
  if (require_true(biupiu_memory_allocate(&too_large, &rejected) != 0)) return 10;

  if (require_true(biupiu_memory_release(handle) == 0)) return 11;
  if (require_true(biupiu_memory_release(handle) != 0)) return 12;
  if (require_true(biupiu_memory_validate() == 0)) return 13;
  if (require_true(biupiu_memory_get_stats(&stats) == 0 && stats.live_bytes == 0 &&
                   stats.allocation_count == 0 && stats.peak_live_bytes == 256)) return 14;
  biupiu_memory_system_shutdown();
  return 0;
}
