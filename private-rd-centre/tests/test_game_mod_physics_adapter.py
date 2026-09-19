from private_rd_centre.engine.game_mod_physics_adapter import (
    VehicleState, VehicleParams, simulate_step, compare_handling_profile
)


def test_straight_line_acceleration():
    s = VehicleState(1500, 0, 0.33)
    p = VehicleParams(2.7, 0.5, 1.2)
    r = simulate_step(s, p, 4500, 0, 0.1)
    assert abs(r.acceleration_mps2 - 3.0) < 1e-9


def test_cornering_target():
    s = VehicleState(1500, 20, 0.33, steering_rad=0.1)
    p = VehicleParams(2.7, 0.5, 1.2)
    r = simulate_step(s, p, 0, 0, 0.01)
    assert r.yaw_target_rps > 0
    assert r.lateral_acceleration_mps2 > 0


def test_profile_delta():
    base = VehicleParams(2.7, 0.5, 1.2)
    mod = VehicleParams(2.7, 0.48, 1.3, aero_downforce_n=500)
    d = compare_handling_profile(base, mod)
    assert d["cg_height_delta_m"] == -0.02
    assert d["max_lateral_g_delta"] == 0.1
