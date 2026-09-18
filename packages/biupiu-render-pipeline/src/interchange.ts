export type InterchangeFormat = "GLTF" | "FBX" | "OBJ" | "USD" | "USDZ" | "NATIVE";

export interface MaterialSlot {
  materialId: string;
  name: string;
  sourceMaterialId?: string;
  pbr: {
    baseColor?: string;
    metallic?: number;
    roughness?: number;
    transmission?: number;
    normalMapAssetId?: string;
  };
  licenceState: "PENDING" | "CLEARED" | "RESTRICTED";
}

export interface UniversalAssetManifest {
  schema: "biupiu.universal-asset.v1";
  sourceAssetId: string;
  sourceModelVersion: string;
  researchIds: string[];
  evidenceState: "DOCUMENTED" | "RECONSTRUCTED" | "EXPERIMENTAL" | "HYPOTHESIS" | "SPECULATIVE";
  ipState: "PUBLIC" | "INTERNAL" | "CONFIDENTIAL" | "PRE-PATENT";
  licenceState: "PENDING" | "CLEARED" | "RESTRICTED";
  geometry: {
    interchangeFormats: InterchangeFormat[];
    units: string;
    coordinateSystem: string;
    upAxis: "X" | "Y" | "Z";
  };
  materials: MaterialSlot[];
  provenance: {
    parentAssetId?: string;
    sourceCommit?: string;
    manifestHash?: string;
  };
}

export interface ProviderPackage {
  provider: string;
  manifest: UniversalAssetManifest;
  importFormat: InterchangeFormat;
  providerSettings: Record<string, string | number | boolean>;
}

export const UNIVERSAL_INTERCHANGE_RULES = {
  sourceAssetIsAuthoritative: true,
  derivativesCannotOverwriteSource: true,
  materialIdentityMustBePreserved: true,
  provenanceRequired: true,
  licenceStateRequired: true,
  measuredPropertiesMustNotBeInvented: true
} as const;

export function createProviderPackage(
  manifest: UniversalAssetManifest,
  provider: string,
  importFormat: InterchangeFormat,
  providerSettings: Record<string, string | number | boolean> = {}
): ProviderPackage {
  if (!manifest.sourceAssetId || !manifest.sourceModelVersion) {
    throw new Error("Universal asset manifest requires source identity and model version.");
  }
  if (manifest.materials.some(m => !m.materialId || !m.licenceState)) {
    throw new Error("Every material slot requires identity and licence state.");
  }
  return { provider, manifest, importFormat, providerSettings };
}
