import type { AccessContext } from "./index";
export type RenderCapability="PRODUCT_STILL"|"DIGITAL_TWIN"|"CINEMATIC_SHOWREEL"|"CONCEPT_VARIATION"|"RESEARCH_VISUALIZATION";
export function authorizeRender(context:AccessContext, capability:RenderCapability){
 if(context.status!=="active") return {allowed:false,capability,reason:"subscriber-not-active"};
 const key="RENDER:"+capability;
 const allowed=context.entitlements.includes("RENDER:ALL")||context.entitlements.includes(key);
 return {allowed,capability,reason:allowed?"entitled":"missing-entitlement"};
}