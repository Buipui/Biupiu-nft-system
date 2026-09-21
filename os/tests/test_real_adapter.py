import sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; sys.path.insert(0,str(ROOT))
from biupiu_os import BiupiuKernel
class TestExistingSimulatorAdapter(unittest.TestCase):
    def test_existing_propulsion_model_executes_unchanged(self):
        k=BiupiuKernel(ROOT); k.discover()
        r=k.execute_registered("biupiu_propulsion_adapter",{"rpm":2000,"throttle":1.0,"speed_kph":60,"battery_assist_kw":50})
        self.assertEqual(r.outputs["status"],"completed")
        self.assertIn("wheel_power_kw",r.outputs)
        self.assertEqual(r.evidence_state,"simulated")
if __name__=="__main__": unittest.main()
