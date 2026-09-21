import unittest
from multi_ai.dependency_graph import Gate,audit,deterministic_order

class DependencyGraphTests(unittest.TestCase):
    def test_native_visual_chain(self):
        gates=[
            Gate("VIS-NATIVE-19","implemented",()),
            Gate("VIS-NATIVE-20","implemented",("VIS-NATIVE-19",)),
            Gate("VIS-NATIVE-21","implemented",("VIS-NATIVE-20",)),
            Gate("VIS-NATIVE-22","implemented",("VIS-NATIVE-19","VIS-NATIVE-21")),
            Gate("VIS-NATIVE-23","implemented",("VIS-NATIVE-19","VIS-NATIVE-22")),
        ]
        self.assertEqual(deterministic_order(gates),["VIS-NATIVE-19","VIS-NATIVE-20","VIS-NATIVE-21","VIS-NATIVE-22","VIS-NATIVE-23"])
        self.assertTrue(all(x.classification=="PASS" for x in audit(gates)))
    def test_missing_dependency_blocks(self):
        x=audit([Gate("AI-NATIVE-03","implemented",("MISSING",))])[0]
        self.assertEqual(x.classification,"BLOCKED")
    def test_cycle_rejected(self):
        with self.assertRaises(ValueError):
            deterministic_order([Gate("A","implemented",("B",)),Gate("B","implemented",("A",))])

if __name__=="__main__": unittest.main()
