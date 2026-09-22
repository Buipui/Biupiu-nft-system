export type FaultClass="TRANSPORT"|"DEPENDENCY"|"CONTRACT"|"VALIDATION"|"AUTHORITY"|"MODEL"|"DATA"|"RUNTIME"|"SECURITY";
export type FaultState="OBSERVED"|"TRIAGING"|"ISOLATED"|"FIX_PROPOSED"|"FIX_VERIFIED"|"REGRESSION_VERIFIED"|"QUARANTINED"|"CLOSED";
export interface FaultSignal{source:string;faultClass:FaultClass;stateSignature:string;severity:"LOW"|"MEDIUM"|"HIGH"|"CRITICAL";message:string;evidenceRefs:string[];traceId?:string;spanId?:string}
export interface FaultFinding{faultId:string;state:FaultState;canonicalOwner:string;subsystemPath:string[];faultClass:FaultClass;confidence:number;nextStep:string;requiredEvidence:string[];stopConditions:string[];candidateCauses:string[]}
const rank:Record<FaultClass,string[]>={
TRANSPORT:["verify delivery/TTL/backpressure","inspect correlation/trace context"],
DEPENDENCY:["compare dependency/version lock state","run isolated dependency smoke test"],
CONTRACT:["validate schema/version/content-type","compare producer/consumer contract"],
VALIDATION:["re-run the failing validation with captured inputs","check requirement/evidence mapping"],
AUTHORITY:["identify canonical owner","quarantine conflicting state and open reconciliation"],
MODEL:["compare assumptions, units and model version","run baseline/reference case"],
DATA:["validate provenance/schema/range/unit constraints","replay with known-good fixture"],
RUNTIME:["capture trace/span and environment","reproduce in smallest supported runtime"],
SECURITY:["quarantine affected path","run security/permission/integrity checks"]};
export function guideFaultFinding(faultId:string,signal:FaultSignal,canonicalOwner:string,subsystemPath:string[]):FaultFinding{
if(!faultId.trim()||!canonicalOwner.trim()||subsystemPath.length===0)throw new Error("fault identity/ownership/path required");
const steps=rank[signal.faultClass],confidence=signal.evidenceRefs.length>0?.7:.35;
return{faultId,state:signal.faultClass==="SECURITY"?"QUARANTINED":"TRIAGING",canonicalOwner,subsystemPath,faultClass:signal.faultClass,confidence,nextStep:steps[0],requiredEvidence:[...steps,"record result and residual error","regression-test before closure"],stopConditions:["missing provenance","conflicting authoritative state","untrusted executable dependency"],candidateCauses:[signal.message,signal.stateSignature]};}
