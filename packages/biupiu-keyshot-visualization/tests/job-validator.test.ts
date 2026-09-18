import {validateRenderJob} from "../src/job-validator";
const valid={jobId:"TEST-001",assetId:"BIUPIU-TEST",profile:"microturbine",input:{sourceFormat:"glb",sourcePath:"C:/Biupiu/test/model.glb"},output:{format:"png",width:3840,height:2160},backend:"local-keyshot"};
const a=validateRenderJob(valid);
if(!a.valid) throw new Error("valid job rejected");
const b=validateRenderJob({...valid,profile:"unknown"});
if(b.valid) throw new Error("invalid profile accepted");
const c=validateRenderJob({...valid,output:{format:"png",width:0,height:2160}});
if(c.valid) throw new Error("invalid dimensions accepted");
