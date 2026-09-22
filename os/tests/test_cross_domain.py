import sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; sys.path.insert(0,str(ROOT))
from biupiu_os import BiupiuKernel
class TestCrossDomain(unittest.TestCase):
    def test_cycle_and_mission_run_through_os(self):
        k=BiupiuKernel(ROOT); k.discover()
        cycle=k.execute_registered("biupiu_cycle_adapter",{"target_kw":140,"altitude_m":0})
        mission=k.execute_registered("biupiu_mission_adapter",{"package_name":"BT-140","mission":"AUTO"})
        self.assertEqual(cycle.outputs["status"],"completed")
        self.assertIn("fuel_kg_h",cycle.outputs)
        self.assertEqual(mission.outputs["status"],"completed")
        self.assertIn("system_specific_power_kw_per_kg",mission.outputs)
        self.assertEqual(cycle.evidence_state,"simulated")
        self.assertEqual(mission.evidence_state,"simulated")
    def test_cycle_parameter_sanity(self):
        k=BiupiuKernel(ROOT); k.discover()
        r=k.execute_registered("biupiu_cycle_adapter",{"target_kw":140,"pressure_ratio":5})
        self.assertEqual(r.outputs["status"],"completed")
        self.assertGreater(r.outputs["air_kg_s"],0)
if __name__=="__main__": unittest.main()
