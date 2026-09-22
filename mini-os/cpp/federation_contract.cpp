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

 const biupiu_compute_unit floor_units[]={{3u,BIUPIU_COMPUTE_NPU,12u,1u},{4u,BIUPIU_COMPUTE_GPU,4u,1u}};
 const biupiu_mini_workload gpu_floor{9u,1u,BIUPIU_COMPUTE_GPU,BIUPIU_COMPUTE_GPU};
 assert(biupiu_mini_select_compute(floor_units,2u,&gpu_floor,&selected)==BIUPIU_MINI_OK);
 assert(selected==4u);

 const biupiu_mini_workload impossible_preference{10u,1u,BIUPIU_COMPUTE_CPU,BIUPIU_COMPUTE_GPU};
 assert(biupiu_mini_select_compute(floor_units,2u,&impossible_preference,&selected)==BIUPIU_MINI_OK);
 assert(selected==4u);
 return 0;
}
