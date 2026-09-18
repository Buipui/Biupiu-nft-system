import type { ProviderAdapter, ProviderAdapterId, ProviderJobInput, ProviderJobResult } from "./provider-adapter";
import { ProviderRegistry } from "./provider-registry";

export interface ExecutionPolicy { maxAttempts:number; retryableStates:string[]; }
export interface ExecutionResult extends ProviderJobResult { attempts:number; }

export class RenderExecutionBroker {
  constructor(private registry:ProviderRegistry, private policy:ExecutionPolicy={maxAttempts:3,retryableStates:["FAILED"]}){}
  async submit(provider:ProviderAdapterId,input:ProviderJobInput):Promise<ExecutionResult>{
    const adapter=this.registry.get(provider); if(!adapter) throw new Error("Provider adapter not registered");
    let attempts=0; let result:ProviderJobResult;
    do { attempts++; result=await adapter.submit(input); }
    while(this.policy.retryableStates.includes(result.state) && attempts<this.policy.maxAttempts);
    return {...result,attempts};
  }
}