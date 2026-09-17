const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');

test('seed database has core R&D collections',()=>{
  const d=JSON.parse(fs.readFileSync(path.join(__dirname,'..','data','db.json'),'utf8'));
  for(const k of ['projects','research','hypotheses','experiments','failures','ip','audit']) assert.ok(Array.isArray(d[k]),`${k} must be an array`);
});

test('research object follows Biupiu lifecycle identifiers',()=>{
  const d=JSON.parse(fs.readFileSync(path.join(__dirname,'..','data','db.json'),'utf8'));
  assert.match(d.research[0].id,/^RES-/);
  assert.match(d.research[0].maturity,/^R[0-9]$/);
});
