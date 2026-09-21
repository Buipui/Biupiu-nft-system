#include "../include/biupiu_visual_provider_validation.h"
#include "../include/biupiu_visual_regression.h"
#include <cstring>
namespace {
int supported(const char* p) {
  return p && (!std::strcmp(p,"OpenUSD") || !std::strcmp(p,"OpenTimelineIO") ||
               !std::strcmp(p,"OpenSubdiv") || !std::strcmp(p,"MaterialX") ||
               !std::strcmp(p,"OpenColorIO") || !std::strcmp(p,"OpenImageIO") ||
               !std::strcmp(p,"OpenEXR"));
}
}
extern "C" int biupiu_visual_provider_validate(const char* provider,const void* input,uint64_t input_size,
                                                const void* canonical_output,uint64_t output_size,
                                                biupiu_visual_provider_validation* out) {
  if (!out || !supported(provider) || (!input && input_size) || (!canonical_output && output_size)) return 1;
  std::memset(out,0,sizeof(*out));
  out->provider=provider;
  out->version="host-evidence-required";
  out->discovered=0; out->linked=0; out->runtime_probe=0;
  out->input_hash=biupiu_visual_regression_hash_bytes(input,input_size);
  out->output_hash=biupiu_visual_regression_hash_bytes(canonical_output,output_size);
  out->deterministic_pass=(out->input_hash && out->output_hash)?1:0;
  out->state=1; // CONTRACT_ONLY until actual provider execution is evidenced.
  return 0;
}
