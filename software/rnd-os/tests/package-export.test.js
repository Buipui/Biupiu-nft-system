const test = require('node:test');
const assert = require('node:assert/strict');
const { exportPackage } = require('../lib/package');

function scopedPackage(db,user) {
  const collections=['projects','research','hypotheses','experiments','failures','ip','relationships','evidence'];
  const out={...db};
  for (const c of collections) out[c]=(db[c]||[]).filter(x=>x.organisationId===user.organisationId);
  out.audit=(db.audit||[]).filter(x=>x.payload?.organisationId===user.organisationId);
  out.sessions=[]; out.users=[]; out.organisations=[];
  return out;
}

test('tenant package export contains only authenticated organisation data', () => {
  const db={
    projects:[{id:'P-A',organisationId:'ORG-A'},{id:'P-B',organisationId:'ORG-B'}],
    research:[{id:'R-A',organisationId:'ORG-A'},{id:'R-B',organisationId:'ORG-B'}],
    relationships:[{id:'REL-A',organisationId:'ORG-A'},{id:'REL-B',organisationId:'ORG-B'}],
    audit:[{id:'AUD-A',payload:{organisationId:'ORG-A'}},{id:'AUD-B',payload:{organisationId:'ORG-B'}}],
    sessions:[{id:'S-A'}],users:[{id:'U-A'}],organisations:[{id:'ORG-A'},{id:'ORG-B'}]
  };
  const pkg=exportPackage(scopedPackage(db,{organisationId:'ORG-A'}));
  assert.deepEqual(pkg.data.projects.map(x=>x.id),['P-A']);
  assert.deepEqual(pkg.data.research.map(x=>x.id),['R-A']);
  assert.deepEqual(pkg.data.relationships.map(x=>x.id),['REL-A']);
  assert.deepEqual(pkg.data.audit.map(x=>x.id),['AUD-A']);
  assert.deepEqual(pkg.data.sessions,[]);
  assert.deepEqual(pkg.data.users,[]);
  assert.deepEqual(pkg.data.organisations,[]);
});
