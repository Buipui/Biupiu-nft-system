import { authorizeRelease } from "./release-gate";
const provenance={jobId:"j1",sourceAssetIds:["a1"],sourceModelVersion:"v1",provider:"BLENDER",providerJobId:"p1",createdAt:"now",conversions:[{sourceFormat:"GLTF",targetFormat:"USD",provider:"BLENDER",status:"READY",unsupportedFeatures:[],warnings:[]}]};
const requirements={outputHash:"sha256:x",sourceAssetIds:["a1"],sourceModelVersion:"v1",provider:"BLENDER",providerJobId:"p1",conversions:provenance.conversions,humanApproved:true};
authorizeRelease({assetId:"a1",destination:"SHOWCASE",provenance,requirements});
authorizeRelease({assetId:"a1",destination:"NFT_STUDIO",provenance,requirements});
let blocked=false; try{authorizeRelease({assetId:"a1",destination:"NFT_STUDIO",provenance,requirements:{...requirements,humanApproved:false}})}catch{blocked=true}
if(!blocked) throw new Error("Unapproved release was not blocked.");
console.log("Release boundary gate: PASS");
