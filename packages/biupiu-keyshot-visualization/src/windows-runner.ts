import {validateRenderJob} from "./job-validator";
export function prepareWindowsExecution(job:any, keyshotExecutable:string){
  const validation=validateRenderJob(job);
  if(!validation.valid) return {ok:false,errors:validation.errors};
  if(job.backend!=="local-keyshot") return {ok:false,errors:["Windows runner requires local-keyshot backend"]};
  if(!keyshotExecutable) return {ok:false,errors:["KeyShot executable path is not configured"]};
  return {ok:true,command:{executable:keyshotExecutable,jobId:job.jobId,input:job.input.sourcePath,profile:job.profile,output:job.output}};
}
