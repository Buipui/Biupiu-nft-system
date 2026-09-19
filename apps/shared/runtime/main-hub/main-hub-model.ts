export type HubState="ENTERABLE"|"LOCKED";
export interface HubDestination { id:string; label:string; route:"SMART_FARMING"|"SMART_METAL_WORKSHOP"|"RND_OS"|"RENDER_PIPELINE"; state:HubState; reason:"AUTHORIZED"|"NO_ENTITLEMENT"|"INACTIVE_ACCOUNT"; }
export interface HubSession { subscriberId:string; status:"active"|"suspended"|"pending"; entitlements:string[]; }
export function buildHub(session:HubSession):HubDestination[]{
 const routes=[{id:"farming_world",label:"FARMING WORLD",route:"SMART_FARMING" as const},{id:"metal_making_world",label:"METAL MAKING WORLD",route:"SMART_METAL_WORKSHOP" as const},{id:"rnd_os",label:"R&D OS",route:"RND_OS" as const},{id:"render_pipeline",label:"RENDER PIPELINE",route:"RENDER_PIPELINE" as const}];
 return routes.map(item=>{
  if(session.status!=="active") return {...item,state:"LOCKED" as const,reason:"INACTIVE_ACCOUNT" as const};
  if(item.route==="RND_OS"||session.entitlements.includes(item.route)||session.entitlements.includes("RENDER:ALL")||session.entitlements.some(e=>e.startsWith("RENDER:"))) return {...item,state:"ENTERABLE" as const,reason:"AUTHORIZED" as const};
  return {...item,state:"LOCKED" as const,reason:"NO_ENTITLEMENT" as const};
 });
}