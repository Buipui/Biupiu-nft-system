export type ResourcePromotion="REGISTERED"|"INTEGRATED"|"CONNECTED"|"VERIFIED"|"BLOCKED";

export interface ResourceCandidate{
 id:string;
 source:string;
 license:string;
 role:string;
 promotion:ResourcePromotion;
}

export interface ResourceGateResult{
 passed:boolean;
 blocked:string[];
 eligible:string[];
}

export class ResourceGateway{
 private readonly resources=new Map<string,ResourceCandidate>();

 register(resource:ResourceCandidate){
  if(this.resources.has(resource.id)) throw new Error("duplicate-resource:"+resource.id);
  if(!resource.id||!resource.source||!resource.license||!resource.role) throw new Error("invalid-resource-contract");
  this.resources.set(resource.id,{...resource});
 }

 promote(id:string,target:ResourcePromotion){
  const r=this.resources.get(id);
  if(!r) throw new Error("unknown-resource:"+id);
  if(r.promotion==="BLOCKED") throw new Error("blocked-resource:"+id);
  r.promotion=target;
 }

 list(){return [...this.resources.values()].map(r=>({...r}));}

 evaluate():ResourceGateResult{
  const blocked=this.list().filter(r=>r.promotion==="BLOCKED").map(r=>r.id);
  const eligible=this.list().filter(r=>r.promotion!=="BLOCKED").map(r=>r.id);
  return{passed:blocked.length===0,blocked,eligible};
 }
}

export function runResourceGatewaySmokeTest(){
 const g=new ResourceGateway();
 g.register({id:"openxr-sdk",source:"https://github.com/KhronosGroup/OpenXR-SDK",license:"Apache-2.0",role:"xr-loader-api",promotion:"REGISTERED"});
 g.register({id:"jolt-physics",source:"https://github.com/jrouwe/JoltPhysics",license:"MIT",role:"physics-provider",promotion:"REGISTERED"});
 g.promote("openxr-sdk","INTEGRATED");
 const result=g.evaluate();
 return result.passed && result.eligible.includes("openxr-sdk") && result.eligible.includes("jolt-physics");
}
