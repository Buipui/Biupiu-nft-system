#include "biupiu_farming_sim.h"
#include <cmath>
int biupiu_farming_step(const BiupiuFarmInput* in,double dt,BiupiuFarmState* out){
 if(!in||!out||!std::isfinite(dt)||dt<=0||!std::isfinite(in->soil_moisture)||!std::isfinite(in->rainfall_mm)||!std::isfinite(in->irrigation_mm)||!std::isfinite(in->evapotranspiration_mm)||in->infiltration_fraction<0||in->infiltration_fraction>1)return 1;
 out->soil_moisture=in->soil_moisture+(in->rainfall_mm+in->irrigation_mm)*in->infiltration_fraction-in->evapotranspiration_mm*dt;
 out->water_deficit_mm=out->soil_moisture<0?-out->soil_moisture:0;
 out->irrigation_demand_mm=out->water_deficit_mm; return 0;
}
