export type SafetyDecision="ALLOW"|"HOLD"|"DENY";
export interface SafetyGateInput { authorized:boolean; sourceAssetsPresent:boolean; providerHealthy:boolean; destructiveAction:boolean; }
export interface SafetyGateResult { decision:SafetyDecision; reasons:string[]; }
export function evaluateSafety(i:SafetyGateInput):SafetyGateResult {
 const reasons:string[]=[];
 if(!i.authorized)reasons.push("authorization-required");
 if(!i.sourceAssetsPresent)reasons.push("source-assets-missing");
 if(!i.providerHealthy)reasons.push("provider-unhealthy");
 if(i.destructiveAction)reasons.push("destructive-action-requires-review");
 if(reasons.length)return {decision:i.destructiveAction?"HOLD":"DENY",reasons};
 return {decision:"ALLOW",reasons:[]};
}