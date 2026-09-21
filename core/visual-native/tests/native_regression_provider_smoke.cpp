#include "../include/biupiu_visual_provider_adapter.h"
#include "../include/biupiu_visual_regression.h"
#include <cassert>
#include <cstring>
int main() {
  biupiu_provider_adapter_info info{};
  assert(biupiu_provider_adapter_usd(&info)==0);
#if defined(BIUPIU_HAS_OPENUSD)
  assert(info.state==BIUPIU_PROVIDER_ADAPTER_HOST_READY);
  char a[256]{}, b[256]{}; uint32_t an=0,bn=0;
  assert(biupiu_provider_adapter_execute("OpenUSD",a,sizeof(a),&an)==0);
  assert(biupiu_provider_adapter_execute("OpenUSD",b,sizeof(b),&bn)==0);
  assert(an==bn && std::strcmp(a,b)==0);
  assert(biupiu_visual_regression_hash_bytes(a,an)==biupiu_visual_regression_hash_bytes(b,bn));
#else
  assert(info.state==BIUPIU_PROVIDER_ADAPTER_CONTRACT_ONLY);
#endif
  const char* providers[]={"MaterialX","OpenColorIO","OpenImageIO","OpenEXR"};
  for (const char* p: providers) {
    char out[256]{}; uint32_t n=0;
    const int rc=biupiu_provider_adapter_execute(p,out,sizeof(out),&n);
#if defined(BIUPIU_HAS_MATERIALX)
    if (std::strcmp(p,"MaterialX")==0) assert(rc==0 && n>0);
#endif
#if defined(BIUPIU_HAS_OCIO)
    if (std::strcmp(p,"OpenColorIO")==0) assert(rc==0 && n>0);
#endif
#if defined(BIUPIU_HAS_OIIO)
    if (std::strcmp(p,"OpenImageIO")==0) assert(rc==0 && n>0);
#endif
#if defined(BIUPIU_HAS_OPENEXR)
    if (std::strcmp(p,"OpenEXR")==0) assert(rc==0 && n>0);
#endif
  }
  assert(biupiu_provider_adapter_execute("Unknown",nullptr,0,nullptr)!=0);
  return 0;
}
