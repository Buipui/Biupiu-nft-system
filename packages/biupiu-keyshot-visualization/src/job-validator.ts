export interface ValidationResult { valid:boolean; errors:string[]; }
const profiles=new Set(["automotive-concept","marine-concept","evtol-helicopter","microturbine","biocomposite","bio-adhesive-resin","textile-fibre","product-hero","engineering-exploded","turntable-showreel"]);
export function validateRenderJob(job:any):ValidationResult{
  const errors:string[]=[];
  if(!job?.jobId) errors.push("jobId is required");
  if(!job?.assetId) errors.push("assetId is required");
  if(!profiles.has(job?.profile)) errors.push("unsupported render profile");
  if(!job?.input?.sourcePath) errors.push("input.sourcePath is required");
  if(!job?.output?.format) errors.push("output.format is required");
  if(!Number.isInteger(job?.output?.width)||job.output.width<1) errors.push("output.width must be a positive integer");
  if(!Number.isInteger(job?.output?.height)||job.output.height<1) errors.push("output.height must be a positive integer");
  if(job?.backend!=="local-keyshot" && job?.backend!=="aws-deadline-cloud") errors.push("unsupported backend");
  return {valid:errors.length===0,errors};
}
