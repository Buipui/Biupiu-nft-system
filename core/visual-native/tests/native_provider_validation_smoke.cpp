#include "../include/biupiu_visual_provider_validation.h"
#include <cassert>
#include <cstring>
int main() {
  const char input[]="provider-fixture-v1";
  const char output[]="canonical-output-v1";
  biupiu_visual_provider_validation v{};
  assert(biupiu_visual_provider_validate("OpenUSD",input,sizeof(input)-1,output,sizeof(output)-1,&v)==0);
  assert(v.input_hash!=0 && v.output_hash!=0);
  assert(v.deterministic_pass==1);
  assert(v.state==1 && v.runtime_probe==0);
  assert(biupiu_visual_provider_validate("UnknownProvider",input,sizeof(input)-1,output,sizeof(output)-1,&v)==1);
  return 0;
}
