export type RendererTarget = "unreal-engine-5"|"blender"|"redshift"|"v-ray"|"octane"|"lumion"|"keyshot";
export interface ProviderPackageRequest { digitalTwinId:string; sourceAssetId:string; sourceModelVersion:string; presetId:string; renderer:RendererTarget; licenceState:"PENDING"|"CLEARED"|"RESTRICTED"; referenceState:"FM6-REFERENCE-ONLY"; }
export interface ProviderPackagePlan { packageId:string; renderer:RendererTarget; status:"READY_FOR_ENVIRONMENT_EXECUTION"; source:Pick<ProviderPackageRequest,"digitalTwinId"|"sourceAssetId"|"sourceModelVersion"|"presetId">; validation:{provenance:"PASS"; licence:"PASS"; referenceBoundary:"PASS"; rendererEnvironment:"NOT_EXECUTED"}; }
export function createFM6ProviderPackagePlan(r:ProviderPackageRequest):ProviderPackagePlan {
 if(r.referenceState!=="FM6-REFERENCE-ONLY") throw new Error("FM6 reference boundary failed.");
 if(r.licenceState!=="CLEARED") throw new Error("Only cleared assets may be packaged.");
 if(!r.digitalTwinId||!r.sourceAssetId||!r.sourceModelVersion||!r.presetId) throw new Error("Complete lineage is required.");
 return {packageId:"BIU-"+r.digitalTwinId+"-"+r.renderer+"-"+r.sourceModelVersion,renderer:r.renderer,status:"READY_FOR_ENVIRONMENT_EXECUTION",source:{digitalTwinId:r.digitalTwinId,sourceAssetId:r.sourceAssetId,sourceModelVersion:r.sourceModelVersion,presetId:r.presetId},validation:{provenance:"PASS",licence:"PASS",referenceBoundary:"PASS",rendererEnvironment:"NOT_EXECUTED"}};
}