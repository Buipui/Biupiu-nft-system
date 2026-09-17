async function api(path,opts){const r=await fetch(path,opts);return r.json()}
function card(label,value){return `<div class="card"><small>${label}</small><strong>${value}</strong></div>`}
async function load(){const d=await api('/api/dashboard');document.querySelector('#cards').innerHTML=Object.entries(d).map(([k,v])=>card(k,v)).join('');const rows=await api('/api/research');render(rows)}
function render(rows){document.querySelector('#research').innerHTML=rows.map(x=>`<tr><td>${x.id}</td><td><b>${x.title}</b><br><small>${x.description||''}</small></td><td><span class="tag">${x.evidenceState||'UNSET'}</span></td><td>${x.maturity||'R0'}</td></tr>`).join('')}
document.querySelector('#search').addEventListener('input',async e=>render(await api('/api/search?q='+encodeURIComponent(e.target.value))));
for(const [id,path] of [['experiment','/api/experiments'],['hypothesis','/api/hypotheses']]) document.querySelector('#'+id).addEventListener('submit',async e=>{e.preventDefault();const body=Object.fromEntries(new FormData(e.target));await api(path,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});e.target.reset();load()});
load();
