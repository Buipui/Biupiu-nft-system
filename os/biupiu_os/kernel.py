import json,time,uuid
from pathlib import Path
from .environment import EnvironmentEngine
from .guards import challenge_inputs,guard_evidence
from .models import Capability,EnvironmentState,EvidenceRecord
from .registry import CapabilityRegistry
class BiupiuKernel:
    def __init__(self,repo_root=None):
        self.repo_root=Path(repo_root or Path(__file__).resolve().parents[2]); self.registry=CapabilityRegistry(); self.environment=EnvironmentEngine(); self.audit=[]; self._register_core()
    def _register_core(self):
        for c in [Capability("biupiu-kernel","os","Biupiu"),Capability("evidence-guard","trust","Biupiu"),Capability("environment-engine","simulation","Biupiu"),Capability("audit-ledger","governance","Biupiu")]: self.registry.register(c)
    def discover(self): return self.registry.discover_existing_simulators(self.repo_root)
    def execute(self,module,operation,inputs,*,evidence_state="simulated",measured_evidence_complete=False,review_passed=False,provenance=None):
        eid=uuid.uuid4().hex; warnings=challenge_inputs(inputs); outputs=dict(operation(**inputs) or {})
        proposed={"execution_id":eid,"module":module,"evidence_state":evidence_state,"measured_evidence_complete":measured_evidence_complete,"review_passed":review_passed}
        guard=guard_evidence(proposed)
        if not guard["valid"]:
            warnings.extend(guard["errors"])
            if evidence_state in ("validated","certified"): evidence_state="simulated"
        rec=EvidenceRecord(eid,module,evidence_state,inputs,outputs,warnings,provenance or [],review_passed); self.audit.append(rec); return rec
    def environment_step(self,env,dt_s,updates=None): return self.environment.step(env,dt_s,updates)
    def audit_json(self): return json.dumps([r.to_dict() for r in self.audit],indent=2,sort_keys=True)
    def health(self): return {"kernel":"operational","capabilities":len(self.registry.all()),"audit_records":len(self.audit),"timestamp":time.time()}
