#include "../include/biupiu_native_shader.h"
#include <cstdlib>
#include <cstring>
#include <limits>

namespace {
constexpr uint32_t kSpirvMagic = 0x07230203u;
bool ok_text(const char* s) { return s && *s; }
}
extern "C" int biupiu_shader_validate_spirv(const uint32_t* words, uint32_t word_count) {
  if (!words || word_count < 5) return 1;
  if (words[0] != kSpirvMagic) return 2;
  const uint32_t version = words[1];
  const uint32_t major = (version >> 16u) & 0xffu;
  const uint32_t minor = (version >> 8u) & 0xffu;
  if (major != 1u || minor > 6u) return 3;
  if (words[3] == 0u) return 4;
  if (words[4] != 0u) return 5;
  uint32_t offset = 5;
  while (offset < word_count) {
    const uint32_t instruction = words[offset];
    const uint32_t word_count_inst = instruction & 0xffffu;
    if (word_count_inst < 1u || offset + word_count_inst > word_count) return 6;
    offset += word_count_inst;
  }
  return offset == word_count ? 0 : 7;
}
extern "C" int biupiu_shader_validate(const biupiu_shader_desc* d) {
  if (!d || !ok_text(d->entry) || !ok_text(d->target) || !d->source || d->source_size == 0) return 1;
  if (d->language < BIUPIU_SHADER_HLSL || d->language > BIUPIU_SHADER_SPIRV) return 2;
  if (d->language == BIUPIU_SHADER_SPIRV) {
    if (d->source_size % sizeof(uint32_t) != 0 || d->source_size / sizeof(uint32_t) > UINT32_MAX) return 3;
    return biupiu_shader_validate_spirv(static_cast<const uint32_t*>(d->source),
                                        static_cast<uint32_t>(d->source_size / sizeof(uint32_t)));
  }
  return 0;
}
extern "C" int biupiu_shader_compile(const biupiu_shader_desc* d, biupiu_spirv_binary* out) {
  if (!out) return 1;
  out->words = nullptr; out->word_count = 0;
  if (biupiu_shader_validate(d)) return 2;
  if (d->language != BIUPIU_SHADER_SPIRV) return 5;
  const uint32_t count = static_cast<uint32_t>(d->source_size / sizeof(uint32_t));
  auto* p = static_cast<uint32_t*>(std::malloc(d->source_size));
  if (!p) return 4;
  std::memcpy(p, d->source, d->source_size);
  out->words = p; out->word_count = count;
  return 0;
}
extern "C" void biupiu_shader_free(biupiu_spirv_binary* b) {
  if (!b) return;
  std::free(const_cast<uint32_t*>(b->words)); b->words = nullptr; b->word_count = 0;
}
