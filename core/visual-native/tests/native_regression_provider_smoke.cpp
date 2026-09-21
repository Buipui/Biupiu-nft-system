#include "../include/biupiu_visual_regression.h"
#include "../include/biupiu_visual_provider_adapter.h"
#include <cassert>
#include <cstring>
int main() {
  const char input[]="biupiu-native-fixture-v1";
  const char output[]="frame-0001-deterministic";
  biupiu_visual_regression_record a{}, b{};
  assert(biupiu_visual_regression_make(9001,1,input,sizeof(input)-1,output,sizeof(output)-1,&a)==0);
  assert(biupiu_visual_regression_make(9001,1,input,sizeof(input)-1,output,sizeof(output)-1,&b)==0);
  assert(a.input_hash != 0 && a.output_hash != 0 && a.pass == 1);
  assert(biupiu_visual_regression_compare(&a,&b)==0);
  b.output_hash ^= 1ULL;
  assert(biupiu_visual_regression_compare(&a,&b)==2);
  biupiu_provider_adapter_info info{};
  assert(biupiu_provider_adapter_usd(&info)==0 && std::strcmp(info.name,"OpenUSD")==0);
  assert(info.state==BIUPIU_PROVIDER_ADAPTER_CONTRACT_ONLY);
  assert(biupiu_provider_adapter_otio(&info)==0 && std::strcmp(info.name,"OpenTimelineIO")==0);
  assert(biupiu_provider_adapter_opensubdiv(&info)==0 && std::strcmp(info.name,"OpenSubdiv")==0);
  return 0;
}
