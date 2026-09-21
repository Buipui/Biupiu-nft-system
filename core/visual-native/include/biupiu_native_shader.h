#ifndef BIUPIU_NATIVE_SHADER_H
#define BIUPIU_NATIVE_SHADER_H
#include <stdint.h>
#ifdef __cplusplus
extern "C" {
#endif
typedef enum { BIUPIU_SHADER_HLSL=1, BIUPIU_SHADER_GLSL=2, BIUPIU_SHADER_SPIRV=3 } biupiu_shader_language;
typedef struct {
  biupiu_shader_language language;
  const void* source;
  uint64_t source_size;
  const char* entry;
  const char* target;
} biupiu_shader_desc;
typedef struct { const uint32_t* words; uint32_t word_count; } biupiu_spirv_binary;
int biupiu_shader_validate(const biupiu_shader_desc* desc);
int biupiu_shader_validate_spirv(const uint32_t* words, uint32_t word_count);
int biupiu_shader_compile(const biupiu_shader_desc* desc, biupiu_spirv_binary* out);
void biupiu_shader_free(biupiu_spirv_binary* binary);
#ifdef __cplusplus
}
#endif
#endif
