import {ProviderBus,BiupiuProvider,ProviderContext,ProviderResult} from "./provider-bus";
import {createDefaultProviderSet} from "./provider-contracts";

export type Promotion="REGISTERED"|"INTEGRATED"|"CONNECTED"|"VERIFIED"|"BLOCKED";
export interface RegressionCase{id:string;description:string;run:()=>boolean}
export interface RegressionReport{passed:boolean;cases:{id:string;passed:boolean}[];promotion:Promotion;faultIsolationPassed:boolean}

function context(tick=1):ProviderContext{return{engineVersion:"ENGINE-04",tick,simTimeS:tick,worldSnapshot:{}}}

export function runEngine04Regression():RegressionReport{
 const cases:RegressionCase[]=[];
 cases.push({id:"provider-uniqueness",description:"duplicate provider IDs are rejected",run:()=>{
  const b=new ProviderBus();const p=createDefaultProviderSet()[0];b.register(p);
  try{b.register(p);return false}catch{return true}
 }});
 cases.push({id:"invalid-timestep",description:"invalid timestep is rejected by contract provider",run:()=>{
  const p=createDefaultProviderSet()[0];p.init(context());
  try{p.step?.(context(),0);return false}catch{return true}
 }});
 cases.push({id:"fault-isolation",description:"provider fault does not crash bus",run:()=>{
  const b=new ProviderBus();
  const bad:BiupiuProvider={id:"fault-injection",kind:"PHYSICS",version:"test",init(){},step(){throw new Error("injected")}};
  const good=createDefaultProviderSet()[0];b.register(bad);b.register(good);b.initialize(context());
  const out=b.step(context(),1);
  return out.some(x=>x.providerId==="fault-injection"&&x.state==="FAULT")&&out.some(x=>x.providerId===good.id&&x.state==="RUNNING");
 }});
 cases.push({id:"deterministic-contract",description:"same contract input yields same output",run:()=>{
  const p=createDefaultProviderSet()[0];p.init(context());
  return JSON.stringify(p.step?.(context(7),1))===JSON.stringify(p.step?.(context(7),1));
 }});
 const results=cases.map(c=>({id:c.id,passed:c.run()}));
 const faultIsolationPassed=results.find(x=>x.id==="fault-isolation")?.passed===true;
 const passed=results.every(x=>x.passed);
 return{passed,cases:results,promotion:passed?"VERIFIED":"BLOCKED",faultIsolationPassed};
}
