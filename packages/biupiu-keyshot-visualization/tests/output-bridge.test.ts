import {registerRenderOutput} from "../src/output-bridge";
const result=registerRenderOutput({jobId:"TEST-OUT-001",assetId:"BIUPIU-TEST",profile:"microturbine",outputPath:"renders/TEST-OUT-001.png",format:"png",width:3840,height:2160,backend:"local-keyshot",provenance:{sourcePath:"models/test.glb"},status:"completed",createdAt:"2026-09-19T00:00:00Z"},{showcaseAssetId:"SHOW-001",digitalTwinAssetId:"DT-001",showreelProjectId:"REEL-001"});
if(result.links.showcaseAssetId!=="SHOW-001") throw new Error("Showcase link failed");
if(result.assetId!=="BIUPIU-TEST") throw new Error("Asset identity was not preserved");
