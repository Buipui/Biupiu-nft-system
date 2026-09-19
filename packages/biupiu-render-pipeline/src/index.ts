export const BIUPIU_APP = "Biupiu Render Pipeline";
export const PACKAGE = "@biupiu/render-pipeline";
export type RenderProvider = "BLENDER"|"MAXON_CINEMA_4D"|"REDSHIFT"|"UNREAL_ENGINE_5"|"TWINMOTION"|"LUMION"|"KEYSHOT"|"OCTANE"|"VRAY"|"ADOBE"|"FIREFLY"|"RUNWAY";
export interface RenderJob { sourceAssetIds:string[]; provider:RenderProvider; output:"STILL"|"VIDEO"|"AUDIO"|"SHOWREEL"; provenanceRequired:true; }
export { REDSHIFT_OSL_VALIDATION_SET, REDSHIFT_PROVIDER_CONTRACT, REDSHIFT_VALIDATION_RULES, validateRedshiftEnvironment } from "./redshift";
export type { RedshiftAdapter, RedshiftEnvironment, RedshiftHost, RedshiftDeviceKind, RedshiftValidationResult } from "./redshift";
export { createProviderPackage, UNIVERSAL_INTERCHANGE_RULES } from "./interchange";
export type { InterchangeFormat, MaterialSlot, UniversalAssetManifest, ProviderPackage } from "./interchange";
export { createConversionReport, RED_06_RULES } from "./conversion";
export type { ConversionStatus, MaterialFeature, MaterialTranslationRule, ConversionReport } from "./conversion";
