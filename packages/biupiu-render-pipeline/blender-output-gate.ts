import type { UniversalAssetManifest } from "./src/interchange";
import { UNIVERSAL_INTERCHANGE_RULES } from "./src/interchange";

export interface BlenderOutput {
  providerJobId: string;
  state: "QUEUED" | "RUNNING" | "REVIEW" | "APPROVED" | "FAILED";
  outputAssetIds: string[];
  manifest: UniversalAssetManifest;
}

export function validateBlenderOutput(output: BlenderOutput): void {
  if (!output.providerJobId) throw new Error("Blender output requires providerJobId.");
  if (!output.outputAssetIds.length) throw new Error("Blender output requires output assets.");

  const m = output.manifest;
  if (m.schema !== "biupiu.universal-asset.v1") throw new Error("Unsupported universal asset schema.");
  if (!m.sourceAssetId || !m.sourceModelVersion) throw new Error("Source identity is required.");
  if (!m.researchIds) throw new Error("Research linkage is required.");
  if (!m.licenceState) throw new Error("Licence state is required.");
  if (!m.ipState) throw new Error("IP state is required.");
  if (!m.evidenceState) throw new Error("Evidence state is required.");
  if (!m.geometry.interchangeFormats.length) throw new Error("Interchange format is required.");
  for (const material of m.materials) {
    if (!material.materialId || !material.licenceState) {
      throw new Error("Every material requires identity and licence state.");
    }
  }
  if (!UNIVERSAL_INTERCHANGE_RULES.sourceAssetIsAuthoritative ||
      !UNIVERSAL_INTERCHANGE_RULES.derivativesCannotOverwriteSource ||
      !UNIVERSAL_INTERCHANGE_RULES.provenanceRequired) {
    throw new Error("Universal interchange rules are not active.");
  }
}
