import type { QueuedRenderJob, QueueState } from "./queue";
import type { RenderProvenance } from "./provenance";
export interface RenderJobRecord extends QueuedRenderJob { createdAt:string; updatedAt:string; providerJobId?:string; outputAssetIds:string[]; provenance?:RenderProvenance; error?:string; }
export interface RenderJobRepository { create(record:RenderJobRecord):Promise<RenderJobRecord>; get(jobId:string):Promise<RenderJobRecord|undefined>; update(jobId:string,patch:Partial<RenderJobRecord>):Promise<RenderJobRecord>; list(states?:QueueState[]):Promise<RenderJobRecord[]>; }
export class MemoryRenderJobRepository implements RenderJobRepository {
 private records=new Map<string,RenderJobRecord>();
 async create(record:RenderJobRecord){if(this.records.has(record.jobId))return this.records.get(record.jobId)!;this.records.set(record.jobId,record);return record;}
 async get(jobId:string){return this.records.get(jobId);}
 async update(jobId:string,patch:Partial<RenderJobRecord>){const current=this.records.get(jobId);if(!current)throw new Error("Render job not found");const next={...current,...patch,updatedAt:new Date().toISOString()};this.records.set(jobId,next);return next;}
 async list(states?:QueueState[]){const all=[...this.records.values()];return states?.length?all.filter(x=>states.includes(x.state)):all;}
}