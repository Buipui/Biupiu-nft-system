export type ExecutionState="queued"|"validating"|"ready"|"running"|"completed"|"failed";
export interface ExecutionRecord {jobId:string;assetId:string;state:ExecutionState;backend:string;outputPath?:string;error?:string;updatedAt:string;}
export function transition(record:ExecutionRecord,state:ExecutionState,details?:Partial<ExecutionRecord>):ExecutionRecord{
  return {...record,...details,state,updatedAt:new Date().toISOString()};
}
