import { validateAssetManifest } from "../src/asset-manifest";
const good={assetId:"asset-microturbine-v1",name:"Biupiu Microturbine",domain:"microturbine",
source:{uri:"assets/microturbine.glb",format:"glb"},geometry:{status:"validated",units:"mm",scale:1},
materials:[{materialId:"mat-hemp-panel-v1",provenanceStatus:"verified" as const}],environment:"engineering-neutral",
validation:{status:"passed" as const,checkedAt:"2026-09-19T00:00:00Z"}};
if(validateAssetManifest(good).length) throw new Error("valid manifest rejected");
if(!validateAssetManifest({...good,geometry:{status:"pending"}}).includes("geometry must be validated")) throw new Error("unvalidated geometry accepted");
if(!validateAssetManifest({...good,materials:[{materialId:"x",provenanceStatus:"restricted"}]}).includes("restricted material cannot enter render manifest")) throw new Error("restricted material accepted");
