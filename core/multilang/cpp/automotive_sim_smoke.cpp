#include "biupiu_automotive_sim.h"
#include <cassert>
#include <cmath>

int main() {
    BiupiuVehicleInput in{
        1500.0, 0.31, 3000.0, 0.0, 0.30, 2.2, 1.225, 180.0
    };
    BiupiuVehicleState out{};
    assert(biupiu_vehicle_step(&in, 10.0, 0.1, &out) == 0);
    assert(std::isfinite(out.speed_mps));
    assert(out.speed_mps > 10.0);
    assert(out.acceleration_mps2 > 0.0);

    in.drive_force_n = 0.0;
    in.brake_force_n = 6000.0;
    assert(biupiu_vehicle_step(&in, out.speed_mps, 0.1, &out) == 0);
    assert(out.acceleration_mps2 < 0.0);
    assert(out.brake_deceleration_mps2 > 0.0);

    BiupiuVehicleInput bad = in;
    bad.mass_kg = 0.0;
    assert(biupiu_vehicle_step(&bad, 1.0, 0.1, &out) != 0);
    return 0;
}
