import sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; sys.path.insert(0,str(ROOT))
from biupiu_os import BiupiuKernel
from biupiu_os.physics_checks import cycle_energy_balance
class TestFailureLearning(unittest.TestCase):
    def test_recurrence_is_detected(self):
        k=BiupiuKernel(ROOT)
        def bad(**_): return {"air_kg_s":1,"fuel_kg_h":100,"target_net_kw":100,"specific_electric_work_kj_kg":50}
        k.execute("bad-cycle",bad,{},physics_check=cycle_energy_balance)
        k.execute("bad-cycle",bad,{},physics_check=cycle_energy_balance)
        s=k.failure_learning.summary()
        self.assertEqual(s["total_failures"],2)
        self.assertGreaterEqual(s["recurring_signatures"],1)
    def test_success_is_not_recorded(self):
        k=BiupiuKernel(ROOT)
        def ok(**_): return {"value":1}
        r=k.execute("ok",ok,{})
        self.assertEqual(r.outputs["status"],"completed")
        self.assertEqual(k.failure_learning.summary()["total_failures"],0)
if __name__=="__main__": unittest.main()
