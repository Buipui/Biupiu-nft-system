import { createProvenance, validateReleaseProvenance } from "./src/provenance";
const p=createProvenance({jobId:"job-1",sourceAssetIds:["asset-1"],sourceModelVersion:"v1",provider:"BLENDER",providerJobId:"provider-1"});
const conversion={sourceFormat:"GLTF",targetFormat:"USD",provider:"BLENDER",status:"READY",unsupportedFeatures:[],warnings:[]};
const withConversion={...p,conversions:[conversion]};
validateReleaseProvenance(withConversion,{outputHash:"sha256:test",sourceAssetIds:["asset-1"],sourceModelVersion:"v1",provider:"BLENDER",providerJobId:"provider-1",conversions:[conversion],humanApproved:true});
let blocked=false;
try { validateReleaseProvenance(withConversion,{outputHash:"",sourceAssetIds:["asset-1"],sourceModelVersion:"v1",provider:"BLENDER",providerJobId:"provider-1",conversions:[conversion],humanApproved:true}); } catch { blocked=true; }
if(!blocked) throw new Error("Missing output hash was not blocked.");
blocked=false;
try { validateReleaseProvenance(withConversion,{outputHash:"sha256:test",sourceAssetIds:["asset-1"],sourceModelVersion:"v1",provider:"BLENDER",providerJobId:"provider-1",conversions:[conversion],humanApproved:false}); } catch { blocked=true; }
if(!blocked) throw new Error("Unapproved release was not blocked.");
console.log("Release provenance gate: PASS");
