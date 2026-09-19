import type { ProviderAdapterId, ProviderJobInput } from "./provider-adapter";
import type { RenderCapability } from "@biupiu/access/render-entitlements";
import { RenderExecutionBroker } from "./execution-broker";
import type { AccessContext } from "@biupiu/access";
import { authorizeRender } from "@biupiu/access/render-entitlements";
import { MemoryRenderJobRepository, type RenderJobRecord } from "./job-registry";
export interface CreateRenderRequest extends ProviderJobInput { capability:RenderCapability; provider:ProviderAdapterId; sourceModelVersion:string; }
export class RenderService {
 constructor(private repository:MemoryRenderJobRepository,private broker:RenderExecutionBroker){}
 async create(context:AccessContext,request:CreateRenderRequest){
  const decision=authorizeRender(context,request.capability);if(!decision.allowed)throw new Error("Render capability not entitled");
  const now=new Date().toISOString();const record:RenderJobRecord={...request,jobId:request.jobId,state:"QUEUED",createdAt:now,updatedAt:now,outputAssetIds:[],provenance:{jobId:request.jobId,sourceAssetIds:request.sourceAssetIds,sourceModelVersion:request.sourceModelVersion,provider:request.provider,createdAt:now}};
  return this.repository.create(record);
 }
 async execute(context:AccessContext,job:RenderJobRecord){
  const decision=authorizeRender(context,job.workflow as RenderCapability);if(!decision.allowed)throw new Error("Render capability not entitled");
  const result=await this.broker.submit(job.provider,{jobId:job.jobId,sourceAssetIds:job.sourceAssetIds,workflow:job.workflow,output:job.output,parameters:job.parameters});
  return this.repository.update(job.jobId,{state:result.state,providerJobId:result.providerJobId,outputAssetIds:result.outputAssetIds});
 }
}