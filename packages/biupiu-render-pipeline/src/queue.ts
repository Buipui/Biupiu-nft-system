import type { RenderJob } from "./index";
import type { ProviderAdapterId } from "./provider-adapter";
export type QueueState="QUEUED"|"RUNNING"|"REVIEW"|"APPROVED"|"FAILED"|"ARCHIVED";
export interface QueuedRenderJob extends Omit<RenderJob,"provider"> { jobId:string; workflow:string; state:QueueState; sourceModelVersion:string; provider:ProviderAdapterId; }