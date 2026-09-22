import sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; sys.path.insert(0,str(ROOT))
from biupiu_os.cross_domain import CrossDomainValidator
class TestCrossDomainValidator(unittest.TestCase):
    def test_consistency(self):
        v=CrossDomainValidator()
        r=v.validate_cycle_to_mission({"status":"completed","target_net_kw":140},{"status":"completed","peak_battery_kw":100})
        self.assertTrue(r["valid"])
    def test_contradiction(self):
        v=CrossDomainValidator()
        r=v.fuel_rate_consistency({"fuel_kg_h":-1})
        self.assertFalse(r["valid"]); self.assertIn("NEGATIVE_FUEL_RATE",r["issues"])
if __name__=="__main__": unittest.main()
