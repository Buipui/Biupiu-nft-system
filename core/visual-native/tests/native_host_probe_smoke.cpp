#include "../include/biupiu_visual_host_probe.h"
#include <cassert>
#include <iostream>
int main() {
  biupiu_visual_host_caps caps{};
  assert(biupiu_visual_host_probe(&caps)==0);
  assert(caps.struct_size==sizeof(caps));
  assert(caps.cpu_threads>0);
  biupiu_visual_provider_probe providers[7]{};
  uint32_t written=0;
  assert(biupiu_visual_provider_probe_all(providers,7,&written)==0);
  assert(written==7);
  for (const auto& p: providers) {
    assert(p.name && *p.name);
    assert(p.discovered==p.linked);
  }
  std::cout << "native host/provider probe smoke: PASS\n";
  return 0;
}
