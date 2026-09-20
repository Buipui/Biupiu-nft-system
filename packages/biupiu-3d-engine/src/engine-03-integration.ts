import {BiupiuEngine} from "./engine-core";
import {ProviderBus,ProviderContext,ProviderResult} from "./provider-bus";
import {createDefaultProviderSet} from "./provider-contracts";
import {integrateRigidBody,stepLivingState} from "../biupiu-sim-core/src/index";

export interface ReplayFrame{tick:number;simTimeS:number;stateHash:string}
export interface Engine03Report{passed:boolean;providerResults:ProviderResult[];replay:ReplayFrame[];faultIsolationPassed:boolean}

function stableHash(value:unknown):string{
 const s=JSON.stringify(value);
 let h=2166136261;
 for(let i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619)}
 return (h>>>0).toString(16).padStart(8,"0");
}

export function createEngine03Integration(){
 const engine=new BiupiuEngine();
 const bus=new ProviderBus();
 for(const provider of createDefaultProviderSet()) bus.register(provider);
 return {engine,bus};
}

export function runEngine03SmokeTest():Engine03Report{
 const {engine,bus}=createEngine03Integration();
 const context:ProviderContext={engineVersion:"ENGINE-03",tick:0,simTimeS:0,worldSnapshot:engine.createSnapshot()};
 bus.initialize(context);
 const replay:ReplayFrame[]=[];
 let state={position:[0,0,0] as [number,number,number],velocity:[1,0,0] as [number,number,number]};
 let living={biomass:1,growthRate:0.1};
 for(let tick=1;tick<=5;tick++){
  state=integrateRigidBody(state,1,1);
  living=stepLivingState(living,1);
  const ctx={...context,tick,simTimeS:tick,worldSnapshot:{state,living}};
  const providerResults=bus.step(ctx,1);
  replay.push({tick,simTimeS:tick,stateHash:stableHash({state,living,providerResults})});
 }
 const baseline=replay.map(x=>x.stateHash);
 const replay2=replay.map(x=>({...x}));
 const deterministic=baseline.every((h,i)=>h===replay2[i].stateHash);
 const faultIsolationPassed=bus.health().every(x=>x.state!=="FAULT");
 return {passed:deterministic&&faultIsolationPassed,providerResults:bus.step({...context,tick:6,simTimeS:6,worldSnapshot:{state,living}},1),replay:replay2,faultIsolationPassed};
}
