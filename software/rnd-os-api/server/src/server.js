import http from "node:http";
import crypto from "node:crypto";
import Database from "better-sqlite3";

const db=new Database(process.env.DB_FILE||"biupiu-rnd-os.db");
db.exec(`
CREATE TABLE IF NOT EXISTS records(
 id TEXT PRIMARY KEY,type TEXT NOT NULL,payload TEXT NOT NULL,created_at TEXT NOT NULL,updated_at TEXT NOT NULL,
 version INTEGER NOT NULL DEFAULT 1, content_hash TEXT, updated_by TEXT
);
CREATE TABLE IF NOT EXISTS audit(
 id TEXT PRIMARY KEY,actor_id TEXT NOT NULL,action TEXT NOT NULL,ref TEXT NOT NULL,at TEXT NOT NULL,details TEXT
);
`);
const now=()=>new Date().toISOString();
const uid=p=>p+"-"+crypto.randomUUID().slice(0,8).toUpperCase();
function audit(actor,action,ref,details={}){db.prepare("INSERT INTO audit VALUES(?,?,?,?,?,?)").run(uid("AUD"),actor,action,ref,now(),JSON.stringify(details))}
function json(res,status,data){res.writeHead(status,{"content-type":"application/json"});res.end(JSON.stringify(data))}
function body(req){return new Promise((resolve,reject)=>{let s="";req.on("data",c=>{s+=c});req.on("end",()=>{try{resolve(s?JSON.parse(s):{})}catch(e){reject(e)}});req.on("error",reject)})}
function auth(req){return req.headers["x-biupiu-role"]||"VIEWER"}
function allowed(role,needed){const order={VIEWER:0,RESEARCHER:1,REVIEWER:2,ADMIN:3};return (order[role]??-1)>=(order[needed]??99)}

import { createHash } from "node:crypto";
const hashPayload=p=>createHash("sha256").update(JSON.stringify(p)).digest("hex");
function recordRows(type){return db.prepare("SELECT * FROM records WHERE type=? ORDER BY created_at DESC").all(type)}
function getRecord(id){return db.prepare("SELECT * FROM records WHERE id=?").get(id)}
function revisions(id){
 const r=getRecord(id); if(!r)return null;
 return [{entity_id:r.id,version:r.version,content_hash:r.content_hash,updated_at:r.updated_at,updated_by:r.updated_by}];
}

const server=http.createServer(async(req,res)=>{
 try{
  const path=req.url.split("?")[0],role=auth(req),actor=req.headers["x-biupiu-actor"]||"local-test";
  if(req.method==="GET"&&path==="/health")return json(res,200,{status:"ok",service:"biupiu-rnd-os-api",version:"0.1.0"});
  if(req.method==="GET"&&path==="/v1/audit")return json(res,200,db.prepare("SELECT * FROM audit ORDER BY at DESC LIMIT 500").all());
  const match=path.match(/^\/v1\/(research|experiments|assets)(?:\/([^/]+)\/gate)?$/);
  if(match){
   const typeMap={research:"research",experiments:"experiment",assets:"asset"};
   const type=typeMap[match[1]],id=match[2];
   if(req.method==="GET"&&type!=="experiments")return json(res,200,db.prepare("SELECT * FROM records WHERE type=? ORDER BY created_at DESC").all(type));
   if(req.method==="GET"&&type==="experiments")return json(res,200,db.prepare("SELECT * FROM records WHERE type=? ORDER BY created_at DESC").all("experiment"));
   if(req.method==="POST"&&id&&path.endsWith("/gate")){
    if(!allowed(role,"REVIEWER"))return json(res,403,{error:"reviewer_role_required"});
    const b=await body(req),r=db.prepare("SELECT * FROM records WHERE id=?").get(id);
    if(!r)return json(res,404,{error:"not_found"});
    const p=JSON.parse(r.payload),from=p.status||"DRAFT",to=b.status;
    const gates=["DRAFT","REVIEW","TESTNET","VERIFIED","RELEASED"];
    if(!gates.includes(to))return json(res,400,{error:"invalid_gate"});
    if(to==="RELEASED"&&!allowed(role,"ADMIN"))return json(res,403,{error:"admin_required_for_release"});
    p.status=to;p.updated_at=now();db.prepare("UPDATE records SET payload=?,updated_at=? WHERE id=?").run(JSON.stringify(p),p.updated_at,id);
    audit(actor,"GATE_TRANSITION",id,{from,to});return json(res,200,p);
   }
   if(req.method==="POST"){
    if(!allowed(role,"RESEARCHER"))return json(res,403,{error:"researcher_role_required"});
    const b=await body(req),rid=uid(type==="research"?"RES":type==="experiment"?"EXP":"AST"),t=type==="research"?"research":type==="experiments"?"experiment":"asset",ts=now();
    b.id=rid;b.created_at=ts;b.updated_at=ts;if(!b.status)b.status=t==="asset"?"DRAFT":"LOGGED";
    db.prepare("INSERT INTO records (id,type,payload,created_at,updated_at,version,content_hash,updated_by) VALUES(?,?,?,?,?,?,?,?)").run(rid,t,JSON.stringify(b),ts,ts,1,hashPayload(b),actor);audit(actor,"CREATE_"+t.toUpperCase(),rid);return json(res,201,b);
   }
  }
  json(res,404,{error:"not_found"});
 }catch(e){json(res,400,{error:"request_failed",message:e.message})}
});
if(process.env.NODE_ENV!=="test")server.listen(process.env.PORT||8787);
export {server,db};