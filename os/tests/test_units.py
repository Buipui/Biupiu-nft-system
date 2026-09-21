import sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; sys.path.insert(0,str(ROOT))
from biupiu_os.units import Quantity,kg_h_to_kg_s
from biupiu_os.cross_domain import CrossDomainValidator
class TestUnits(unittest.TestCase):
    def test_power_conversion(self): self.assertEqual(Quantity(2,"kW").to("W").value,2000)
    def test_flow_conversion(self): self.assertAlmostEqual(kg_h_to_kg_s(3600),1)
    def test_dimension_mismatch(self):
        with self.assertRaises(ValueError): Quantity(2,"kW").to("K")
    def test_bounds(self):
        r=CrossDomainValidator().bounds({"pressure_ratio":5},{"pressure_ratio":(1,20)})
        self.assertTrue(r["valid"])
if __name__=="__main__": unittest.main()
