#include "../include/biupiu_mini_federation.h"
extern "C" biupiu_mini_status biupiu_mini_select_compute(
 const biupiu_compute_unit *units, uint32_t unit_count,
 const biupiu_mini_workload *workload, uint32_t *selected_unit_id) {
 if (!units || !workload || !selected_unit_id || unit_count==0u) return BIUPIU_MINI_INVALID_ARGUMENT;
 const biupiu_compute_unit *best=nullptr;
 for(uint32_t i=0;i<unit_count;++i){
   const auto &u=units[i];
   if(!u.available || u.capacity==0u || u.compute_class != workload->minimum_class) continue;
   if(u.compute_class==workload->preferred_class){ best=&u; break; }
   if(!best || u.capacity>best->capacity) best=&u;
 }
 if(!best) return BIUPIU_MINI_NOT_READY;
 *selected_unit_id=best->unit_id;
 return BIUPIU_MINI_OK;
}
