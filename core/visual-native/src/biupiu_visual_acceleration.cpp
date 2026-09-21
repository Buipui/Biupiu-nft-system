#include "../include/biupiu_visual_acceleration.h"
#include <thread>
#if defined(__AVX512F__)
#define B_AVX512 1
#else
#define B_AVX512 0
#endif
#if defined(__AVX2__)
#define B_AVX2 1
#else
#define B_AVX2 0
#endif
#if defined(__ARM_NEON) || defined(__ARM_NEON__)
#define B_NEON 1
#else
#define B_NEON 0
#endif
extern "C" int biupiu_acceleration_probe(biupiu_acceleration_caps*out){if(!out)return 1;*out={uint8_t(B_AVX2||B_AVX512||B_NEON),uint8_t(B_AVX2),uint8_t(B_AVX512),uint8_t(B_NEON),0,0,0,0,(uint32_t)std::thread::hardware_concurrency(),0};return 0;}
