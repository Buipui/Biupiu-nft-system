#include "../include/biupiu_visual_provider_adapter.h"
#include "../include/biupiu_visual_regression.h"
#include <cstring>
#include <cstdio>
#if defined(BIUPIU_HAS_OPENUSD)
#include <pxr/usd/usd/stage.h>
#include <pxr/usd/sdf/path.h>
#endif
#include <string>
#if defined(BIUPIU_HAS_OTIO)
#include <opentimelineio/timeline.h>
#include <opentimelineio/track.h>
#include <opentimelineio/clip.h>
#include <opentime/rationalTime.h>
#include <opentime/timeRange.h>
#endif
#if defined(BIUPIU_HAS_OPENSUBDIV)
#include <opensubdiv/far/topologyRefinerFactory.h>
#endif
#if defined(BIUPIU_HAS_MATERIALX)
#include <MaterialXCore/Document.h>
#endif
#if defined(BIUPIU_HAS_OCIO)
#include <OpenColorIO/OpenColorIO.h>
#endif
#if defined(BIUPIU_HAS_OIIO)
#include <OpenImageIO/imageio.h>
#endif
#if defined(BIUPIU_HAS_OPENEXR)
#include <OpenEXR/ImfHeader.h>
#endif

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
undefined
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

extern "C" int biupiu_provider_adapter_run_usd_fixture(uint64_t* canonical_output_hash) {
  if (!canonical_output_hash) return 1;
#if defined(BIUPIU_HAS_OPENUSD)
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
  const std::string canonical =
      prim.GetPath().GetString() + "|" + prim.GetTypeName().GetString() + "|radius=1.0";
  *canonical_output_hash = biupiu_visual_regression_hash_bytes(canonical.data(), canonical.size());
  return *canonical_output_hash ? 0 : 6;
#else
  *canonical_output_hash = 0;
  return 10;
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
  int rc=fill_contract(out, "OpenTimelineIO", "external-provider", 2ULL);
#if defined(BIUPIU_HAS_OTIO)
  char buf[256]{}; uint32_t n=0;
  if (rc==0 && biupiu_provider_adapter_execute("OpenTimelineIO",buf,sizeof(buf),&n)==0) {
    out->version="runtime-probed"; out->state=BIUPIU_PROVIDER_ADAPTER_HOST_READY;
  }
#endif
  return rc;
}
extern "C" int biupiu_provider_adapter_opensubdiv(biupiu_provider_adapter_info* out) {
  int rc=fill_contract(out, "OpenSubdiv", "external-provider", 4ULL);
#if defined(BIUPIU_HAS_OPENSUBDIV)
  char buf[256]{}; uint32_t n=0;
  if (rc==0 && biupiu_provider_adapter_execute("OpenSubdiv",buf,sizeof(buf),&n)==0) {
    out->version="runtime-probed"; out->state=BIUPIU_PROVIDER_ADAPTER_HOST_READY;
  }
#endif
  return rc;
}


extern "C" int biupiu_provider_adapter_execute(const char* provider, char* output, uint32_t capacity, uint32_t* written) {
  if (!provider || !written) return 1;
  const char* canonical = nullptr;
#if defined(BIUPIU_HAS_OPENUSD)
  if (!std::strcmp(provider, "OpenUSD")) {
    auto stage = pxr::UsdStage::CreateInMemory();
    if (!stage) return 2;
    auto prim = stage->DefinePrim(pxr::SdfPath("/Biupiu"));
    if (!prim || !prim.IsValid()) return 3;
    static thread_local char buf[256];
    std::snprintf(buf, sizeof(buf), "OpenUSD|stage=in-memory|prim=%s|type=%s",
                  prim.GetPath().GetString().c_str(), prim.GetTypeName().GetString().c_str());
    canonical = buf;
  }
#endif
#if defined(BIUPIU_HAS_OTIO)
  if (!std::strcmp(provider, "OpenTimelineIO")) {
    OTIO_NS::SerializableObject::Retainer<OTIO_NS::Timeline> timeline(new OTIO_NS::Timeline("BiupiuFixture"));
    OTIO_NS::SerializableObject::Retainer<OTIO_NS::Track> track(new OTIO_NS::Track("Visual", OTIO_NS::TimeRange(OTIO_NS::RationalTime(0,24), OTIO_NS::RationalTime(48,24)), OTIO_NS::Track::Kind::video));
    OTIO_NS::SerializableObject::Retainer<OTIO_NS::Clip> clip(new OTIO_NS::Clip("BiupiuClip", nullptr, OTIO_NS::TimeRange(OTIO_NS::RationalTime(0,24), OTIO_NS::RationalTime(48,24))));
    track->append_child(clip);
    timeline->tracks()->append_child(track);
    if (clip->duration().value() != 48.0 || clip->duration().rate() != 24.0) return 10;
    canonical = "OpenTimelineIO|timeline=BiupiuFixture|track=Visual|clip=BiupiuClip|duration=48/24";
  }
#endif
#if defined(BIUPIU_HAS_OPENSUBDIV)
  if (!std::strcmp(provider, "OpenSubdiv")) {
    typedef OpenSubdiv::Far::TopologyDescriptor Descriptor;
    static int vertsPerFace[1]={4};
    static int indices[4]={0,1,2,3};
    Descriptor desc{};
    desc.numVertices=4; desc.numFaces=1; desc.numVertsPerFace=vertsPerFace; desc.vertIndicesPerFace=indices;
    auto* refiner=OpenSubdiv::Far::TopologyRefinerFactory<Descriptor>::Create(
      desc, OpenSubdiv::Far::TopologyRefinerFactory<Descriptor>::Options(
        OpenSubdiv::Sdc::SCHEME_CATMARK, OpenSubdiv::Sdc::Options()));
    if (!refiner) return 11;
    refiner->RefineUniform(OpenSubdiv::Far::TopologyRefiner::UniformOptions(1));
    const int total=refiner->GetNumVerticesTotal();
    delete refiner;
    if (total <= 4) return 12;
    static thread_local char buf[128];
    std::snprintf(buf,sizeof(buf),"OpenSubdiv|scheme=catmark|base_vertices=4|level1_total_vertices=%d",total);
    canonical=buf;
  }
#endif
#if defined(BIUPIU_HAS_MATERIALX)
  if (!std::strcmp(provider, "MaterialX")) {
    auto doc = MaterialX::createDocument();
    if (!doc) return 5;
    auto node = doc->addNode("constant", "BiupiuConstant", "color3");
    if (!node) return 6;
    canonical = "MaterialX|document=created|node=BiupiuConstant|type=color3";
  }
#endif
#if defined(BIUPIU_HAS_OCIO)
  if (!std::strcmp(provider, "OpenColorIO")) {
    auto config = OCIO::Config::Create();
    if (!config) return 7;
    canonical = "OpenColorIO|config=created";
  }
#endif
#if defined(BIUPIU_HAS_OIIO)
  if (!std::strcmp(provider, "OpenImageIO")) {
    OIIO::ImageSpec spec(2, 2, 4, OIIO::TypeDesc::FLOAT);
    if (spec.width != 2 || spec.height != 2 || spec.nchannels != 4) return 8;
    canonical = "OpenImageIO|spec=2x2x4|float";
  }
#endif
#if defined(BIUPIU_HAS_OPENEXR)
  if (!std::strcmp(provider, "OpenEXR")) {
    Imf::Header header(2, 2);
    if (header.width() != 2 || header.height() != 2) return 9;
    canonical = "OpenEXR|header=2x2";
  }
#endif
  if (!canonical) return 4;
  const uint32_t n=static_cast<uint32_t>(std::strlen(canonical));
  *written=n;
  if (!output || capacity<n+1) return 2;
  std::memcpy(output, canonical, n+1);
  return 0;
}
