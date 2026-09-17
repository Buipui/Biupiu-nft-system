const test = require('node:test');
const assert = require('node:assert/strict');
const { spawn } = require('node:child_process');
const path = require('node:path');
const { read, write } = require('../lib/store');
const { issueToken } = require('../lib/auth');

async function request(base, route, options={}) {
  const res = await fetch(base + route, options);
  return { status: res.status, body: await res.json() };
}

function waitForServer(child) {
  return new Promise((resolve,reject)=>{
    let settled=false;
    const timer=setTimeout(()=>{if(!settled){settled=true;resolve()}},500);
    child.once('error',e=>{if(!settled){settled=true;clearTimeout(timer);reject(e)}});
  });
}

test('protected API rejects unauthenticated access while health remains public', async () => {
  const port=3400+Math.floor(Math.random()*100);
  const child=spawn(process.execPath,['server.js'],{cwd:path.join(__dirname,'..'),env:{...process.env,PORT:String(port)}});
  try {
    await waitForServer(child);
    const base='http://127.0.0.1:'+port;
    assert.equal((await request(base,'/api/health')).status,200);
    assert.equal((await request(base,'/api/projects')).status,401);
  } finally { child.kill(); }
});

test('authenticated user can read only its organisation', async () => {
  const original=read();
  try {
    const db=read();
    db.organisations=[{id:'ORG-TEST-A'},{id:'ORG-TEST-B'}];
    db.users=[
      {id:'USER-TEST-A',organisationId:'ORG-TEST-A',role:'owner'}
    ];
    db.sessions=[];
    const session=issueToken(db.users[0]);
    db.sessions.push({id:'SESSION-TEST-A',userId:'USER-TEST-A',organisationId:'ORG-TEST-A',tokenHash:session.tokenHash,expiresAt:session.expiresAt});
    db.projects=[
      {id:'P-A',organisationId:'ORG-TEST-A',title:'Visible'},
      {id:'P-B',organisationId:'ORG-TEST-B',title:'Hidden'}
    ];
    write(db);
    const port=3500+Math.floor(Math.random()*100);
    const child=spawn(process.execPath,['server.js'],{cwd:path.join(__dirname,'..'),env:{...process.env,PORT:String(port)}});
    try {
      await waitForServer(child);
      const result=await request('http://127.0.0.1:'+port,'/api/projects',{headers:{Authorization:'Bearer '+session.token}});
      assert.equal(result.status,200);
      assert.deepEqual(result.body.map(x=>x.id),['P-A']);
    } finally { child.kill(); }
  } finally {
    write(original);
  }
});
