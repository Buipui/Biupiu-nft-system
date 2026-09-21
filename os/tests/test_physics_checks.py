import sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; sys.path.insert(0,str(ROOT))
from biupiu_os.physics_checks import cycle_energy_balance,temperature_order
class TestPhysicsChecks(unittest.TestCase):
    def test_cycle_balance(self):
        r={"air_kg_s":1,"fuel_kg_h":100,"target_net_kw":100,"specific_electric_work_kj_kg":100}
        c=cycle_energy_balance(r)
        self.assertTrue(c.valid); self.assertLess(abs(c.metrics["relative_power_residual"]),.02)
    def test_bad_balance_detected(self):
        r={"air_kg_s":1,"fuel_kg_h":100,"target_net_kw":100,"specific_electric_work_kj_kg":50}
        self.assertFalse(cycle_energy_balance(r).valid)
    def test_temperature_order(self):
        self.assertTrue(temperature_order({"ambient_K":288,"T2_K":400,"T3_K":700,"T5_K":600}).valid)
        self.assertFalse(temperature_order({"ambient_K":288,"T2_K":700,"T3_K":600,"T5_K":500}).valid)
if __name__=="__main__": unittest.main()
