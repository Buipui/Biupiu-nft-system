import unittest
from multi_ai.native_main_boundary import Module,Authority,audit

class BoundaryTests(unittest.TestCase):
    def test_native_main_and_shared_contracts(self):
        findings=audit([
            Module("NativeVisual",Authority.NATIVE,"CABI:visual","implemented"),
            Module("MainOSAdapter",Authority.MAIN,"CABI:adapter","implemented"),
            Module("SharedScheduler",Authority.SHARED,"CABI:scheduler","implemented"),
        ])
        self.assertTrue(all(x.classification=="PASS" for x in findings))
    def test_external_authority_is_blocked(self):
        x=audit([Module("ExternalProvider",Authority.EXTERNAL,"SDK","authoritative")])[0]
        self.assertEqual(x.classification,"CONFLICT")

if __name__=="__main__": unittest.main()
