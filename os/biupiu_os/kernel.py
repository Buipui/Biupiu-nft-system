import json,time,uuid
from pathlib import Path
from .environment import EnvironmentEngine
from .guards import challenge_inputs,guard_evidence
from .models import Capability,EnvironmentState,EvidenceRecord
from .registry import CapabilityRegistry
from .schemas import validate_mapping,validate_outputs
from .cross_domain import CrossDomainValidator
class BiupiuKernel:
    def __init__(self,repo_root=None):
        self.repo_root=Path(repo_root or Path(__file__).resolve().parents[2]); self.registry=CapabilityRegistry(); self.environment=EnvironmentEngine(); self.audit=[]; self.cross_domain=CrossDomainValidator(); self._register_core()
    def _register_core(self):
        for c in [Capability("biupiu-kernel","os","Biupiu"),Capability("evidence-guard","trust","Biupiu"),Capability("environment-engine","simulation","Biupiu"),Capability("audit-ledger","governance","Biupiu"),Capability("schema-guard","trust","Biupiu"),Capability("cross-domain-validator","trust","Biupiu")]: self.registry.register(c)
    def discover(self): return self.registry.discover_existing_simulators(self.repo_root)
    def execute(self,module,operation,inputs,*,evidence_state="simulated",measured_evidence_complete=False,review_passed=False,provenance=None):
        eid=uuid.uuid4().hex; warnings=challenge_inputs(inputs); status="completed"; outputs={}
        try:
            validate_mapping(inputs); outputs=dict(operation(**inputs) or {}); validate_outputs(outputs)
        except Exception as exc:
            status="failed"; warnings.append(f"EXECUTION_ERROR:{type(exc).__name__}:{exc}")
        proposed={"execution_id":eid,"module":module,"evidence_state":evidence_state,"measured_evidence_complete":measured_evidence_complete,"review_passed":review_passed}
        guard=guard_evidence(proposed)
        if not guard["valid"]:
            warnings.extend(guard["errors"])
            if evidence_state in ("validated","certified"): evidence_state="simulated"
        rec=EvidenceRecord(eid,module,evidence_state,inputs,{"status":status,**outputs},warnings,provenance or [],review_passed); self.audit.append(rec); return rec
    def execute_registered(self,module,inputs,**kwargs):
        target=next((c for c in self.registry.all() if c.name==module),None)
        if target is None: raise KeyError(f"capability not registered: {module}")
        if target.status!="loadable": raise RuntimeError(f"capability not executable: {module} [{target.status}]")
        path=self.repo_root/target.entrypoint
        import importlib.util
        spec=importlib.util.spec_from_file_location(module,path)
        if spec is None or spec.loader is None: raise RuntimeError(f"cannot load capability: {module}")
        loaded=importlib.util.module_from_spec(spec); spec.loader.exec_module(loaded)
        operation=getattr(loaded,"run",None) or getattr(loaded,"execute",None)
        if operation is None: raise AttributeError(f"{module} exposes no run/execute entrypoint")
        return self.execute(module,operation,inputs,**kwargs)
    def execute_pipeline(self,steps,initial_inputs=None,provenance=None):
        state=dict(initial_inputs or {}); records=[]
        for step in steps:
            module=step["module"]; inputs={**state,**dict(step.get("inputs",{}))}
            record=self.execute_registered(module,inputs,provenance=provenance or [])
            records.append(record)
            if record.outputs.get("status")!="completed": break
            state.update({k:v for k,v in record.outputs.items() if k!="status"})
        return records,state
    def environment_step(self,env,dt_s,updates=None): return self.environment.step(env,dt_s,updates)
    def audit_json(self): return json.dumps([r.to_dict() for r in self.audit],indent=2,sort_keys=True)
    def health(self): return {"kernel":"operational","capabilities":len(self.registry.all()),"audit_records":len(self.audit),"timestamp":time.time()}
