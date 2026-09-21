#include "../include/biupiu_visual_provider_adapter.h"
#include "../include/biupiu_visual_regression.h"
#include <cstring>
#include <string>

#if defined(BIUPIU_HAS_OPENUSD)
#include <pxr/usd/usd/stage.h>
#include <pxr/usd/usd/prim.h>
#include <pxr/usd/usdGeom/sphere.h>
#endif

namespace {
int fill_contract(biupiu_provider_adapter_info* out, const char* n, const char* v, uint64_t c) {
  if (!out) return 1;
  out->name=n; out->version=v; out->capabilities=c;
  out->state=BIUPIU_PROVIDER_ADAPTER_CONTRACT_ONLY;
  return 0;
}
#if defined(BIUPIU_HAS_OPENUSD)
int fill_usd_runtime(biupiu_provider_adapter_info* out) {
  if (!out) return 1;
  auto stage = pxr::UsdStage::CreateInMemory("biupiu_native_fixture");
  if (!stage) return 2;
  const pxr::SdfPath path("/Biupiu/VisualFixture");
  auto sphere = pxr::UsdGeomSphere::Define(stage, path);
  if (!sphere) return 3;
  sphere.CreateRadiusAttr().Set(1.0);
  const pxr::UsdPrim prim = stage->GetPrimAtPath(path);
  if (!prim || prim.GetTypeName() != pxr::TfToken("Sphere")) return 4;
  double radius = 0.0;
  if (!sphere.GetRadiusAttr().Get(&radius) || radius != 1.0) return 5;
  out->name="OpenUSD"; out->version="runtime-probed"; out->capabilities=1ULL;
  out->state=BIUPIU_PROVIDER_ADAPTER_HOST_READY;
  return 0;
}
#endif
}

extern "C" int biupiu_provider_adapter_usd(biupiu_provider_adapter_info* out) {
#if defined(BIUPIU_HAS_OPENUSD)
  return fill_usd_runtime(out);
#else
  return fill_contract(out, "OpenUSD", "external-provider", 1ULL);
#endif
}
extern "C" int biupiu_provider_adapter_otio(biupiu_provider_adapter_info* out) {
  return fill_contract(out, "OpenTimelineIO", "external-provider", 2ULL);
}
extern "C" int biupiu_provider_adapter_opensubdiv(biupiu_provider_adapter_info* out) {
  return fill_contract(out, "OpenSubdiv", "external-provider", 4ULL);
}
