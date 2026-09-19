export type DriftSeverity = "NONE" | "INFO" | "WARNING" | "ERROR" | "BLOCKED";
export type DriftDomain = "GEOMETRY" | "TRANSFORM" | "MATERIAL" | "TEXTURE" | "CAMERA" | "METADATA" | "PROVENANCE";
export interface DriftFinding { domain: DriftDomain; severity: DriftSeverity; field: string; expected?: string | number | boolean; actual?: string | number | boolean; message: string; }
export interface RoundTripSnapshot { sourceAssetId:string; sourceModelVersion:string; provider:string; format:string; geometrySignature:string; transformSignature:string; materialSignature:string; metadataSignature:string; provenanceSignature:string; }
export interface RoundTripReport { sourceAssetId:string; sourceModelVersion:string; provider:string; path:string[]; findings:DriftFinding[]; status:"PASS"|"DRIFT"|"BLOCKED"; provenanceRequired:true; }
export function compareRoundTrip(source:RoundTripSnapshot, returned:RoundTripSnapshot):RoundTripReport {
 const findings:DriftFinding[]=[];
 const compare=(domain:DriftDomain,field:string,expected:string,actual:string)=>{ if(expected!==actual){ const hard=domain==="PROVENANCE"||field==="sourceAssetId"||field==="sourceModelVersion"; findings.push({domain,severity:hard?"BLOCKED":"ERROR",field,expected,actual,message:hard?"Authoritative identity/provenance drift blocks acceptance.":"Round-trip signature drift detected."}); } };
 compare("PROVENANCE","sourceAssetId",source.sourceAssetId,returned.sourceAssetId);
 compare("METADATA","sourceModelVersion",source.sourceModelVersion,returned.sourceModelVersion);
 compare("GEOMETRY","geometrySignature",source.geometrySignature,returned.geometrySignature);
 compare("TRANSFORM","transformSignature",source.transformSignature,returned.transformSignature);
 compare("MATERIAL","materialSignature",source.materialSignature,returned.materialSignature);
 compare("METADATA","metadataSignature",source.metadataSignature,returned.metadataSignature);
 compare("PROVENANCE","provenanceSignature",source.provenanceSignature,returned.provenanceSignature);
 const blocked=findings.some(f=>f.severity==="BLOCKED");
 return {sourceAssetId:source.sourceAssetId,sourceModelVersion:source.sourceModelVersion,provider:returned.provider,path:["SOURCE_ASSET","PROVIDER","INTERCHANGE","PROVIDER","SOURCE_ASSET"],findings,status:blocked?"BLOCKED":findings.length?"DRIFT":"PASS",provenanceRequired:true};
}
export const RED_07_RULES={sourceIdentityDriftBlocksAcceptance:true,provenanceDriftBlocksAcceptance:true,geometryDriftRequiresReview:true,materialDriftRequiresReview:true,metadataDriftMustBeReported:true,providerSpecificCosmeticDifferencesAreNotAutomaticallyAssetDrift:true,liveRendererComparisonRequiresMeasuredOutputs:true} as const;