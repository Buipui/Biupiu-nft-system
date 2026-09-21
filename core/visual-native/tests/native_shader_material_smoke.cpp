#include "../include/biupiu_native_shader.h"
#include <cstdint>

static int req(bool v, int n) { return v ? 0 : n; }

int main() {
  const uint32_t valid[] = {0x07230203u, 0x00010600u, 0u, 16u, 0u};
  biupiu_shader_desc s{BIUPIU_SHADER_SPIRV, valid, sizeof(valid), "main", "spirv"};
  if (int r=req(biupiu_shader_validate(&s)==0,1)) return r;
  biupiu_spirv_binary b{};
  if (int r=req(biupiu_shader_compile(&s,&b)==0,2)) return r;
  if (int r=req(b.word_count==5 && b.words[0]==0x07230203u,3)) return r;
  biupiu_shader_free(&b);

  const uint32_t bad_magic[] = {0u,0x00010600u,0u,16u,0u};
  s.source=bad_magic; s.source_size=sizeof(bad_magic);
  if (int r=req(biupiu_shader_validate(&s)!=0,4)) return r;

  const char hlsl[] = "float4 main() : SV_Position { return 0; }";
  s.language=BIUPIU_SHADER_HLSL; s.source=hlsl; s.source_size=sizeof(hlsl)-1;
  if (int r=req(biupiu_shader_validate(&s)==0,5)) return r;
  return 0;
}
