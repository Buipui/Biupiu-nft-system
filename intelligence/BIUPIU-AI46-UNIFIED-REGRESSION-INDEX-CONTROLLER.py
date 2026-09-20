"""AI-46 unified regression/index controller.

Indexes canonical gate states only; it never promotes evidence.
"""
from __future__ import annotations
import hashlib,json
from datetime import datetime,timezone
DOMAINS=["OS","DMS","INTELLIGENCE","SIMULATORS","CONFIGURATORS","MATH_PHYSICS","DIGITAL_TWIN","PROVENANCE","SECURITY","BLOCKCHAIN","HMI","RESEARCH"]
STATES=["DISCOVERED","ASSIGNED","EXECUTING","CHALLENGED","VALIDATED","REGRESSION_PASS","PROMOTION_READY","PROMOTED","PENDING_RUNTIME","REMEDIATION_REQUIRED","BLOCKED_UNTRUSTED_EVIDENCE","BLOCKED_CONTROL_CONTRACT"]
def digest(v): return hashlib.sha256(json.dumps(v,sort_keys=True).encode()).hexdigest()
def build_index(records):
    index={}
    for domain in DOMAINS:
        rs=[r for r in records if r.get("domain")==domain]
        index[domain]={"records":len(rs),
          "verified":sum(r.get("state")=="VERIFIED" for r in rs),
          "regression_pass":sum(r.get("state")=="REGRESSION_PASS" for r in rs),
          "promotion_ready":sum(r.get("state")=="PROMOTION_READY" for r in rs),
          "promoted":sum(r.get("state")=="PROMOTED" for r in rs),
          "pending":sum(r.get("state") not in ("REGRESSION_PASS","PROMOTION_READY","PROMOTED") for r in rs)}
    return {"schema":"BIUPIU-AI46-v2","timestamp":datetime.now(timezone.utc).isoformat(),
            "domains":index,"record_count":len(records),"index_hash":digest(index)}
