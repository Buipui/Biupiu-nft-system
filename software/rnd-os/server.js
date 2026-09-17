const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const { validateResearchObject, EVIDENCE_STATES, MATURITY, lifecycleTransition } = require('./lib/domain');
const { read: readDb, write: writeDb } = require('./lib/store');
const { exportPackage, importPackage } = require('./lib/package');

const ROOT = __dirname;
const PUBLIC = path.join(ROOT, 'public');
function db(){ return readDb(); }
function save(x){ return writeDb(x); }
function id(prefix){ return `${prefix}-${new Date().toISOString().slice(0,10).replaceAll('-','')}-${crypto.randomBytes(3).toString('hex').toUpperCase()}`; }
function send(res,status,type,body){ res.writeHead(status,{'Content-Type':type}); res.end(body); }
function json(res,status,obj){ send(res,status,'application/json; charset=utf-8',JSON.stringify(obj)); }
function audit(d,action,entity,entityId,payload={}){ d.audit ||= []; d.audit.push({id:id('AUD'),timestamp:new Date().toISOString(),action,entity,entityId,payload}); }
function readBody(req){ return new Promise((resolve,reject)=>{let b='';req.on('data',c=>b+=c);req.on('end',()=>{try{resolve(b?JSON.parse(b):{})}catch(e){reject(e)}});}); }
const collections = {projects:'PRJ',research:'RES',hypotheses:'HYP',experiments:'EXP',failures:'FAIL',ip:'IP'};
const server = http.createServer(async (req,res)=>{
  try {
    const url = new URL(req.url, 'http://localhost');
    if(req.method==='GET' && url.pathname==='/api/health') return json(res,200,{ok:true,service:'Biupiu R&D OS',version:'0.2.0',storage:'json-development'});
    if(req.method==='GET' && url.pathname==='/api/meta') return json(res,200,{evidenceStates:[...EVIDENCE_STATES],maturity:[...MATURITY]});
    if(req.method==='GET' && url.pathname==='/api/dashboard') { const d=db(); return json(res,200,{projects:(d.projects||[]).length,research:(d.research||[]).length,hypotheses:(d.hypotheses||[]).length,experiments:(d.experiments||[]).length,failures:(d.failures||[]).length,ip:(d.ip||[]).length,relationships:(d.relationships||[]).length,audit:(d.audit||[]).length}); }
    if(req.method==='GET' && url.pathname==='/api/search') { const q=(url.searchParams.get('q')||'').toLowerCase(); const d=db(); const out=[]; for(const [c,arr] of Object.entries(d)){ if(!Array.isArray(arr)) continue; for(const x of arr) if(JSON.stringify(x).toLowerCase().includes(q)) out.push({...x,_collection:c}); } return json(res,200,out.slice(0,100)); }
    if(req.method==='GET' && url.pathname==='/api/graph') { const d=db(); const nodes=[]; const edges=[]; for(const c of ['projects','research','hypotheses','experiments','failures','ip']) for(const x of (d[c]||[])) nodes.push({id:x.id,type:c,title:x.title||x.name||x.id}); for(const r of (d.relationships||[])) edges.push({from:r.from,to:r.to,type:r.type}); for(const c of ['research','hypotheses','experiments','failures','ip']) for(const x of (d[c]||[])) for(const key of ['projectId','researchId','hypothesisId','experimentId']) if(x[key]) edges.push({from:x.id,to:x[key],type:key}); return json(res,200,{nodes,edges}); }
    const lineage=url.pathname.match(/^\/api\/research\/([^/]+)\/lineage$/);
    if(req.method==='GET' && lineage){ const d=db(); const target=lineage[1]; const objects=(d.research||[]).filter(x=>x.id===target); const related=(d.relationships||[]).filter(r=>r.from===target||r.to===target); return json(res,200,{research:objects,relationships:related}); }
    if(req.method==='GET' && url.pathname==='/api/package/export') return json(res,200,exportPackage(db()));
    if(req.method==='POST' && url.pathname==='/api/package/import') { const pkg=await readBody(req); const imported=importPackage(pkg); return json(res,200,{ok:true,collections:Object.fromEntries(Object.entries(imported).map(([k,v])=>[k,Array.isArray(v)?v.length:undefined]))}); }
    const rel=url.pathname==='/api/relationships';
    if(rel && req.method==='GET') return json(res,200,db().relationships||[]);
    if(rel && req.method==='POST') { const d=db(); d.relationships ||= []; const body=await readBody(req); if(!body.from||!body.to||!body.type) return json(res,400,{error:'from, to and type are required'}); const record={id:id('REL'),createdAt:new Date().toISOString(),...body}; d.relationships.push(record); audit(d,'CREATE','relationships',record.id); save(d); return json(res,201,record); }
    const transition=url.pathname.match(/^\/api\/research\/([^/]+)\/transition$/);
    if(transition && req.method==='POST') { const d=db(); const body=await readBody(req); const item=(d.research||[]).find(x=>x.id===transition[1]); if(!item) return json(res,404,{error:'research object not found'}); if(!lifecycleTransition(body.from||item.lifecycleStage||'SOURCE',body.to)) return json(res,400,{error:'invalid lifecycle transition'}); item.lifecycleStage=body.to; item.updatedAt=new Date().toISOString(); audit(d,'TRANSITION','research',item.id,{from:body.from||null,to:body.to}); save(d); return json(res,200,item); }
    const m=url.pathname.match(/^\/api\/(projects|research|hypotheses|experiments|failures|ip)$/);
    if(m && req.method==='GET') return json(res,200,db()[m[1]]||[]);
    if(m && req.method==='POST') { const d=db(), c=m[1], body=await readBody(req); if(c==='research'){ const errors=validateResearchObject(body); if(errors.length) return json(res,400,{errors}); } d[c] ||= []; const record={id:id(collections[c]),createdAt:new Date().toISOString(),updatedAt:new Date().toISOString(),...body}; d[c].push(record); audit(d,'CREATE',c,record.id); save(d); return json(res,201,record); }
    if(req.method==='GET') { let file=url.pathname==='/'?'/index.html':url.pathname; const fp=path.normalize(path.join(PUBLIC,file)); if(!fp.startsWith(PUBLIC)) return send(res,403,'text/plain','Forbidden'); if(fs.existsSync(fp)&&fs.statSync(fp).isFile()){const ext=path.extname(fp);const type={'.html':'text/html; charset=utf-8','.js':'text/javascript; charset=utf-8','.css':'text/css; charset=utf-8','.json':'application/json; charset=utf-8'}[ext]||'text/plain';return send(res,200,type,fs.readFileSync(fp));} }
    return json(res,404,{error:'Not found'});
  } catch(e){ console.error(e); json(res,500,{error:e.message}); }
});
server.listen(process.env.PORT||3000,()=>console.log(`Biupiu R&D OS running on http://localhost:${process.env.PORT||3000}`));
