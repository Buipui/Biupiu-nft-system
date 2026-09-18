export const BIUPIU_APP = "Biupiu Render Pipeline";
export const PACKAGE = "@biupiu/render-pipeline";
export type RenderProvider = "BLENDER"|"UNREAL_ENGINE_5"|"TWINMOTION"|"KEYSHOT"|"ADOBE"|"FIREFLY"|"RUNWAY";
export interface RenderJob { sourceAssetIds:string[]; provider:RenderProvider; output:"STILL"|"VIDEO"|"AUDIO"|"SHOWREEL"; provenanceRequired:true; }