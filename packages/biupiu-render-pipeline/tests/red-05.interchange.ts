import { createProviderPackage, type UniversalAssetManifest } from "../src/interchange";

const manifest: UniversalAssetManifest = {
  schema: "biupiu.universal-asset.v1",
  sourceAssetId: "BIUPIU-RENDER-TEST-001",
  sourceModelVersion: "TEST-001",
  researchIds: [],
  evidenceState: "EXPERIMENTAL",
  ipState: "INTERNAL",
  licenceState: "PENDING",
  geometry: { interchangeFormats: ["GLTF","FBX","USD"], units: "metric", coordinateSystem: "right-handed", upAxis: "Z" },
  materials: [{
    materialId: "MAT-001",
    name: "Test",
    pbr: { roughness: 0.5 },
    licenceState: "PENDING"
  }],
  provenance: { sourceCommit: "TEST" }
};

for (const provider of ["BLENDER","UNREAL_ENGINE_5","REDSHIFT","VRAY","OCTANE","LUMION","KEYSHOT"]) {
  const pkg = createProviderPackage(manifest, provider, "GLTF");
  if (pkg.manifest.sourceAssetId !== manifest.sourceAssetId) throw new Error("Source identity changed.");
  if (pkg.manifest.materials[0].materialId !== "MAT-001") throw new Error("Material identity changed.");
}
