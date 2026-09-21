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
}
extern "C" int biupiu_visual_provider_validate(const char* provider,const void* input,uint64_t input_size,
                                                const void* canonical_output,uint64_t output_size,
                                                biupiu_visual_provider_validation* out) {
  if (!out || !supported(provider) || (!input && input_size) || (!canonical_output && output_size)) return 1;
  std::memset(out,0,sizeof(*out));
  out->provider=provider;
  out->version="host-evidence-required";
  out->input_hash=biupiu_visual_regression_hash_bytes(input,input_size);
  out->output_hash=biupiu_visual_regression_hash_bytes(canonical_output,output_size);
  out->deterministic_pass=(out->input_hash && out->output_hash)?1:0;
  char a[512]{}, b[512]{}; uint32_t an=0,bn=0;
  const int ra=biupiu_provider_adapter_execute(provider,a,sizeof(a),&an);
  const int rb=biupiu_provider_adapter_execute(provider,b,sizeof(b),&bn);
  out->discovered=1;
  out->linked=(ra==0 && rb==0)?1:0;
  out->runtime_probe=(ra==0 && rb==0)?1:0;
  if (ra==0 && rb==0 && an==bn) {
    const uint64_t first_hash=biupiu_visual_regression_hash_bytes(a,an);
    const uint64_t second_hash=biupiu_visual_regression_hash_bytes(b,bn);
    out->output_hash=first_hash;
    out->repeat_hash=second_hash;
    out->repeat_pass=(std::memcmp(a,b,an)==0 && first_hash!=0 && first_hash==second_hash)?1:0;
    out->deterministic_pass=out->repeat_pass;
    out->state=out->repeat_pass?3:2;
    out->version="runtime-probed";
  } else {
    out->state=1;
  }
  return 0;
}
