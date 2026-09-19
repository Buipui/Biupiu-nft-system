import { createConversionReport, RED_06_RULES } from "../src/conversion";

const report = createConversionReport({
  sourceAssetId: "BIUPIU-RENDER-TEST-001",
  sourceModelVersion: "TEST-001",
  sourceFormat: "GLTF",
  targetFormat: "USD",
  provider: "UNREAL_ENGINE_5",
  rules: [
    { sourceFeature: "BASE_COLOR", targetFeature: "BASE_COLOR", supported: true },
    { sourceFeature: "CLEARCOAT", supported: false, fallback: "ROUGHNESS_APPROXIMATION", lossReason: "Target adapter does not guarantee clearcoat parity." }
  ],
  unsupportedFeatures: [],
  warnings: [],
  provenanceRequired: true
});
if (report.status !== "LOSSY") throw new Error("RED-06 must report unsupported features as LOSSY.");
if (!report.unsupportedFeatures.includes("CLEARCOAT")) throw new Error("Unsupported feature was not recorded.");
if (!RED_06_RULES.neverSilentlyDropMaterialFeatures) throw new Error("RED-06 loss reporting rule missing.");
if (!report.provenanceRequired) throw new Error("RED-06 provenance requirement missing.");
