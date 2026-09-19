export type ConversionStatus = "READY" | "BLOCKED" | "LOSSY" | "FAILED";
export type MaterialFeature = "BASE_COLOR" | "METALLIC" | "ROUGHNESS" | "TRANSMISSION" | "NORMAL" | "DISPLACEMENT" | "SUBSURFACE" | "CLEARCOAT";

export interface MaterialTranslationRule {
  sourceFeature: MaterialFeature;
  targetFeature?: MaterialFeature;
  supported: boolean;
  fallback?: string;
  lossReason?: string;
}

export interface ConversionReport {
  sourceAssetId: string;
  sourceModelVersion: string;
  sourceFormat: string;
  targetFormat: string;
  provider: string;
  status: ConversionStatus;
  rules: MaterialTranslationRule[];
  unsupportedFeatures: MaterialFeature[];
  warnings: string[];
  provenanceRequired: true;
}

export function createConversionReport(input: Omit<ConversionReport, "status">): ConversionReport {
  const unsupported = input.rules.filter(rule => !rule.supported).map(rule => rule.sourceFeature);
  const status: ConversionStatus = unsupported.length ? "LOSSY" : "READY";
  return { ...input, unsupportedFeatures: unsupported, status };
}

export const RED_06_RULES = {
  failClosedOnMissingSourceIdentity: true,
  neverSilentlyDropMaterialFeatures: true,
  unsupportedFeaturesRequireReport: true,
  derivativeCannotOverwriteSource: true,
  provenanceRequired: true
} as const;
