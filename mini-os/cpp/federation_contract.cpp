#include "../include/biupiu_mini_federation.h"
#include <cassert>

int main(){
 const biupiu_compute_unit units[]={
   {1u,BIUPIU_COMPUTE_CPU,2u,1u},
   {2u,BIUPIU_COMPUTE_GPU,8u,1u},
   {3u,BIUPIU_COMPUTE_CPU,8u,1u}
 };
 uint32_t selected=0;

 const biupiu_mini_workload gpu{
   7u,10u,BIUPIU_COMPUTE_GPU,BIUPIU_COMPUTE_GPU
 };
 assert(biupiu_mini_select_compute(units,3u,&gpu,&selected)==BIUPIU_MINI_OK);
 assert(selected==2u);

 // Preferred GPU cannot override a hard CPU minimum.
 const biupiu_mini_workload cpu_min_gpu_preferred{
   9u,10u,BIUPIU_COMPUTE_GPU,BIUPIU_COMPUTE_CPU
 };
 assert(biupiu_mini_select_compute(units,3u,&cpu_min_gpu_preferred,&selected)==BIUPIU_MINI_OK);
 assert(selected==3u);

 const biupiu_mini_workload npu{
   8u,1u,BIUPIU_COMPUTE_NPU,BIUPIU_COMPUTE_NPU
 };
 assert(biupiu_mini_select_compute(units,3u,&npu,&selected)==BIUPIU_MINI_NOT_READY);

 return 0;
}
