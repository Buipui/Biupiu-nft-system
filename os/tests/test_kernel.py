import sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; sys.path.insert(0,str(ROOT))
from biupiu_os import BiupiuKernel,EnvironmentState
class TestKernel(unittest.TestCase):
    def test_kernel_and_environment(self):
        k=BiupiuKernel(ROOT); e=EnvironmentState("test",variables={"temperature_K":293.15})
        e2=k.environment_step(e,1,{"temperature_K":294.15})
        self.assertEqual(e2.timestep_s,1); self.assertEqual(e.timestep_s,0)
    def test_evidence_guard(self):
        k=BiupiuKernel(ROOT); r=k.execute("screening",lambda **kw:{"value":kw["x"]*2},{"x":3})
        self.assertEqual(r.outputs["value"],6); self.assertEqual(r.evidence_state,"simulated")
    def test_validation_claim_is_downgraded_without_measurement(self):
        k=BiupiuKernel(ROOT); r=k.execute("screening",lambda **kw:{"value":1},{},evidence_state="validated")
        self.assertEqual(r.evidence_state,"simulated")
        self.assertIn("VALIDATED_REQUIRES_MEASURED_EVIDENCE",r.warnings)
if __name__=="__main__": unittest.main()
