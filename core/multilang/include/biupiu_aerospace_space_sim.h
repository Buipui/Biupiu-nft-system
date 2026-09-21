#ifndef BIUPIU_AEROSPACE_SPACE_SIM_H
#define BIUPIU_AEROSPACE_SPACE_SIM_H
#ifdef __cplusplus
extern "C" {
#endif
typedef struct { double mass_kg, thrust_n, drag_n, gravity_mps2; } BiupiuAeroInput;
typedef struct { double altitude_m, velocity_mps, acceleration_mps2; } BiupiuAeroState;
int biupiu_aerospace_step(const BiupiuAeroInput*, double altitude_m, double velocity_mps, double dt_s, BiupiuAeroState*);
#ifdef __cplusplus
}
#endif
#endif
