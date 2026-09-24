from __future__ import annotations
import hashlib, json, time
from pathlib import Path
from biupiu_ai.compute_federation import ComputeClass, ComputeFederation, ComputeUnit, HostTopology, Workload
from biupiu_ai.quantum_federation import select_quantum_candidate

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"research/BIUPIU-BLIND-BENCHMARK-QUANTUM-VS-FEDERATION-RESULT-20260924.json"
ITERATIONS={"L0":10000,"L1":5000,"L2":3000,"L3":2000,"L4":1000}

def digest(v):
    return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def arm_a(p):
    topology=HostTopology("blind-host","blind-arch",(ComputeUnit("u0",ComputeClass.PERFORMANCE,2.0),ComputeUnit("u1",ComputeClass.GPU,8.0),ComputeUnit("u2",ComputeClass.EFFICIENCY,1.0)))
    f=ComputeFederation(topology)
    plan=f.plan([Workload("physics",p["cost"],preferred=(ComputeClass.GPU,ComputeClass.PERFORMANCE)),Workload("ui",2.0,minimum=(ComputeClass.EFFICIENCY,ComputeClass.PERFORMANCE))])
    return {"decision":plan,"success_rate":f.telemetry.success_rate}

def arm_b(p):
    return {"decision":select_quantum_candidate(classical_score=p["classical_score"],quantum_simulator_score=p["quantum_simulator_score"],uncertainty=p["uncertainty"],resource_pressure=p["resource_pressure"]),"qpu_activation":"DISABLED"}

def run(fn,p,n):
    s=time.perf_counter_ns(); last=None
    for _ in range(n): last=fn(p)
    e=time.perf_counter_ns()-s
    return {"iterations":n,"mean_ns":e/n,"result_hash":digest(last),"result":last}

def main():
    p={"cost":8.0,"classical_score":0.55,"quantum_simulator_score":0.72,"uncertainty":0.20,"resource_pressure":0.40}
    raw={}
    for label,fn in (("ARM-A",arm_a),("ARM-B",arm_b)):
        raw[label]={level:run(fn,p,n) for level,n in ITERATIONS.items()}
    out={"schema":"biupiu.blind-benchmark.result.v1","date":"2026-09-24","status":"RAW_EXECUTION_RECORDED","arms":raw,"identity_unsealed":False,"qpu":"DISABLED","promotion":"NONE","winner":"NOT_ASSIGNED","quantum_advantage":"NOT_CLAIMED"}
    OUT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(out,indent=2))

if __name__=="__main__":
    main()
