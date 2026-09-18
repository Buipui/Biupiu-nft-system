"""Biupiu independent propulsion comparison simulator v0.1.

Separates diesel-electric and Jaguar-style microturbine-electric architectures
so later comparisons use identical vehicle assumptions.

Conceptual model only; not a controller, safety model, CFD model, or certification tool.
"""
from dataclasses import dataclass

@dataclass
class Vehicle:
    mass_kg: float = 1450.0
    cd: float = 0.30
    area_m2: float = 1.90
    rolling_coeff: float = 0.012
    air_density: float = 1.225
    gravity: float = 9.81

@dataclass
class DieselElectric:
    engine_peak_kw: float = 210.0
    generator_eff: float = 0.93
    engine_to_wheel_eff: float = 0.94
    motor_peak_kw: float = 300.0
    inverter_eff: float = 0.97
    motor_eff: float = 0.94

@dataclass
class TurbineElectric:
    turbine_modules: int = 2
    module_kw: float = 70.0
    generator_eff: float = 0.94
    motor_peak_kw: float = 300.0
    inverter_eff: float = 0.97
    motor_eff: float = 0.94
    recuperator_eff: float = 0.70
    thermal_eff_at_design: float = 0.35

class ComparisonSimulator:
    def __init__(self, vehicle=None):
        self.v = vehicle or Vehicle()

    def road_load_kw(self, speed_kph, grade=0.0):
        speed = speed_kph / 3.6
        aero = 0.5 * self.v.air_density * self.v.cd * self.v.area_m2 * speed**3
        rolling = self.v.mass_kg * self.v.gravity * self.v.rolling_coeff * speed
        grade_force = self.v.mass_kg * self.v.gravity * grade * speed
        return max(0.0, (aero + rolling + grade_force) / 1000.0)

    def diesel(self, battery_assist_kw=0.0, engine_load=1.0):
        engine = self._clamp(engine_load) * 210.0
        traction_from_engine = engine * 0.94
        motor_wheel = min(max(0.0, battery_assist_kw), 300.0 * 0.97 * 0.94)
        return {
            "architecture": "diesel-electric",
            "primary_generation_kw": round(engine * 0.93, 2),
            "direct_engine_wheel_kw": round(traction_from_engine, 2),
            "motor_wheel_kw": round(motor_wheel, 2),
            "nominal_peak_wheel_kw": round(traction_from_engine + 300.0 * 0.97 * 0.94, 2),
        }

    def turbine(self, battery_assist_kw=0.0, module_load=1.0):
        gross = 2 * 70.0 * self._clamp(module_load)
        electrical = gross * 0.94
        motor_wheel = min(max(0.0, battery_assist_kw + electrical), 300.0 * 0.97 * 0.94)
        return {
            "architecture": "Jaguar-style-turbine-electric",
            "turbine_gross_kw": round(gross, 2),
            "turbine_electrical_kw": round(electrical, 2),
            "motor_wheel_kw": round(motor_wheel, 2),
            "nominal_turbine_generation_kw": round(electrical, 2),
            "nominal_motor_peak_wheel_kw": round(300.0 * 0.97 * 0.94, 2),
        }

    @staticmethod
    def _clamp(x):
        return max(0.0, min(1.0, x))

if __name__ == "__main__":
    s = ComparisonSimulator()
    print(s.diesel(battery_assist_kw=100))
    print(s.turbine(battery_assist_kw=100))
    print("road_load_200_kph_kw:", round(s.road_load_kw(200), 2))
