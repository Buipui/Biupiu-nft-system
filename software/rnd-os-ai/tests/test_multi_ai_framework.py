import unittest
from multi_ai.biupiu_multi_ai import Evidence,MultiAIOrchestrator,State

class MultiAIFrameworkTests(unittest.TestCase):
    def test_harvest_before_proposal(self):
        o=MultiAIOrchestrator(); item=o.create("NATIVE-AI-01","Build next native OS gate")
        with self.assertRaises(ValueError): o.propose(item,"unharvested")
        o.harvest(item,[Evidence.from_text("repository","existing-module","render graph; scheduler")])
        o.propose(item,"reuse existing scheduler and extend native graph"); o.implement(item); o.verify(item,True)
        self.assertEqual(item.state,State.VERIFIED); self.assertEqual(len(item.evidence),1)
        self.assertEqual(len(item.roles),8); self.assertEqual(len(item.signature()),64)

    def test_failure_is_retained(self):
        o=MultiAIOrchestrator(); item=o.create("NATIVE-AI-02","Validate provider")
        o.harvest(item,[Evidence.from_text("repo","provider","fixture")]); o.propose(item,"execute twice")
        o.implement(item); o.verify(item,False,"provider unavailable")
        self.assertEqual(item.state,State.BLOCKED); self.assertEqual(item.failures,["provider unavailable"])

if __name__=="__main__": unittest.main()
