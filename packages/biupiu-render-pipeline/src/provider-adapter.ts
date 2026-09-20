export type ProviderAdapterId="BLENDER"|"UNREAL_ENGINE_5"|"TWINMOTION"|"KEYSHOT"|"ADOBE"|"FIREFLY"|"RUNWAY";
export interface ProviderAdapter { id:ProviderAdapterId; capabilities:string[]; submit(input:ProviderJobInput):Promise<ProviderJobResult>; }
export interface ProviderJobInput { jobId:string; sourceAssetIds:string[]; workflow:string; output:string; parameters:Record<string,unknown>; }
import type { UniversalAssetManifest } from "./interchange";
export interface ProviderJobResult { providerJobId:string; state:"QUEUED"|"RUNNING"|"REVIEW"|"APPROVED"|"FAILED"; outputAssetIds:string[]; manifest?:UniversalAssetManifest; }