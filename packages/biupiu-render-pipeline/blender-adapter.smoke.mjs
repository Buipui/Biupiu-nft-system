import { BlenderAdapter } from "../blender-adapter";
import { ProviderRegistry } from "./provider-registry";

const calls: unknown[] = [];
const adapter = new BlenderAdapter(async request => {
  calls.push(request);
  return {
    providerJobId: "blender-smoke-job",
    state: "REVIEW",
    outputAssetIds: ["asset-rendered-001"],
    manifest: {
      schema: "biupiu.universal-asset.v1", sourceAssetId: "asset-source-001", sourceModelVersion: "model-v1", researchIds: ["research-001"],
      evidenceState: "DOCUMENTED", ipState: "INTERNAL", licenceState: "CLEARED",
      geometry: { interchangeFormats: ["GLTF"], units: "metric", coordinateSystem: "right-handed", upAxis: "Z" },
      materials: [{ materialId: "mat-001", name: "body", pbr: { metallic: 0.5, roughness: 0.4 }, licenceState: "CLEARED" }],
      provenance: { parentAssetId: "asset-source-001" }
    }
  };
});

const registry = new ProviderRegistry();
registry.register(adapter);

if (!registry.has("BLENDER")) throw new Error("BLENDER adapter was not registered.");
const resolved = registry.get("BLENDER");
if (!resolved) throw new Error("BLENDER adapter could not be resolved.");

const result = await resolved.submit({
  jobId: "render-smoke-001",
  sourceAssetIds: ["asset-source-001"],
  workflow: "PRODUCT_STILL",
  output: "STILL",
  parameters: { engine: "BLENDER" }
});

if (result.providerJobId !== "blender-smoke-job") throw new Error("Unexpected provider job ID.");
if (result.outputAssetIds[0] !== "asset-rendered-001") throw new Error("Unexpected output asset.");
if (calls.length !== 1) throw new Error("Expected exactly one executor call.");

console.log("Blender adapter smoke test: PASS");
