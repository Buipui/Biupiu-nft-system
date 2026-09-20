export type ProviderKind="SIMULATION"|"PHYSICS"|"LIVING_SYSTEMS"|"XR"|"RENDERER"|"ASSET";
export type ProviderState="REGISTERED"|"READY"|"RUNNING"|"DEGRADED"|"FAULT";
export interface ProviderContext{engineVersion:string;tick:number;simTimeS:number;worldSnapshot:unknown}
export interface ProviderResult{providerId:string;state:ProviderState;warnings:string[];faults:string[];outputs:Record<string,unknown>}
export interface BiupiuProvider{id:string;kind:ProviderKind;version:string;init(context:ProviderContext):void;step?(context:ProviderContext,dtS:number):ProviderResult;shutdown?():void}
export class ProviderBus{
 private providers=new Map<string,BiupiuProvider>(); private states=new Map<string,ProviderState>();
 register(p:BiupiuProvider){if(this.providers.has(p.id))throw new Error("duplicate provider: "+p.id);this.providers.set(p.id,p);this.states.set(p.id,"REGISTERED")}
 initialize(context:ProviderContext){for(const p of this.providers.values()){try{p.init(context);this.states.set(p.id,"READY")}catch(e){this.states.set(p.id,"FAULT");throw e}}}
 step(context:ProviderContext,dtS:number){const results:ProviderResult[]=[];for(const p of this.providers.values()){if(this.states.get(p.id)==="FAULT")continue;try{const result=p.step?p.step(context,dtS):{providerId:p.id,state:"RUNNING" as ProviderState,warnings:[],faults:[],outputs:{}};this.states.set(p.id,result.faults.length?"DEGRADED":"RUNNING");results.push(result)}catch(e){this.states.set(p.id,"FAULT");results.push({providerId:p.id,state:"FAULT",warnings:[],faults:[e instanceof Error?e.message:String(e)],outputs:{}})}}return results}
 health(){return [...this.providers.keys()].map(id=>({id,kind:this.providers.get(id)!.kind,state:this.states.get(id)}))}
}
