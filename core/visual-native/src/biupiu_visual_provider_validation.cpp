#include "../include/biupiu_visual_provider_validation.h"
#include "../include/biupiu_visual_regression.h"
#include "../include/biupiu_visual_provider_adapter.h"
#include <cstring>

namespace {
int supported(const char* p) {
  return p && (!std::strcmp(p,"OpenUSD") || !std::strcmp(p,"OpenTimelineIO") ||
               !std::strcmp(p,"OpenSubdiv") || !std::strcmp(p,"MaterialX") ||
               !std::strcmp(p,"OpenColorIO") || !std::strcmp(p,"OpenImageIO") ||
               !std::strcmp(p,"OpenEXR"));
}
bool linked(const char* p) {
#if defined(BIUPIU_HAS_OPENUSD)
  if (!std::strcmp(p,"OpenUSD")) return true;
#endif
#if defined(BIUPIU_HAS_OTIO)
  if (!std::strcmp(p,"OpenTimelineIO")) return true;
#endif
#if defined(BIUPIU_HAS_OPENSUBDIV)
  if (!std::strcmp(p,"OpenSubdiv")) return true;
#endif
#if defined(BIUPIU_HAS_MATERIALX)
  if (!std::strcmp(p,"MaterialX")) return true;
#endif
#if defined(BIUPIU_HAS_OCIO)
  if (!std::strcmp(p,"OpenColorIO")) return true;
#endif
#if defined(BIUPIU_HAS_OIIO)
  if (!std::strcmp(p,"OpenImageIO")) return true;
#endif
#if defined(BIUPIU_HAS_OPENEXR)
  if (!std::strcmp(p,"OpenEXR")) return true;
#endif
  return false;
}
}

extern "C" int biupiu_visual_provider_validate(const char* provider,const void* input,uint64_t input_size,
                                                const void* canonical_output,uint64_t output_size,
                                                biupiu_visual_provider_validation* out) {
  if (!out || !supported(provider) || (!input && input_size) || (!canonical_output && output_size)) return 1;
  std::memset(out,0,sizeof(*out));
  out->provider=provider;
  out->version=linked(provider) ? "linked-sdk" : "host-evidence-required";
  out->discovered=linked(provider) ? 1 : 0;
  out->linked=linked(provider) ? 1 : 0;
  out->input_hash=biupiu_visual_regression_hash_bytes(input,input_size);
  out->output_hash=biupiu_visual_regression_hash_bytes(canonical_output,output_size);
  out->runtime_probe=0;
  out->deterministic_pass=(out->input_hash && out->output_hash)?1:0;
  out->state=1;
  if (!linked(provider)) return 0;

  char runtime_a[512]{}, runtime_b[512]{};
  uint32_t a=0,b=0;
  if (biupiu_provider_adapter_execute(provider,runtime_a,sizeof(runtime_a),&a)==0 &&
      biupiu_provider_adapter_execute(provider,runtime_b,sizeof(runtime_b),&b)==0 &&
      a==b && a>0 && std::memcmp(runtime_a,runtime_b,a)==0) {
    const uint64_t ha=biupiu_visual_regression_hash_bytes(runtime_a,a);
    const uint64_t hb=biupiu_visual_regression_hash_bytes(runtime_b,b);
    out->runtime_probe=1;
    out->deterministic_pass=(ha!=0 && ha==hb)?1:0;
    out->state=out->deterministic_pass ? 2 : 1;
    out->version="runtime-probed";
  }
  return 0;
}
