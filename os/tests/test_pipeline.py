import sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; sys.path.insert(0,str(ROOT))
from biupiu_os import BiupiuKernel
class TestPipeline(unittest.TestCase):
    def test_two_stage_pipeline(self):
        k=BiupiuKernel(ROOT); k.discover()
        records,state=k.execute_pipeline([
            {"module":"biupiu_material_screen","inputs":{"modulus_GPa":20,"density_kg_m3":1000}},
            {"module":"biupiu_load_screen","inputs":{"load_N":500}}
        ],provenance=["controlled-pipeline"])
        self.assertEqual(len(records),2); self.assertEqual(records[-1].outputs["status"],"completed")
        self.assertAlmostEqual(state["screening_index"],0.04)
        self.assertEqual(records[-1].evidence_state,"simulated")
    def test_bad_schema_stops_pipeline(self):
        k=BiupiuKernel(ROOT); k.discover()
        records,state=k.execute_pipeline([{"module":"biupiu_material_screen","inputs":{"modulus_GPa":"bad","density_kg_m3":1000}}])
        self.assertEqual(records[0].outputs["status"],"failed")
if __name__=="__main__": unittest.main()
