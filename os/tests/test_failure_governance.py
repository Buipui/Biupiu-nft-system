import unittest
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]; sys.path.insert(0,str(ROOT))
from biupiu_os import BiupiuKernel
from biupiu_os.physics_checks import cycle_energy_balance

class TestFailureGovernance(unittest.TestCase):
    def test_cluster_requires_approval(self):
        k=BiupiuKernel(ROOT)
        def bad(**_): return {"air_kg_s":1,"fuel_kg_h":100,"target_net_kw":100,"specific_electric_work_kj_kg":50}
        k.execute("bad-cycle",bad,{},physics_check=cycle_energy_balance)
        k.execute("bad-cycle",bad,{},physics_check=cycle_energy_balance)
        proposals=k.propose_failure_remediation()
        self.assertEqual(len(proposals),1)
        self.assertEqual(proposals[0]["status"],"pending_human_approval")
        approved=k.approve_failure_remediation(proposals[0]["proposal_id"])
        self.assertEqual(approved["status"],"approved")

if __name__=="__main__": unittest.main()
