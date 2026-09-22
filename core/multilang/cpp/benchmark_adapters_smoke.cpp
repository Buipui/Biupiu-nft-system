#include "biupiu_benchmark_adapters.h"
#include <cassert>
int main(){BiupiuBenchmarkModule m{};assert(biupiu_benchmark_classify(BIUPIU_BENCHMARK_NVIDIA_OMNIVERSE,BIUPIU_HARVEST_ADAPTER,&m)==0);m.capability="digital-twin-simulation";m.native_target="core/multilang + world/adapters";assert(biupiu_benchmark_validate(&m)==0);m.harvest_class=BIUPIU_HARVEST_PROHIBITED;assert(biupiu_benchmark_validate(&m)!=0);return 0;}
