export type RenderJobState = "queued"|"running"|"completed"|"failed";
export interface RenderJob { jobId:string; assetId:string; profile:string; input:{sourceFormat:string;sourcePath:string}; output:{format:string;width:number;height:number;frames?:number}; materialProfile?:string; environmentProfile?:string; cameraProfile?:string; distributed?:boolean; backend:"local-keyshot"|"aws-deadline-cloud"; }
export function createLocalKeyShotJob(job:RenderJob, executablePath:string) {
  if (job.backend !== "local-keyshot") throw new Error("Local adapter requires backend=local-keyshot");
  if (!executablePath) throw new Error("KeyShot executable path is required");
  return {jobId:job.jobId, executablePath, state:"queued" as RenderJobState};
}
