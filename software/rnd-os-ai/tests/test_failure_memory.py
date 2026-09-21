import unittest,json
from multi_ai.failure_memory import FailureMemory

class FailureMemoryTests(unittest.TestCase):
    def test_record_is_deterministic_and_retained(self):
        m=FailureMemory()
        a=m.record("VIS-NATIVE-19","build","release smoke failure","assert compiled out")
        b=m.record("VIS-NATIVE-19","build","release smoke failure","assert compiled out")
        self.assertEqual(a.failure_id,b.failure_id)
        self.assertEqual(len(m.regressions_for("VIS-NATIVE-19")),1)
    def test_resolution_is_explicit(self):
        m=FailureMemory(); x=m.record("VIS-NATIVE-20","provider","compiler unavailable","CI evidence")
        y=m.resolve(x.failure_id,"provider remains optional")
        self.assertTrue(y.resolved)
        self.assertIn("provider remains optional",m.export())
    def test_unknown_resolution_rejected(self):
        with self.assertRaises(KeyError): FailureMemory().resolve("missing","x")

if __name__=="__main__": unittest.main()
