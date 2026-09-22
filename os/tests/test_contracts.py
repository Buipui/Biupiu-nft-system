import sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; sys.path.insert(0,str(ROOT))
from biupiu_os import SimulationRequest,validate_request,system_health,BiupiuKernel
from biupiu_os.adapters import default_adapters
class TestContracts(unittest.TestCase):
    def test_request_contract(self):
        req=validate_request(SimulationRequest("demo",{"mass_kg":10})); self.assertEqual(req.module,"demo")
    def test_adapter_boundary_fails_closed(self):
        adapter=default_adapters()[0]; self.assertFalse(adapter.health()["runtime_available"])
        with self.assertRaisesRegex(RuntimeError,"runtime is not installed"): adapter.execute({})
    def test_system_health(self):
        h=system_health(BiupiuKernel(ROOT)); self.assertTrue(h["verification_policy"]["validated_requires_measurement"]); self.assertGreaterEqual(len(h["adapters"]),6)
if __name__=="__main__": unittest.main()
