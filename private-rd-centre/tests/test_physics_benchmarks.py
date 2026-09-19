"""PHYS-SYS-02 numerical benchmark and conservation smoke tests."""
import importlib.util
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location("physics_kernel",ROOT/"private-rd-centre/engine/physics_kernel.py")
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

# Constant-force benchmark: this kernel uses explicit Euler position integration,
# so x is the sum of the pre-step velocities: 0.4995 m for this case.
body=m.RigidBody6DoF(2,1,1,1,m.Vec3(0,0,0),m.Vec3(0,0,0),m.Vec3(0,0,0))
dt=0.001
for _ in range(1000):
    body.step(m.Vec3(2,0,0),m.Vec3(0,0,0),dt)
assert abs(body.velocity_mps.x-1.0) < 1e-12
assert abs(body.position_m.x-0.4995) < 1e-12

body2=m.RigidBody6DoF(1,2,3,4,m.Vec3(0,0,0),m.Vec3(0,0,0),m.Vec3(0.3,-0.2,0.1))
for _ in range(100):
    body2.step(m.Vec3(0,0,0),m.Vec3(0,0,0),0.01)
assert body2.angular_rate_rps.x == 0.3
assert body2.angular_rate_rps.y == -0.2
assert body2.angular_rate_rps.z == 0.1

thermal=m.LumpedThermalModel(300,100,10)
for _ in range(100):
    thermal.step(0,300,0.1)
assert thermal.temperature_k == 300

rot=m.RotatingMachine(2,25)
for _ in range(100):
    rot.step(5,5,0.1)
assert rot.angular_speed_rad_s == 25

print("PHYS-SYS-02 numerical/conservation tests: PASS")
