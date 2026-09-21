import sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; sys.path.insert(0,str(ROOT))
from biupiu_os import BiupiuKernel
class TestKernelPhysicsGuard(unittest.TestCase):
    def test_failed_physics_blocks_success(self):
        k=BiupiuKernel(ROOT)
        def bad(**_): return {"air_kg_s":1,"fuel_kg_h":100,"target_net_kw":100,"specific_electric_work_kj_kg":50}
        from biupiu_os.physics_checks import cycle_energy_balance
        r=k.execute("bad-cycle",bad,{},physics_check=cycle_energy_balance)
        self.assertEqual(r.outputs["status"],"physics_failed")
        self.assertTrue(any(w=="PHYSICS_CHECK:POWER_BALANCE_RESIDUAL" for w in r.warnings))
    def test_real_cycle_guard_path(self):
        k=BiupiuKernel(ROOT); k.discover()
        r=k.run_cycle_with_physics_guard({"target_kw":140})
        self.assertIn(r.outputs["status"],("completed","physics_failed"))
        self.assertIn("physics_check",r.outputs)
if __name__=="__main__": unittest.main()
