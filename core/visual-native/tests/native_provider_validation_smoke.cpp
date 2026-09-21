#include "../include/biupiu_visual_provider_validation.h"
#include "../include/biupiu_visual_provider_adapter.h"
#include <cassert>
#include <cstring>

int main() {
  const char input[]="provider-fixture-v1";
  const char output[]="canonical-output-v1";
  biupiu_visual_provider_validation v{};
  assert(biupiu_visual_provider_validate("OpenUSD",input,sizeof(input)-1,output,sizeof(output)-1,&v)==0);
  assert(v.input_hash!=0 && v.output_hash!=0);
  assert(v.deterministic_pass==1);
  assert(v.discovered==1);
#if defined(BIUPIU_HAS_OPENUSD)
  assert(v.linked==1 && v.runtime_probe==1 && v.repeat_pass==1 && v.state==3);
#else
  assert(v.state==1 && v.runtime_probe==0);
#endif
  assert(biupiu_visual_provider_validate("UnknownProvider",input,sizeof(input)-1,output,sizeof(output)-1,&v)==1);

  uint64_t usd_a=0, usd_b=0;
  const int ra=biupiu_provider_adapter_run_usd_fixture(&usd_a);
  const int rb=biupiu_provider_adapter_run_usd_fixture(&usd_b);
#if defined(BIUPIU_HAS_OPENUSD)
  assert(ra==0 && rb==0);
  assert(usd_a!=0 && usd_a==usd_b);
  biupiu_provider_adapter_info info{};
  assert(biupiu_provider_adapter_usd(&info)==0);
  assert(info.state==BIUPIU_PROVIDER_ADAPTER_HOST_READY);
#else
  assert(ra==10 && rb==10);
  assert(usd_a==0 && usd_b==0);
#endif
  return 0;
}
