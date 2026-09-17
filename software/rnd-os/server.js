const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const { validateResearchObject, EVIDENCE_STATES, MATURITY, lifecycleTransition } = require('./lib/domain');
const { read: readDb, write: writeDb } = require('./lib/store');
const { exportPackage, importPackage } = require('./lib/package');
const { enforceApiGate } = require('./lib/api-gate');
const { scopedRecords, assertWriteAccess } = require('./lib/tenant-store');
const { recordSecurityEvent } = require('./lib/request-audit');

const ROOT = __dirname; const PUBLIC = path.join(ROOT, 'public');
function db(){ return readDb(); }
function save(x){ return writeDb(x); }
function id(prefix){ return prefix+'-'+new Date().toISOString().slice(0,10).replaceAll('-','')+'-'+crypto.randomBytes(3).toString('hex').toUpperCase(); }
function send(res,status,type,body){ res.writeHead(status,{'Content-Type':type}); res.end(body); }
function json(res,status,obj){ send(res,status,'application/json; charset=utf-8',JSON.stringify(obj)); }
function audit(d,action,entity,entityId,payload={}){ d.audit ||= []; d.audit.push({id:id('AUD'),timestamp:new Date().toISOString(),action,entity,entityId,payload}); }
function readBody(req){ return new Promise((resolve,reject)=>{let b='';req.on('data',c=>b+=c);req.on('end',()=>{try{resolve(b?JSON.parse(b):{})}catch(e){reject(e)}});}); }
const collections={projects:'PRJ',research:'RES',hypotheses:'HYP',experiments:'EXP',failures:'FAIL',ip:'IP'};
const server=http.createServer(async(req,res)=>{ let principal=null; let activeDb=null; try {
const url=new URL(req.url,'http://localhost'); activeDb=db();
if(req.method==='GET'&&url.pathname==='/api/health') return json(res,200,{ok:true,service:'Biupiu R&D OS',version:'0.5.0',storage:'json-development'});
if(req.method==='GET'&&url.pathname==='/api/meta') return json(res,200,{evidenceStates:[...EVIDENCE_STATES],maturity:[...MATURITY]});
principal=enforceApiGate(req,activeDb);
if(req.method==='GET'&&url.pathname==='/api/dashboard') return json(res,200,{projects:scopedRecords(activeDb,principal,'projects').length,research:scopedRecords(activeDb,principal,'research').length,hypotheses:scopedRecords(activeDb,principal,'hypotheses').length,experiments:scopedRecords(activeDb,principal,'experiments').length,failures:scopedRecords(activeDb,principal,'failures').length,ip:scopedRecords(activeDb,principal,'ip').length,relationships:scopedRecords(activeDb,principal,'relationships').length});
if(req.method==='GET'&&url.pathname==='/api/search'){const q=(url.searchParams.get('q')||'').toLowerCase();const out=[];for(const c of ['projects','research','hypotheses','experiments','failures','ip'])for(const x of scopedRecords(activeDb,principal,c))if(JSON.stringify(x).toLowerCase().includes(q))out.push({...x,_collection:c});return json(res,200,out.slice(0,100));}
if(req.method==='GET'&&url.pathname==='/api/graph'){const nodes=[];const edges=[];for(const c of ['projects','research','hypotheses','experiments','failures','ip'])for(const x of scopedRecords(activeDb,principal,c))nodes.push({id:x.id,type:c,title:x.title||x.name||x.id});const allowed=new Set(nodes.map(x=>x.id));for(const r of scopedRecords(activeDb,principal,'relationships'))if(allowed.has(r.from)&&allowed.has(r.to))edges.push({from:r.from,to:r.to,type:r.type});return json(res,200,{nodes,edges});}
const lineage=url.pathname.match(/^\/api\/research\/([^/]+)\/lineage$/);
if(req.method==='GET'&&lineage){const item=(activeDb.research||[]).find(x=>x.id===lineage[1]&&x.organisationId===principal.organisationId);if(!item)return json(res,404,{error:'research object not found'});return json(res,200,{research:[item],relationships:(activeDb.relationships||[]).filter(r=>r.organisationId===principal.organisationId&&(r.from===item.id||r.to===item.id))});}
if(req.method==='GET'&&url.pathname==='/api/package/export')return json(res,200,exportPackage(activeDb));
if(req.method==='POST'&&url.pathname==='/api/package/import'){assertWriteAccess(principal);const imported=importPackage(await readBody(req));return json(res,200,{ok:true,collections:Object.fromEntries(Object.entries(imported).map(([k,v])=>[k,Array.isArray(v)?v.length:undefined]))});}
if(url.pathname==='/api/relationships'&&req.method==='GET')return json(res,200,scopedRecords(activeDb,principal,'relationships'));
if(url.pathname==='/api/relationships'&&req.method==='POST'){assertWriteAccess(principal);const body=await readBody(req);if(!body.from||!body.to||!body.type)return json(res,400,{error:'from, to and type are required'});const all=['projects','research','hypotheses','experiments','failures','ip'].flatMap(c=>activeDb[c]||[]);const from=all.find(x=>x.id===body.from),to=all.find(x=>x.id===body.to);if(!from||!to||from.organisationId!==principal.organisationId||to.organisationId!==principal.organisationId)return json(res,403,{error:'relationship endpoints must share organisation scope'});activeDb.relationships ||= [];const record={id:id('REL'),createdAt:new Date().toISOString(),organisationId:principal.organisationId,...body};activeDb.relationships.push(record);audit(activeDb,'CREATE','relationships',record.id,{organisationId:principal.organisationId,userId:principal.id});save(activeDb);return json(res,201,record);}
const transition=url.pathname.match(/^\/api\/research\/([^/]+)\/transition$/);
if(transition&&req.method==='POST'){assertWriteAccess(principal);const item=(activeDb.research||[]).find(x=>x.id===transition[1]&&x.organisationId===principal.organisationId);if(!item)return json(res,404,{error:'research object not found'});const body=await readBody(req);if(!lifecycleTransition(body.from||item.lifecycleStage||'SOURCE',body.to))return json(res,400,{error:'invalid lifecycle transition'});item.lifecycleStage=body.to;item.updatedAt=new Date().toISOString();audit(activeDb,'TRANSITION','research',item.id,{from:body.from||null,to:body.to,organisationId:principal.organisationId,userId:principal.id});save(activeDb);return json(res,200,item);}
const m=url.pathname.match(/^\/api\/(projects|research|hypotheses|experiments|failures|ip)$/);
if(m&&req.method==='GET')return json(res,200,scopedRecords(activeDb,principal,m[1]));
if(m&&req.method==='POST'){assertWriteAccess(principal);const c=m[1],body=await readBody(req);if(c==='research'){const errors=validateResearchObject(body);if(errors.length)return json(res,400,{errors});}activeDb[c] ||= [];const record={id:id(collections[c]),createdAt:new Date().toISOString(),updatedAt:new Date().toISOString(),organisationId:principal.organisationId,...body};delete record.organisation_id;activeDb[c].push(record);audit(activeDb,'CREATE',c,record.id,{organisationId:principal.organisationId,userId:principal.id});save(activeDb);return json(res,201,record);}
if(req.method==='GET'){let file=url.pathname==='/'?'/index.html':url.pathname;const fp=path.normalize(path.join(PUBLIC,file));if(!fp.startsWith(PUBLIC))return send(res,403,'text/plain','Forbidden');if(fs.existsSync(fp)&&fs.statSync(fp).isFile()){const ext=path.extname(fp);const type={'.html':'text/html; charset=utf-8','.js':'text/javascript; charset=utf-8','.css':'text/css; charset=utf-8','.json':'application/json; charset=utf-8'}[ext]||'text/plain';return send(res,200,type,fs.readFileSync(fp));}}
return json(res,404,{error:'Not found'});
}catch(e){const status=e.statusCode||500;if(activeDb&&principal){recordSecurityEvent(activeDb,{method:req.method,path:req.url,userId:principal.id,organisationId:principal.organisationId,outcome:'denied'});writeDb(activeDb);}return json(res,status,{error:e.message});}});
server.listen(process.env.PORT||3000,()=>console.log('Biupiu R&D OS running on http://localhost:'+ (process.env.PORT||3000)));