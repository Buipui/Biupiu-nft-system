cmake_minimum_required(VERSION 3.22.1)
project(biupiu_native)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_library(biupiu_native SHARED
    src/main/cpp/scientific_android_bridge.cpp
    ../../../core/multilang/cpp/scientific_math_adapter.cpp
)

target_include_directories(biupiu_native PRIVATE
    ../../../core/multilang/include
)

target_compile_options(biupiu_native PRIVATE
    -Wall
    -Wextra
    -Werror
)
