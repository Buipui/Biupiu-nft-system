#ifndef BIUPIU_FARMING_SIM_H
#define BIUPIU_FARMING_SIM_H
#ifdef __cplusplus
extern "C" {
#endif
typedef struct { double soil_moisture, rainfall_mm, irrigation_mm, evapotranspiration_mm, infiltration_fraction; } BiupiuFarmInput;
typedef struct { double soil_moisture, water_deficit_mm, irrigation_demand_mm; } BiupiuFarmState;
int biupiu_farming_step(const BiupiuFarmInput*, double dt_days, BiupiuFarmState*);
#ifdef __cplusplus
}
#endif
#endif
