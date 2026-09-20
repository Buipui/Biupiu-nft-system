import { appendConversionLineage, createProvenance } from "./src/provenance";
const p=createProvenance({jobId:"job-001",sourceAssetIds:["asset-001"],sourceModelVersion:"v1",provider:"BLENDER"});
const next=appendConversionLineage(p,{sourceFormat:"GLTF",targetFormat:"OBJ",provider:"BLENDER",status:"LOSSY",unsupportedFeatures:["SUBSURFACE"],warnings:["subsurface fallback"]});
if(next.conversions?.length!==1) throw new Error("Conversion lineage missing.");
if(next.conversions[0].unsupportedFeatures[0]!=="SUBSURFACE") throw new Error("Loss detail missing.");
if(next.sourceAssetIds[0]!=="asset-001") throw new Error("Source identity changed.");
console.log("Persistent conversion lineage gate: PASS");
