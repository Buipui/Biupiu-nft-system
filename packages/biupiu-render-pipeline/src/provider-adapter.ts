export type ProviderAdapterId="BLENDER"|"UNREAL_ENGINE_5"|"TWINMOTION"|"LUMION"|"KEYSHOT"|"ADOBE"|"FIREFLY"|"RUNWAY";
export type RenderOutput="STILL"|"VIDEO"|"AUDIO"|"SHOWREEL";
export interface ProviderAdapter { id:ProviderAdapterId; capabilities:string[]; submit(input:ProviderJobInput):Promise<ProviderJobResult>; }
export interface ProviderJobInput { jobId:string; sourceAssetIds:string[]; workflow:string; output:RenderOutput; parameters:Record<string,unknown>; }
import type { UniversalAssetManifest } from "./interchange";
export interface ProviderJobResult { providerJobId:string; state:"QUEUED"|"RUNNING"|"REVIEW"|"APPROVED"|"FAILED"; outputAssetIds:string[]; manifest?:UniversalAssetManifest; }