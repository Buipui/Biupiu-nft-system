import { validateConversionInput } from "./src/conversion";
const manifest = {
 schema:"biupiu.universal-asset.v1", sourceAssetId:"source-001", sourceModelVersion:"v1",
 researchIds:["research-001"], evidenceState:"DOCUMENTED", ipState:"INTERNAL", licenceState:"CLEARED",
 geometry:{interchangeFormats:["GLTF"],units:"metric",coordinateSystem:"right-handed",upAxis:"Z"},
 materials:[{materialId:"mat-001",name:"body",pbr:{metallic:.5,roughness:.4},licenceState:"CLEARED"}],
 provenance:{parentAssetId:"source-001"}
};
const ready=validateConversionInput({manifest,sourceFormat:"GLTF",targetFormat:"USD",provider:"BLENDER",rules:[
 {sourceFeature:"BASE_COLOR",targetFeature:"BASE_COLOR",supported:true},
 {sourceFeature:"METALLIC",targetFeature:"METALLIC",supported:true}
]});
if(ready.status!=="READY") throw new Error("Expected READY conversion.");
const lossy=validateConversionInput({manifest,sourceFormat:"GLTF",targetFormat:"OBJ",provider:"BLENDER",rules:[
 {sourceFeature:"BASE_COLOR",targetFeature:"BASE_COLOR",supported:true},
 {sourceFeature:"SUBSURFACE",supported:false,fallback:"bake",lossReason:"Target format does not preserve subsurface."}
]});
if(lossy.status!=="LOSSY" || !lossy.unsupportedFeatures.includes("SUBSURFACE")) throw new Error("Lossy conversion was not reported.");
console.log("Conversion provenance/loss gate: PASS");
