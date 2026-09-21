#include "biupiu_automotive_sim.h"
#include <cmath>

int biupiu_vehicle_step(const BiupiuVehicleInput* in,
                        double speed_mps,
                        double dt_s,
                        BiupiuVehicleState* out) {
    if (!in || !out || !std::isfinite(speed_mps) || !std::isfinite(dt_s) ||
        dt_s <= 0.0 || in->mass_kg <= 0.0 || in->wheel_radius_m <= 0.0 ||
        in->air_density_kg_m3 < 0.0 || in->frontal_area_m2 < 0.0 ||
        in->drag_coeff < 0.0 || in->rolling_resistance_n < 0.0) {
        return 1;
    }

    const double v = std::max(0.0, speed_mps);
    const double drag = 0.5 * in->air_density_kg_m3 *
                        in->drag_coeff * in->frontal_area_m2 * v * v;
    const double net = in->drive_force_n - in->brake_force_n -
                       drag - in->rolling_resistance_n;
    const double a = net / in->mass_kg;
    const double next_v = std::max(0.0, v + a * dt_s);

    out->speed_mps = next_v;
    out->acceleration_mps2 = a;
    out->longitudinal_force_n = net;
    out->brake_deceleration_mps2 =
        (in->brake_force_n + drag + in->rolling_resistance_n) / in->mass_kg;
    return 0;
}
