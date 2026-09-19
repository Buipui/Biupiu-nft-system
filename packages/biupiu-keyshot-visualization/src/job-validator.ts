export interface ValidationResult { valid:boolean; errors:string[]; }
const profiles=new Set(["automotive-concept","marine-concept","evtol-helicopter","microturbine","biocomposite","bio-adhesive-resin","textile-fibre","product-hero","engineering-exploded","turntable-showreel"]);
export interface ManifestGate { assetId:string; validation:{status:"passed"|"pending"|"failed"}; geometry:{status:"validated"|"pending"|"failed"}; materials:{materialId:string;provenanceStatus:"verified"|"pending-review"|"reference-only"|"restricted"}[]; environment:string; }
export function validateRenderJob(job:any, manifest?:ManifestGate):ValidationResult {
 const errors:string[]=[];
 if(!job?.jobId) errors.push("jobId is required"); if(!job?.assetId) errors.push("assetId is required");
 if(!profiles.has(job?.profile)) errors.push("unsupported render profile"); if(!job?.input?.sourcePath) errors.push("input.sourcePath is required");
 if(!job?.output?.format) errors.push("output.format is required");
 if(!Number.isInteger(job?.output?.width)||job.output.width<1) errors.push("output.width must be a positive integer");
 if(!Number.isInteger(job?.output?.height)||job.output.height<1) errors.push("output.height must be a positive integer");
 if(job?.backend!=="local-keyshot" && job?.backend!=="aws-deadline-cloud") errors.push("unsupported backend");
 if(manifest){ if(manifest.assetId!==job.assetId) errors.push("asset manifest assetId does not match render job"); if(manifest.validation.status!=="passed") errors.push("asset manifest validation must be passed"); if(manifest.geometry.status!=="validated") errors.push("asset geometry must be validated"); if(manifest.materials.some(m=>m.provenanceStatus==="restricted")) errors.push("render job contains restricted material"); if(!manifest.environment) errors.push("asset manifest environment is required"); } else errors.push("validated asset manifest is required before rendering");
 return {valid:errors.length===0,errors};
}