const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');

const ROOT = __dirname;
const DATA = path.join(ROOT, 'data', 'db.json');
const PUBLIC = path.join(ROOT, 'public');
fs.mkdirSync(path.dirname(DATA), { recursive: true });
if (!fs.existsSync(DATA)) fs.writeFileSync(DATA, JSON.stringify({projects:[],research:[],hypotheses:[],experiments:[],failures:[],ip:[],audit:[]}, null, 2));

function db(){ return JSON.parse(fs.readFileSync(DATA,'utf8')); }
function save(x){ fs.writeFileSync(DATA, JSON.stringify(x,null,2)); }
function id(prefix){ return `${prefix}-${new Date().toISOString().slice(0,10).replaceAll('-','')}-${crypto.randomBytes(3).toString('hex').toUpperCase()}`; }
function send(res,status,type,body){ res.writeHead(status,{'Content-Type':type}); res.end(body); }
function json(res,status,obj){ send(res,status,'application/json; charset=utf-8',JSON.stringify(obj)); }
function audit(d,action,entity,entityId){ d.audit.push({id:id('AUD'),timestamp:new Date().toISOString(),action,entity,entityId}); }
function readBody(req){ return new Promise((resolve,reject)=>{let b='';req.on('data',c=>b+=c);req.on('end',()=>{try{resolve(b?JSON.parse(b):{})}catch(e){reject(e)}});}); }

const collections = {projects:'PRJ',research:'RES',hypotheses:'HYP',experiments:'EXP',failures:'FAIL',ip:'IP'};
const server = http.createServer(async (req,res)=>{
  try {
    const url = new URL(req.url, 'http://localhost');
    if(req.method==='GET' && url.pathname==='/api/health') return json(res,200,{ok:true,service:'Biupiu R&D OS',version:'0.1.0'});
    if(req.method==='GET' && url.pathname==='/api/dashboard') { const d=db(); return json(res,200,{projects:d.projects.length,research:d.research.length,hypotheses:d.hypotheses.length,experiments:d.experiments.length,failures:d.failures.length,ip:d.ip.length,audit:d.audit.length}); }
    if(req.method==='GET' && url.pathname==='/api/search') { const q=(url.searchParams.get('q')||'').toLowerCase(); const d=db(); const out=[]; for(const [c,arr] of Object.entries(d)){ if(!Array.isArray(arr)) continue; for(const x of arr) if(JSON.stringify(x).toLowerCase().includes(q)) out.push({...x,_collection:c}); } return json(res,200,out.slice(0,100)); }
    const m=url.pathname.match(/^\/api\/(projects|research|hypotheses|experiments|failures|ip)$/);
    if(m && req.method==='GET') return json(res,200,db()[m[1]]);
    if(m && req.method==='POST') { const d=db(), c=m[1], body=await readBody(req); const record={id:id(collections[c]),createdAt:new Date().toISOString(),updatedAt:new Date().toISOString(),...body}; d[c].push(record); audit(d,'CREATE',c,record.id); save(d); return json(res,201,record); }
    if(req.method==='GET' && url.pathname==='/api/graph') { const d=db(); const nodes=[]; const edges=[]; for(const c of ['projects','research','hypotheses','experiments','failures','ip']) for(const x of d[c]) nodes.push({id:x.id,type:c,title:x.title||x.name||x.id}); for(const c of ['research','hypotheses','experiments','failures','ip']) for(const x of d[c]) for(const key of ['projectId','researchId','hypothesisId','experimentId']) if(x[key]) edges.push({from:x.id,to:x[key],type:key}); return json(res,200,{nodes,edges}); }
    if(req.method==='GET') { let file=url.pathname==='/'?'/index.html':url.pathname; const fp=path.normalize(path.join(PUBLIC,file)); if(!fp.startsWith(PUBLIC)) return send(res,403,'text/plain','Forbidden'); if(fs.existsSync(fp)&&fs.statSync(fp).isFile()){const ext=path.extname(fp);const type={'.html':'text/html; charset=utf-8','.js':'text/javascript; charset=utf-8','.css':'text/css; charset=utf-8','.json':'application/json; charset=utf-8'}[ext]||'text/plain';return send(res,200,type,fs.readFileSync(fp));} }
    return json(res,404,{error:'Not found'});
  } catch(e){ console.error(e); json(res,500,{error:e.message}); }
});
server.listen(process.env.PORT||3000,()=>console.log(`Biupiu R&D OS running on http://localhost:${process.env.PORT||3000}`));
