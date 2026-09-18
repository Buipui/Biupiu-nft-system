import type { RenderJob } from "./index";
export type QueueState="QUEUED"|"RUNNING"|"REVIEW"|"APPROVED"|"FAILED"|"ARCHIVED";
export interface QueuedRenderJob extends RenderJob { jobId:string; workflow:string; state:QueueState; sourceModelVersion:string; }