"""Source-level semantic contract audit across native Biupiu systems."""
from __future__ import annotations
import ast, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
TARGETS={
"AI":"software/rnd-os-ai/src/biupiu_ai",
"OS":"packages/biupiu-rnd-os/src",
"INTELLIGENCE":"intelligence",
"DIGITAL_TWIN":"digital-twin",
"DMS":"dms",
"SIMULATORS":"simulators",
"SMART_FARMING":"smart-farming",
}
REQUIRED_TOKENS={
"software/rnd-os-ai/src/biupiu_ai/guided_fault_finding.py":("promotion_allowed","requires_os_validation","evidence_refs"),
"software/rnd-os-ai/src/biupiu_ai/learning_federation_bridge.py":("provenance_hash","ADAPTATION_PROPOSAL","append"),
"software/rnd-os-ai/src/biupiu_ai/federation_protocol.py":("gate_passes","federation_ready","VERIFIED"),
"packages/biupiu-rnd-os/src/guided-fault-finder.ts":("QUARANTINED","stopConditions","evidenceRefs"),
"packages/biupiu-rnd-os/src/federation-contracts.ts":("schemaVersion","provenance","correlation"),
"intelligence/BIUPIU-BLOCKCHAIN-ANCHOR-BOUNDARY.py":("merkle_root","promotion_ready","inclusion_proof"),
}
def run():
    results=[]
    for rel,tokens in REQUIRED_TOKENS.items():
        p=ROOT/rel
        if not p.is_file(): results.append((rel,"FAIL","missing")); continue
        s=p.read_text(encoding="utf-8")
        missing=[t for t in tokens if t not in s]
        if p.suffix==".py":
            try: ast.parse(s,filename=str(p))
            except SyntaxError as e: missing.append("SYNTAX:"+str(e))
        results.append((rel,"PASS" if not missing else "FAIL",missing))
    return results
if __name__=="__main__":
    for rel,status,missing in run(): print(status,rel,missing)
