cmake_minimum_required(VERSION 3.20)
project(biupiu_visual_native LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

set(BIUPIU_VISUAL_NATIVE_SOURCES
  src/biupiu_visual_native.cpp
  src/biupiu_visual_scene.cpp
  src/biupiu_visual_provider.cpp
  src/biupiu_visual_manifest.cpp
  src/biupiu_native_render.cpp
  src/biupiu_native_shader.cpp
  src/biupiu_visual_material.cpp
  src/biupiu_visual_assets.cpp
  src/biupiu_visual_gpu_pipeline.cpp
  src/biupiu_visual_animation.cpp
  src/biupiu_visual_geometry.cpp
  src/biupiu_visual_subdivision.cpp
  src/biupiu_visual_scheduler.cpp
  src/biupiu_visual_acceleration.cpp
  src/biupiu_visual_provider_runtime.cpp
  src/biupiu_visual_regression.cpp
  src/biupiu_visual_provider_adapter.cpp
  src/biupiu_visual_host_probe.cpp
)

add_library(biupiu_visual_native SHARED ${BIUPIU_VISUAL_NATIVE_SOURCES})
target_include_directories(biupiu_visual_native PUBLIC include)
target_compile_features(biupiu_visual_native PUBLIC cxx_std_20)

# Optional host/provider discovery. The native core remains buildable without external SDKs.
find_package(Vulkan QUIET)
if (Vulkan_FOUND)
  target_link_libraries(biupiu_visual_native PRIVATE Vulkan::Vulkan)
  target_compile_definitions(biupiu_visual_native PRIVATE BIUPIU_HAS_VULKAN=1)
endif()

if (WIN32)
  find_library(BIUPIU_D3D12_LIBRARY NAMES d3d12)
  find_library(BIUPIU_DXGI_LIBRARY NAMES dxgi)
  if (BIUPIU_D3D12_LIBRARY AND BIUPIU_DXGI_LIBRARY)
    target_link_libraries(biupiu_visual_native PRIVATE ${BIUPIU_D3D12_LIBRARY} ${BIUPIU_DXGI_LIBRARY})
    target_compile_definitions(biupiu_visual_native PRIVATE BIUPIU_HAS_DX12=1)
  endif()
endif()

# Provider SDK discovery is deliberately target-based where packages export CMake targets.
# A discovered target is linked and promoted only by host/runtime evidence.
find_package(OpenUSD CONFIG QUIET)
if (TARGET pxr::usd)
  target_link_libraries(biupiu_visual_native PRIVATE pxr::usd)
  target_compile_definitions(biupiu_visual_native PRIVATE BIUPIU_HAS_OPENUSD=1)
endif()
find_package(OpenTimelineIO CONFIG QUIET)
if (TARGET OpenTimelineIO::opentimelineio)
  target_link_libraries(biupiu_visual_native PRIVATE OpenTimelineIO::opentimelineio)
  target_compile_definitions(biupiu_visual_native PRIVATE BIUPIU_HAS_OTIO=1)
endif()
find_package(OpenSubdiv CONFIG QUIET)
if (TARGET OpenSubdiv::osdCPU)
  target_link_libraries(biupiu_visual_native PRIVATE OpenSubdiv::osdCPU)
  target_compile_definitions(biupiu_visual_native PRIVATE BIUPIU_HAS_OPENSUBDIV=1)
endif()
find_package(MaterialX CONFIG QUIET)
if (TARGET MaterialXCore)
  target_link_libraries(biupiu_visual_native PRIVATE MaterialXCore)
  target_compile_definitions(biupiu_visual_native PRIVATE BIUPIU_HAS_MATERIALX=1)
endif()
find_package(OpenColorIO CONFIG QUIET)
if (TARGET OpenColorIO::OpenColorIO)
  target_link_libraries(biupiu_visual_native PRIVATE OpenColorIO::OpenColorIO)
  target_compile_definitions(biupiu_visual_native PRIVATE BIUPIU_HAS_OCIO=1)
endif()
find_package(OpenImageIO CONFIG QUIET)
if (TARGET OpenImageIO::OpenImageIO)
  target_link_libraries(biupiu_visual_native PRIVATE OpenImageIO::OpenImageIO)
  target_compile_definitions(biupiu_visual_native PRIVATE BIUPIU_HAS_OIIO=1)
endif()
find_package(OpenEXR CONFIG QUIET)
if (TARGET OpenEXR::OpenEXR)
  target_link_libraries(biupiu_visual_native PRIVATE OpenEXR::OpenEXR)
  target_compile_definitions(biupiu_visual_native PRIVATE BIUPIU_HAS_OPENEXR=1)
endif()

add_executable(biupiu_visual_native_smoke tests/native_visual_api_smoke.cpp)
target_link_libraries(biupiu_visual_native_smoke PRIVATE biupiu_visual_native)

add_executable(biupiu_native_render_smoke tests/native_render_smoke.cpp)
target_link_libraries(biupiu_native_render_smoke PRIVATE biupiu_visual_native)

add_executable(biupiu_native_shader_material_smoke tests/native_shader_material_smoke.cpp)
target_link_libraries(biupiu_native_shader_material_smoke PRIVATE biupiu_visual_native)

add_executable(biupiu_native_asset_pipeline_smoke tests/native_asset_pipeline_smoke.cpp)
target_link_libraries(biupiu_native_asset_pipeline_smoke PRIVATE biupiu_visual_native)

add_executable(biupiu_native_animation_geometry_smoke tests/native_animation_geometry_smoke.cpp)
target_link_libraries(biupiu_native_animation_geometry_smoke PRIVATE biupiu_visual_native)

add_executable(biupiu_native_acceleration_smoke tests/native_acceleration_smoke.cpp)
target_link_libraries(biupiu_native_acceleration_smoke PRIVATE biupiu_visual_native)

add_executable(biupiu_native_regression_provider_smoke tests/native_regression_provider_smoke.cpp)
target_link_libraries(biupiu_native_regression_provider_smoke PRIVATE biupiu_visual_native)

enable_testing()
add_test(NAME native_visual_api_smoke COMMAND biupiu_visual_native_smoke)
add_test(NAME native_render_smoke COMMAND biupiu_native_render_smoke)
add_test(NAME native_shader_material_smoke COMMAND biupiu_native_shader_material_smoke)
add_test(NAME native_asset_pipeline_smoke COMMAND biupiu_native_asset_pipeline_smoke)
add_test(NAME native_animation_geometry_smoke COMMAND biupiu_native_animation_geometry_smoke)
add_test(NAME native_acceleration_smoke COMMAND biupiu_native_acceleration_smoke)
add_test(NAME native_regression_provider_smoke COMMAND biupiu_native_regression_provider_smoke)
