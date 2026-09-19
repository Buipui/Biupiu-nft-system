export type ValidationMetric = "provenance"|"material"|"lod"|"camera"|"lighting";
export interface RenderEvidence { renderer:string; rendererVersion:string; packageId:string; outputHash:string; metrics:Partial<Record<ValidationMetric,"PASS"|"FAIL"|"NOT_EXECUTED">>; }
export interface CrossRenderReport { digitalTwinId:string; referenceState:"FM6-REFERENCE-ONLY"; status:"READY_FOR_ENVIRONMENT_VALIDATION"|"VALIDATED"|"FAILED"; renderers:string[]; evidence:RenderEvidence[]; }
export function createCrossRenderReport(digitalTwinId:string, packageIds:string[]):CrossRenderReport {
 if(!digitalTwinId || packageIds.length===0) throw new Error("Digital Twin ID and package IDs are required.");
 return {digitalTwinId,referenceState:"FM6-REFERENCE-ONLY",status:"READY_FOR_ENVIRONMENT_VALIDATION",renderers:[],evidence:[]};
}
export function acceptRenderEvidence(report:CrossRenderReport,evidence:RenderEvidence):CrossRenderReport {
 if(evidence.packageId.length===0 || evidence.outputHash.length===0 || evidence.rendererVersion.length===0) throw new Error("Renderer version, package ID and output hash are required.");
 if(Object.values(evidence.metrics).includes("FAIL")) return {...report,status:"FAILED",renderers:[...new Set([...report.renderers,evidence.renderer])],evidence:[...report.evidence,evidence]};
 const evidenceList=[...report.evidence,evidence];
 const renderers=[...new Set([...report.renderers,evidence.renderer])];
 const complete=evidenceList.length>0 && evidenceList.every(e=>e.metrics.provenance==="PASS");
 return {...report,status:complete?"VALIDATED":"READY_FOR_ENVIRONMENT_VALIDATION",renderers,evidence:evidenceList};
}