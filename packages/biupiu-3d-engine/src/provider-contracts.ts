import {BiupiuProvider,ProviderContext,ProviderResult} from "./provider-bus";

export function contractProvider(id:string,kind:BiupiuProvider["kind"],version="0.1.0"):BiupiuProvider{
 return {id,kind,version,init(){},step(ctx:ProviderContext,dtS:number):ProviderResult{
  if(!Number.isFinite(dtS)||dtS<=0)throw new Error("invalid provider timestep");
  return {providerId:id,state:"RUNNING",warnings:[],faults:[],outputs:{tick:ctx.tick,simTimeS:ctx.simTimeS}};
 }};
}

export function createDefaultProviderSet(){
 return [
  contractProvider("biupiu-simulation-core","SIMULATION"),
  contractProvider("biupiu-physics-provider","PHYSICS"),
  contractProvider("biupiu-living-systems","LIVING_SYSTEMS"),
  contractProvider("biupiu-xr-openxr","XR"),
  contractProvider("biupiu-render-provider","RENDERER"),
  contractProvider("biupiu-asset-provenance","ASSET")
 ];
}
