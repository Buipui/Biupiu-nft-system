#include "biupiu_benchmark_adapters.h"
#include <cstring>
static bool nonempty(const char* s){return s && *s;}
extern "C" int biupiu_benchmark_validate(const BiupiuBenchmarkModule* m){
 if(!m||!nonempty(m->capability)||!nonempty(m->native_target)||!nonempty(m->evidence_state)||!nonempty(m->provenance_ref)||!nonempty(m->licence_state)||!nonempty(m->source_version)) return -1;
 if(m->benchmark_id<BIUPIU_BENCHMARK_PALANTIR_ONTOLOGY||m->benchmark_id>BIUPIU_BENCHMARK_UNITY) return -2;
 if(m->harvest_class==BIUPIU_HARVEST_PROHIBITED) return -3; return 0;
}
extern "C" int biupiu_benchmark_classify(BiupiuBenchmarkId id,BiupiuHarvestClass c,BiupiuBenchmarkModule* out){
 if(!out)return -1; std::memset(out,0,sizeof(*out)); out->benchmark_id=id; out->harvest_class=c;
 out->evidence_state="SUPPORTED"; out->provenance_ref="research/BIUPIU-BENCHMARK-PROGRAM-HARVEST-GATE-2026-09-22.md"; out->licence_state="REVIEW_REQUIRED"; out->source_version="EXTERNAL_REFERENCE_VERSION_REQUIRED"; return 0;
}
