#include "../include/biupiu_visual_host_probe.h"
#include <thread>
#include <cstring>
#include <algorithm>
#if defined(BIUPIU_HAS_VULKAN)
#include <vulkan/vulkan.h>
#endif
#if defined(_WIN32) && defined(BIUPIU_HAS_DX12)
#include <d3d12.h>
#include <dxgi1_6.h>
#endif

namespace {
void provider_fill(biupiu_visual_provider_probe& p, const char* n, const char* v, bool d, bool l) {
  p.name=n; p.version=v; p.discovered=d?1:0; p.linked=l?1:0;
}
}

extern "C" int biupiu_visual_host_probe(biupiu_visual_host_caps* out) {
  if (!out) return 1;
  std::memset(out, 0, sizeof(*out));
  out->struct_size=sizeof(*out);
  const unsigned hc=std::thread::hardware_concurrency();
  out->cpu_threads=hc?hc:1;

#if defined(__AVX2__)
  out->avx2=1;
#endif
#if defined(__AVX512F__)
  out->avx512=1;
#endif
#if defined(__ARM_NEON) || defined(__ARM_NEON__)
  out->neon=1;
#endif

#if defined(BIUPIU_HAS_VULKAN)
  VkInstance instance=VK_NULL_HANDLE;
  VkApplicationInfo ai{VK_STRUCTURE_TYPE_APPLICATION_INFO,nullptr,"BiupiuVisualHostProbe",1,"BiupiuVisualNative",1,VK_API_VERSION_1_0};
  VkInstanceCreateInfo ci{VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO,nullptr,0,&ai,0,nullptr,0,nullptr};
  if (vkCreateInstance(&ci,nullptr,&instance)==VK_SUCCESS) {
    out->vulkan_loader=1;
    uint32_t api=VK_API_VERSION_1_0;
    auto enumerate_instance_version=reinterpret_cast<PFN_vkEnumerateInstanceVersion>(vkGetInstanceProcAddr(instance,"vkEnumerateInstanceVersion"));
    if (enumerate_instance_version) enumerate_instance_version(&api);
    out->vulkan_api_major=VK_VERSION_MAJOR(api);
    out->vulkan_api_minor=VK_VERSION_MINOR(api);
    uint32_t count=0;
    if (vkEnumeratePhysicalDevices(instance,&count,nullptr)==VK_SUCCESS && count) {
      out->vulkan_device=1;
      out->vulkan_device_count=count;
      VkPhysicalDevice* devs=new VkPhysicalDevice[count];
      if (vkEnumeratePhysicalDevices(instance,&count,devs)==VK_SUCCESS) {
        for (uint32_t i=0;i<count;i++) {
          VkPhysicalDeviceMemoryProperties mp{};
          vkGetPhysicalDeviceMemoryProperties(devs[i],&mp);
          for (uint32_t h=0;h<mp.memoryHeapCount;h++)
            if (mp.memoryHeaps[h].flags & VK_MEMORY_HEAP_DEVICE_LOCAL_BIT)
              out->vulkan_vram_bytes=std::max(out->vulkan_vram_bytes,static_cast<uint64_t>(mp.memoryHeaps[h].size));
        }
      }
      delete[] devs;
    }
    vkDestroyInstance(instance,nullptr);
  }
#endif

#if defined(_WIN32) && defined(BIUPIU_HAS_DX12)
  ID3D12Device* device=nullptr;
  if (SUCCEEDED(D3D12CreateDevice(nullptr,D3D_FEATURE_LEVEL_11_0,IID_PPV_ARGS(&device)))) {
    out->dx12_loader=1; out->dx12_device=1;
    D3D12_FEATURE_DATA_D3D12_OPTIONS5 opt5{};
    if (SUCCEEDED(device->CheckFeatureSupport(D3D12_FEATURE_D3D12_OPTIONS5,&opt5,sizeof(opt5))))
      out->dx12_ray_tracing = opt5.RaytracingTier != D3D12_RAYTRACING_TIER_NOT_SUPPORTED;
    device->Release();
  }
#endif
  return 0;
}

extern "C" int biupiu_visual_provider_probe_all(biupiu_visual_provider_probe* out,uint32_t capacity,uint32_t* written) {
  if (!written) return 1;
  const biupiu_visual_provider_probe all[] = {
#if defined(BIUPIU_HAS_OPENUSD)
    {"OpenUSD", "discovered", 1, 1},
#else
    {"OpenUSD", "not-found", 0, 0},
#endif
#if defined(BIUPIU_HAS_OTIO)
    {"OpenTimelineIO", "discovered", 1, 1},
#else
    {"OpenTimelineIO", "not-found", 0, 0},
#endif
#if defined(BIUPIU_HAS_OPENSUBDIV)
    {"OpenSubdiv", "discovered", 1, 1},
#else
    {"OpenSubdiv", "not-found", 0, 0},
#endif
#if defined(BIUPIU_HAS_MATERIALX)
    {"MaterialX", "discovered", 1, 1},
#else
    {"MaterialX", "not-found", 0, 0},
#endif
#if defined(BIUPIU_HAS_OCIO)
    {"OpenColorIO", "discovered", 1, 1},
#else
    {"OpenColorIO", "not-found", 0, 0},
#endif
#if defined(BIUPIU_HAS_OIIO)
    {"OpenImageIO", "discovered", 1, 1},
#else
    {"OpenImageIO", "not-found", 0, 0},
#endif
#if defined(BIUPIU_HAS_OPENEXR)
    {"OpenEXR", "discovered", 1, 1},
#else
    {"OpenEXR", "not-found", 0, 0},
#endif
  };
  const uint32_t n=static_cast<uint32_t>(sizeof(all)/sizeof(all[0]));
  const uint32_t copy=std::min(capacity,n);
  if (out && copy) std::memcpy(out,all,sizeof(all[0])*copy);
  *written=n;
  return capacity<n ? 2 : 0;
}
