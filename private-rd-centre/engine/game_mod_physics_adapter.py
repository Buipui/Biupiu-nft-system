"""Game-mod physics adapter v0.1.

Translates common vehicle-handling concepts into the Biupiu physics kernel.
This is a research/test adapter, not a game-specific replacement engine.
It deliberately uses documented, generic quantities rather than proprietary
game internals or extracted copyrighted assets.
"""

from dataclasses import dataclass
from math import isfinite


def finite(x: float) -> float:
    x = float(x)
    if not isfinite(x):
        raise ValueError("non-finite numeric input")
    return x


@dataclass
class VehicleState:
    mass_kg: float
    speed_mps: float
    wheel_radius_m: float
    yaw_rate_rps: float = 0.0
    steering_rad: float = 0.0


@dataclass
class VehicleParams:
    wheelbase_m: float
    cg_height_m: float
    max_lateral_g: float
    drivetrain_front_bias: float = 0.0
    aero_downforce_n: float = 0.0
    drag_n: float = 0.0


@dataclass
class VehicleResult:
    acceleration_mps2: float
    lateral_acceleration_mps2: float
    yaw_target_rps: float
    longitudinal_load_transfer_n: float
    traction_limit_n: float


def simulate_step(state: VehicleState, params: VehicleParams,
                  drive_force_n: float, brake_force_n: float,
                  dt_s: float) -> VehicleResult:
    values = [state.mass_kg, state.speed_mps, state.wheel_radius_m,
              params.wheelbase_m, params.cg_height_m, params.max_lateral_g,
              drive_force_n, brake_force_n, dt_s]
    for value in values:
        finite(value)
    if state.mass_kg <= 0 or state.wheel_radius_m <= 0:
        raise ValueError("invalid vehicle dimensions/mass")
    if params.wheelbase_m <= 0 or params.cg_height_m < 0 or params.max_lateral_g <= 0:
        raise ValueError("invalid vehicle parameters")
    if dt_s <= 0:
        raise ValueError("dt_s must be > 0")

    net_force = drive_force_n - brake_force_n - params.drag_n
    acceleration = net_force / state.mass_kg

    # Kinematic bicycle approximation for the preliminary game-mod bridge.
    yaw_target = 0.0
    if abs(state.speed_mps) > 1e-6:
        yaw_target = state.speed_mps * __import__("math").tan(state.steering_rad) / params.wheelbase_m
    lateral_accel = state.speed_mps * yaw_target

    total_weight = state.mass_kg * 9.80665
    traction_limit = total_weight * params.max_lateral_g + max(0.0, params.aero_downforce_n)

    # First-order longitudinal load-transfer estimate.
    load_transfer = state.mass_kg * acceleration * params.cg_height_m / params.wheelbase_m

    return VehicleResult(
        acceleration_mps2=acceleration,
        lateral_acceleration_mps2=lateral_accel,
        yaw_target_rps=yaw_target,
        longitudinal_load_transfer_n=load_transfer,
        traction_limit_n=traction_limit,
    )


def compare_handling_profile(base: VehicleParams, candidate: VehicleParams) -> dict:
    """Return neutral deltas for a modded handling profile."""
    return {
        "wheelbase_delta_m": candidate.wheelbase_m - base.wheelbase_m,
        "cg_height_delta_m": candidate.cg_height_m - base.cg_height_m,
        "max_lateral_g_delta": candidate.max_lateral_g - base.max_lateral_g,
        "front_bias_delta": candidate.drivetrain_front_bias - base.drivetrain_front_bias,
        "aero_downforce_delta_n": candidate.aero_downforce_n - base.aero_downforce_n,
        "drag_delta_n": candidate.drag_n - base.drag_n,
    }
