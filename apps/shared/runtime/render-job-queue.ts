export type RenderJobState="QUEUED"|"RUNNING"|"REVIEW"|"APPROVED"|"FAILED"|"ARCHIVED";
export interface RenderQueueJob { jobId:string; sourceAssetIds:string[]; provider:string; workflow:string; output:"STILL"|"VIDEO"|"AUDIO"|"SHOWREEL"; state:RenderJobState; provenance:{sourceModelVersion:string; parentJobId?:string}; }
export const RENDER_QUEUE_ROUTE="RENDER_PIPELINE";