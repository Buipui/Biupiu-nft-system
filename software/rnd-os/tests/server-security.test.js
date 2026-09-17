const test = require('node:test');
const assert = require('node:assert/strict');
const { spawn } = require('node:child_process');

async function request(base, path, options={}) {
  const res = await fetch(base + path, options);
  return { status: res.status, body: await res.json() };
}

test('protected API rejects unauthenticated access while public health remains available', async () => {
  const port = 3300 + Math.floor(Math.random() * 100);
  const child = spawn(process.execPath, ['server.js'], { cwd: require('node:path').join(__dirname, '..'), env:{...process.env,PORT:String(port)} });
  try {
    await new Promise((resolve,reject)=>{ const t=setTimeout(resolve,300); child.once('error',reject); });
    const base='http://127.0.0.1:'+port;
    const health=await request(base,'/api/health');
    assert.equal(health.status,200);
    const projects=await request(base,'/api/projects');
    assert.equal(projects.status,401);
  } finally {
    child.kill();
  }
});
