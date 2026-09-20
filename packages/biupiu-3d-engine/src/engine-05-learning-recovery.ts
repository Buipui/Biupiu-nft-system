export type FailureClass="TRANSIENT"|"CONTRACT"|"RUNTIME"|"UNKNOWN";
export interface FailureLearningRecord{id:string;providerId:string;fault:string;classification:FailureClass;recoveryAttempted:boolean;recovered:boolean;}
export interface RegressionFixture{id:string;tick:number;stateHash:string;}
export interface Engine05Report{passed:boolean;fixtures:RegressionFixture[];learning:FailureLearningRecord[];recoveryPassed:boolean;}

export class FailureLearningStore{
 private records:FailureLearningRecord[]=[];
 record(r:FailureLearningRecord){this.records.push({...r});}
 all(){return [...this.records];}
 classify(fault:string):FailureClass{
  const s=fault.toLowerCase();
  if(s.includes("timeout")||s.includes("transient")||s.includes("tempor"))return"TRANSIENT";
  if(s.includes("contract")||s.includes("invalid"))return"CONTRACT";
  if(s.includes("runtime")||s.includes("exception"))return"RUNTIME";
  return"UNKNOWN";
 }
}

export function buildRegressionFixtures(states:unknown[]):RegressionFixture[]{
 return states.map((state,tick)=>{const s=JSON.stringify(state);let h=2166136261;for(let i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619)}return{id:`fixture-${tick}`,tick,stateHash:(h>>>0).toString(16).padStart(8,"0")}})
}

export function compareRegressionFixtures(expected:RegressionFixture[],actual:RegressionFixture[]){
 if(expected.length!==actual.length)return{passed:false,mismatches:["length"]};
 const mismatches:string[]=[];expected.forEach((e,i)=>{if(e.tick!==actual[i].tick||e.stateHash!==actual[i].stateHash)mismatches.push(e.id)});
 return{passed:mismatches.length===0,mismatches};
}
