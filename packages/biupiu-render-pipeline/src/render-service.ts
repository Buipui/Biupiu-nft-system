import type { ProviderAdapterId, ProviderJobInput } from "./provider-adapter";
import type { RenderCapability } from "@biupiu/access/render-entitlements";
import { RenderExecutionBroker } from "./execution-broker";
import type { AccessContext } from "@biupiu/access";
import { authorizeRender } from "@biupiu/access/render-entitlements";
import { MemoryRenderJobRepository, type RenderJobRecord } from "./job-registry";
import { validateBlenderOutput } from "../blender-output-gate";
import { appendConversionLineage } from "./provenance";
import type { ConversionLineage } from "./provenance";
export interface CreateRenderRequest extends Omit<ProviderJobInput, "output"> {
 capability:RenderCapability;
 provider:ProviderAdapterId;
 output:"STILL"|"VIDEO"|"AUDIO"|"SHOWREEL";
 sourceModelVersion:string;
 conversion?:ConversionLineage;
}
export class RenderService {
 constructor(private repository:MemoryRenderJobRepository,private broker:RenderExecutionBroker){}
 async create(context:AccessContext,request:CreateRenderRequest){
  const decision=authorizeRender(context,request.capability);if(!decision.allowed)throw new Error("Render capability not entitled");
  const now=new Date().toISOString();const record:RenderJobRecord={...request,jobId:request.jobId,state:"QUEUED",createdAt:now,updatedAt:now,outputAssetIds:[],provenanceRequired:true,provenance:{jobId:request.jobId,sourceAssetIds:request.sourceAssetIds,sourceModelVersion:request.sourceModelVersion,provider:request.provider,createdAt:now,...(request.conversion ? { conversions:[request.conversion] } : {})}};
  return this.repository.create(record);
 }
 async execute(context:AccessContext,job:RenderJobRecord){
  const decision=authorizeRender(context,job.workflow as RenderCapability);if(!decision.allowed)throw new Error("Render capability not entitled");
  const result=await this.broker.submit(job.provider,{jobId:job.jobId,sourceAssetIds:job.sourceAssetIds,workflow:job.workflow,output:job.output,parameters:job.parameters});
  if (job.provider === "BLENDER") {
    if (!result.manifest) throw new Error("Blender render output is missing its universal asset manifest.");
    validateBlenderOutput({ providerJobId: result.providerJobId, state: result.state, outputAssetIds: result.outputAssetIds, manifest: result.manifest });
  }
  return this.repository.update(job.jobId,{state:result.state,providerJobId:result.providerJobId,outputAssetIds:result.outputAssetIds,provenance:{...job.provenance!,providerJobId:result.providerJobId}});
 }
}