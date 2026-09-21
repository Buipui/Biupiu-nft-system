#include "../include/biupiu_visual_provider_adapter.h"
#include <cstring>
namespace {
int fill(biupiu_provider_adapter_info* out, const char* n, const char* v, uint64_t c) {
  if (!out) return 1;
  out->name=n; out->version=v; out->capabilities=c;
  out->state=BIUPIU_PROVIDER_ADAPTER_CONTRACT_ONLY;
  return 0;
}
}
extern "C" int biupiu_provider_adapter_usd(biupiu_provider_adapter_info* out) {
  return fill(out, "OpenUSD", "external-provider", 1ULL);
}
extern "C" int biupiu_provider_adapter_otio(biupiu_provider_adapter_info* out) {
  return fill(out, "OpenTimelineIO", "external-provider", 2ULL);
}
extern "C" int biupiu_provider_adapter_opensubdiv(biupiu_provider_adapter_info* out) {
  return fill(out, "OpenSubdiv", "external-provider", 4ULL);
}
