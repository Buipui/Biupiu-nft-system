import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; sys.path.insert(0,str(ROOT))
from biupiu_os import BiupiuKernel,EnvironmentState
def test_kernel_and_environment():
    k=BiupiuKernel(ROOT); k.discover(); e=EnvironmentState("test",variables={"temperature_K":293.15}); e2=k.environment_step(e,1,{"temperature_K":294.15}); assert e2.timestep_s==1 and e.timestep_s==0
def test_evidence_guard():
    k=BiupiuKernel(ROOT); r=k.execute("screening",lambda **kw:{"value":kw["x"]*2},{"x":3}); assert r.outputs["value"]==6 and r.evidence_state=="simulated"
def test_validation_claim_is_downgraded_without_measurement():
    k=BiupiuKernel(ROOT); r=k.execute("screening",lambda **kw:{"value":1},{},evidence_state="validated"); assert r.evidence_state=="simulated" and "VALIDATED_REQUIRES_MEASURED_EVIDENCE" in r.warnings
