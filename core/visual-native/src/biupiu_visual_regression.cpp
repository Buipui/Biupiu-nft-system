#include "../include/biupiu_visual_regression.h"
#include <cstddef>
#include <cstdint>
namespace {
uint64_t fnv1a(const uint8_t* p, uint64_t n) {
  uint64_t h = 1469598103934665603ULL;
  for (uint64_t i = 0; i < n; ++i) { h ^= p[i]; h *= 1099511628211ULL; }
  return h;
}
uint64_t mix(uint64_t a, uint64_t b) {
  a ^= b + 0x9e3779b97f4a7c15ULL + (a << 6) + (a >> 2);
  return a;
}
}
extern "C" uint64_t biupiu_visual_regression_hash_bytes(const void* data, uint64_t size) {
  if (!data && size) return 0;
  return fnv1a(static_cast<const uint8_t*>(data), size);
}
extern "C" int biupiu_visual_regression_make(
    uint64_t fixture_id, uint32_t frame,
    const void* input, uint64_t input_size,
    const void* output, uint64_t output_size,
    biupiu_visual_regression_record* out) {
  if (!out || (!input && input_size) || (!output && output_size)) return 1;
  out->fixture_id = fixture_id;
  out->frame = frame;
  out->input_hash = biupiu_visual_regression_hash_bytes(input, input_size);
  out->output_hash = biupiu_visual_regression_hash_bytes(output, output_size);
  out->pass = (mix(out->input_hash, out->output_hash) != 0) ? 1U : 0U;
  return 0;
}
extern "C" int biupiu_visual_regression_compare(
    const biupiu_visual_regression_record* expected,
    const biupiu_visual_regression_record* actual) {
  if (!expected || !actual) return 1;
  return (expected->fixture_id == actual->fixture_id &&
          expected->frame == actual->frame &&
          expected->input_hash == actual->input_hash &&
          expected->output_hash == actual->output_hash) ? 0 : 2;
}
