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
set(BIUPIU_PROVIDER_TARGETS
  "OpenUSD;pxr::usd;BIUPIU_HAS_OPENUSD"
  "OpenTimelineIO;OpenTimelineIO::opentimelineio;BIUPIU_HAS_OTIO"
  "OpenSubdiv;OpenSubdiv::osdCPU;BIUPIU_HAS_OPENSUBDIV"
  "MaterialX;MaterialXCore;BIUPIU_HAS_MATERIALX"
  "OpenColorIO;OpenColorIO::OpenColorIO;BIUPIU_HAS_OCIO"
  "OpenImageIO;OpenImageIO::OpenImageIO;BIUPIU_HAS_OIIO"
  "OpenEXR;OpenEXR::OpenEXR;BIUPIU_HAS_OPENEXR"
)
foreach(spec IN LISTS BIUPIU_PROVIDER_TARGETS)
  string(REPLACE ";" "|" parts "${spec}")
  list(GET parts 0 package)
  list(GET parts 1 target)
  list(GET parts 2 macro)
  find_package(${package} CONFIG QUIET)
  if (TARGET ${target})
    target_link_libraries(biupiu_visual_native PRIVATE ${target})
    target_compile_definitions(biupiu_visual_native PRIVATE ${macro}=1)
  endif()
endforeach()

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
