export type EquivalenceStatus = "PASS" | "DRIFT" | "BLOCKED";
export type EquivalenceDomain = "GEOMETRY" | "TRANSFORM" | "MATERIAL" | "METADATA" | "PROVENANCE";
export interface ProviderSnapshot { provider:string; format:string; sourceAssetId:string; sourceModelVersion:string; geometrySignature:string; transformSignature:string; materialSignature:string; metadataSignature:string; provenanceSignature:string; }
export interface ProviderEquivalenceFinding { provider:string; domain:EquivalenceDomain; severity:"INFO"|"ERROR"|"BLOCKED"; message:string; }
export interface ProviderEquivalenceReport { sourceAssetId:string; sourceModelVersion:string; providers:string[]; findings:ProviderEquivalenceFinding[]; status:EquivalenceStatus; measuredOutputsRequired:true; provenanceRequired:true; }
export function compareProviderMatrix(baseline:ProviderSnapshot, snapshots:ProviderSnapshot[]):ProviderEquivalenceReport {
 const findings:ProviderEquivalenceFinding[]=[];
 for(const s of snapshots){
  if(s.sourceAssetId!==baseline.sourceAssetId) findings.push({provider:s.provider,domain:"PROVENANCE",severity:"BLOCKED",message:"Source asset identity differs from authoritative baseline."});
  if(s.sourceModelVersion!==baseline.sourceModelVersion) findings.push({provider:s.provider,domain:"METADATA",severity:"BLOCKED",message:"Source model version differs from authoritative baseline."});
  if(s.geometrySignature!==baseline.geometrySignature) findings.push({provider:s.provider,domain:"GEOMETRY",severity:"ERROR",message:"Geometry signature differs from baseline."});
  if(s.transformSignature!==baseline.transformSignature) findings.push({provider:s.provider,domain:"TRANSFORM",severity:"ERROR",message:"Transform signature differs from baseline."});
  if(s.materialSignature!==baseline.materialSignature) findings.push({provider:s.provider,domain:"MATERIAL",severity:"ERROR",message:"Material signature differs from baseline; inspect RED-06 loss report."});
  if(s.metadataSignature!==baseline.metadataSignature) findings.push({provider:s.provider,domain:"METADATA",severity:"ERROR",message:"Metadata signature differs from baseline."});
  if(s.provenanceSignature!==baseline.provenanceSignature) findings.push({provider:s.provider,domain:"PROVENANCE",severity:"BLOCKED",message:"Provenance signature differs from baseline."});
 }
 const blocked=findings.some(f=>f.severity==="BLOCKED");
 return {sourceAssetId:baseline.sourceAssetId,sourceModelVersion:baseline.sourceModelVersion,providers:snapshots.map(s=>s.provider),findings,status:blocked?"BLOCKED":findings.length?"DRIFT":"PASS",measuredOutputsRequired:true,provenanceRequired:true};
}
export const RED_08_RULES={authoritativeBaselineRequired:true,providerIdentityRecorded:true,lossMustBeClassified:true,provenanceMismatchBlocksAcceptance:true,liveMeasuredOutputsRequired:true,cosmeticRenderDifferencesRequireSeparateVisualReview:true} as const;