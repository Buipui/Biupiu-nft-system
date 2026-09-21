#ifndef BIUPIU_AUTOMOTIVE_SIM_H
#define BIUPIU_AUTOMOTIVE_SIM_H

#ifdef __cplusplus
extern "C" {
#endif

typedef struct {
    double mass_kg;
    double wheel_radius_m;
    double drive_force_n;
    double brake_force_n;
    double drag_coeff;
    double frontal_area_m2;
    double air_density_kg_m3;
    double rolling_resistance_n;
} BiupiuVehicleInput;

typedef struct {
    double speed_mps;
    double acceleration_mps2;
    double longitudinal_force_n;
    double brake_deceleration_mps2;
} BiupiuVehicleState;

/* Deterministic, dependency-free longitudinal vehicle step. */
int biupiu_vehicle_step(const BiupiuVehicleInput* input,
                        double speed_mps,
                        double dt_s,
                        BiupiuVehicleState* output);

#ifdef __cplusplus
}
#endif

#endif
