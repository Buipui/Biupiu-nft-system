#include "../include/biupiu_mini_federation.h"
#include <cassert>
int main(){
 const biupiu_compute_unit units[]={{1u,BIUPIU_COMPUTE_CPU,2u,1u},{2u,BIUPIU_COMPUTE_GPU,8u,1u}};
 const biupiu_mini_workload gpu{7u,10u,BIUPIU_COMPUTE_GPU,BIUPIU_COMPUTE_GPU};
 uint32_t selected=0;
 assert(biupiu_mini_select_compute(units,2u,&gpu,&selected)==BIUPIU_MINI_OK);
 assert(selected==2u);
 const biupiu_mini_workload npu{8u,1u,BIUPIU_COMPUTE_NPU,BIUPIU_COMPUTE_NPU};
 assert(biupiu_mini_select_compute(units,2u,&npu,&selected)==BIUPIU_MINI_NOT_READY);
 return 0;
}
