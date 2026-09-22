import sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; sys.path.insert(0,str(ROOT))
from biupiu_os import BiupiuKernel
class TestExecution(unittest.TestCase):
    def test_registered_module_executes_through_kernel(self):
        k=BiupiuKernel(ROOT); found=k.discover()
        self.assertTrue(any(c.name=="biupiu_kernel_smoke" and c.status=="loadable" for c in found))
        r=k.execute_registered("biupiu_kernel_smoke",{"value":4,"scale":5},provenance=["controlled-smoke"])
        self.assertEqual(r.outputs["status"],"completed"); self.assertEqual(r.outputs["scaled"],20)
        self.assertEqual(r.evidence_state,"simulated")
    def test_failed_module_is_recorded_not_crashed(self):
        k=BiupiuKernel(ROOT)
        r=k.execute("intentional-failure",lambda **_: 1/0,{})
        self.assertEqual(r.outputs["status"],"failed")
        self.assertTrue(any(w.startswith("EXECUTION_ERROR:") for w in r.warnings))
if __name__=="__main__": unittest.main()
