export type RenderWorkspaceView="JOB_CREATE"|"QUEUE"|"JOB_DETAIL"|"PROVENANCE"|"OUTPUT_REVIEW";
export interface RenderWorkspaceModel { view:RenderWorkspaceView; jobId?:string; state?:string; sourceAssetIds:string[]; provider?:string; workflow?:string; output?:string; outputAssetIds:string[]; reviewRequired:boolean; }
export const RENDER_WORKSPACE_ROUTE="RENDER_PIPELINE";