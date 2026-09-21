#ifndef BIUPIU_MARINE_SIM_H
#define BIUPIU_MARINE_SIM_H
#ifdef __cplusplus
extern "C" {
#endif
typedef struct { double mass_kg, surge_force_n, sway_force_n, yaw_moment_nm, water_density_kg_m3, drag_coeff; } BiupiuMarineInput;
typedef struct { double surge_mps, sway_mps, yaw_rate_rps, surge_accel_mps2; } BiupiuMarineState;
int biupiu_marine_step(const BiupiuMarineInput*, double surge_mps, double sway_mps, double yaw_rate_rps, double dt_s, BiupiuMarineState*);
#ifdef __cplusplus
}
#endif
#endif
