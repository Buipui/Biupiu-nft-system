#pragma once
#include <stdint.h>
#ifdef __cplusplus
extern "C" {
#endif

typedef enum {
 BIUPIU_BENCHMARK_PALANTIR_ONTOLOGY=1, BIUPIU_BENCHMARK_SIEMENS_XCELERATOR=2,
 BIUPIU_BENCHMARK_DASSAULT_3DEXPERIENCE=3, BIUPIU_BENCHMARK_NVIDIA_OMNIVERSE=4,
 BIUPIU_BENCHMARK_PTC_THINGWORX=5, BIUPIU_BENCHMARK_BENTLEY_ITWIN=6,
 BIUPIU_BENCHMARK_UNREAL_ENGINE=7, BIUPIU_BENCHMARK_UNITY=8
} BiupiuBenchmarkId;

typedef enum { BIUPIU_HARVEST_REFERENCE=1, BIUPIU_HARVEST_PATTERN=2, BIUPIU_HARVEST_ADAPTER=3, BIUPIU_HARVEST_DEPENDENCY=4, BIUPIU_HARVEST_PROHIBITED=5 } BiupiuHarvestClass;

typedef struct { BiupiuBenchmarkId benchmark_id; BiupiuHarvestClass harvest_class; const char* capability; const char* native_target; const char* evidence_state; const char* provenance_ref; } BiupiuBenchmarkModule;
int biupiu_benchmark_validate(const BiupiuBenchmarkModule* module);
int biupiu_benchmark_classify(BiupiuBenchmarkId benchmark_id, BiupiuHarvestClass harvest_class, BiupiuBenchmarkModule* out);
#ifdef __cplusplus
}
#endif
