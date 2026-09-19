import test from "node:test";
import assert from "node:assert/strict";
process.env.NODE_ENV="test";
const {server}=await import("../src/server.js");
const port=18987;await new Promise(r=>server.listen(port,r));
const req=(method,path,body,role="RESEARCHER")=>fetch("http://127.0.0.1:"+port+path,{method,headers:{"content-type":"application/json","x-biupiu-role":role,"x-biupiu-actor":"test-user"},body:body?JSON.stringify(body):undefined});
test("health",async()=>{const r=await req("GET","/health");assert.equal(r.status,200)});
test("research creation and audit",async()=>{const r=await req("POST","/v1/research",{title:"Test",evidence_class:"HYPOTHESIS"});assert.equal(r.status,201);const a=await req("GET","/v1/audit",null);assert.equal(a.status,200);const j=await a.json();assert.ok(j.length>0)});
test("release requires admin",async()=>{const r=await req("POST","/v1/assets",{name:"Test Asset"});const a=await r.json();const x=await req("POST","/v1/assets/"+a.id+"/gate",{status:"RELEASED"},"REVIEWER");assert.equal(x.status,403)});
test.after(()=>server.close());
test("stale update returns version conflict",async()=>{
 const created=await req("POST","/v1/research",{title:"Concurrent",evidence_class:"EXPERIMENTAL"});
 const x=await created.json();
 const a=await req("POST","/v1/records/"+x.id+"/sync",{base_version:1,operation_id:"OP-1",payload:{title:"v2"}});
 assert.equal(a.status,200);
 const stale=await req("POST","/v1/records/"+x.id+"/sync",{base_version:1,operation_id:"OP-2",payload:{title:"stale"}});
 assert.equal(stale.status,409);
 const body=await stale.json(); assert.equal(body.error,"VERSION_CONFLICT"); assert.equal(body.server_version,2);
});
test("conflict resolution is reviewer-controlled",async()=>{
 const created=await req("POST","/v1/assets",{name:"Conflict Asset"});
 const x=await created.json();
 const r=await req("POST","/v1/records/"+x.id+"/conflicts/resolve",{operation_id:"OP-3",strategy:"MANUAL_MERGE"},"REVIEWER");
 assert.equal(r.status,200);
});
