#include "../include/biupiu_mini_federation.h"

static bool supports_class(uint32_t available, uint32_t minimum) {
    // Enum ordering is a capability floor: higher classes satisfy lower floors.
    return available >= minimum;
}

static bool better_candidate(const biupiu_compute_unit *candidate,
                             const biupiu_compute_unit *best) {
    if (!best) return true;
    if (candidate->capacity != best->capacity) return candidate->capacity > best->capacity;
    return candidate->unit_id < best->unit_id;
}

extern "C" biupiu_mini_status biupiu_mini_select_compute(
 const biupiu_compute_unit *units, uint32_t unit_count,
 const biupiu_mini_workload *workload, uint32_t *selected_unit_id) {
 if (!units || !workload || !selected_unit_id || unit_count==0u) return BIUPIU_MINI_INVALID_ARGUMENT;
 const biupiu_compute_unit *best=nullptr;
 const biupiu_compute_unit *preferred=nullptr;
 for(uint32_t i=0;i<unit_count;++i){
   const auto &u=units[i];
   if(!u.available || u.capacity==0u || !supports_class(u.compute_class, workload->minimum_class)) continue;
   if(u.compute_class==workload->preferred_class && better_candidate(&u, preferred)) preferred=&u;
   if(better_candidate(&u, best)) best=&u;
 }
 if(preferred) best=preferred;
 if(!best) return BIUPIU_MINI_NOT_READY;
 *selected_unit_id=best->unit_id;
 return BIUPIU_MINI_OK;
}
