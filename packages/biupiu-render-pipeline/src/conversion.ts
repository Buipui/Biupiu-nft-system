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


export interface ConversionExecutionInput {
  manifest: import("./interchange").UniversalAssetManifest;
  sourceFormat: string;
  targetFormat: string;
  provider: string;
  rules: MaterialTranslationRule[];
}

export function validateConversionInput(input: ConversionExecutionInput): ConversionReport {
  if (!input.manifest.sourceAssetId || !input.manifest.sourceModelVersion) {
    throw new Error("Conversion requires source asset identity and model version.");
  }
  if (!input.manifest.provenance) throw new Error("Conversion requires provenance.");
  if (input.manifest.materials.some(material => !material.materialId || !material.licenceState)) {
    throw new Error("Conversion requires material identity and licence state.");
  }
  const report = createConversionReport({
    sourceAssetId: input.manifest.sourceAssetId,
    sourceModelVersion: input.manifest.sourceModelVersion,
    sourceFormat: input.sourceFormat,
    targetFormat: input.targetFormat,
    provider: input.provider,
    rules: input.rules,
    unsupportedFeatures: [],
    warnings: [],
    provenanceRequired: true
  });
  if (report.status === "LOSSY" && !RED_06_RULES.unsupportedFeaturesRequireReport) {
    throw new Error("Lossy conversion policy is not active.");
  }
  return report;
}
