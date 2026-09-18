export const BIUPIU_APP = "Biupiu Render Pipeline";
export const PACKAGE = "@biupiu/render-pipeline";
export type RenderProvider = "BLENDER"|"MAXON_CINEMA_4D"|"REDSHIFT"|"UNREAL_ENGINE_5"|"TWINMOTION"|"LUMION"|"KEYSHOT"|"OCTANE"|"VRAY"|"ADOBE"|"FIREFLY"|"RUNWAY";
export interface RenderJob { sourceAssetIds:string[]; provider:RenderProvider; output:"STILL"|"VIDEO"|"AUDIO"|"SHOWREEL"; provenanceRequired:true; }