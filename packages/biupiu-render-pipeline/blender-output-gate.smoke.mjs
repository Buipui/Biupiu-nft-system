import { validateBlenderOutput } from "./blender-output-gate";
const valid = {
  providerJobId: "blender-job-001",
  state: "REVIEW",
  outputAssetIds: ["asset-output-001"],
  manifest: {
    schema: "biupiu.universal-asset.v1",
    sourceAssetId: "asset-source-001",
    sourceModelVersion: "model-v1",
    researchIds: ["research-001"],
    evidenceState: "DOCUMENTED",
    ipState: "INTERNAL",
    licenceState: "CLEARED",
    geometry: { interchangeFormats: ["GLTF"], units: "metric", coordinateSystem: "right-handed", upAxis: "Z" },
    materials: [{ materialId: "mat-001", name: "body", pbr: { metallic: 0.5, roughness: 0.4 }, licenceState: "CLEARED" }],
    provenance: { parentAssetId: "asset-source-001" }
  }
} as const;
validateBlenderOutput(valid);
let blocked = false;
try { validateBlenderOutput({ ...valid, manifest: { ...valid.manifest, sourceAssetId: "" } }); } catch { blocked = true; }
if (!blocked) throw new Error("Invalid source identity was not blocked.");
console.log("Blender provenance/interchange gate: PASS");
