const test = require('node:test');
const assert = require('node:assert/strict');
const { read, write } = require('../lib/store');
const { exportPackage } = require('../lib/package');
const { tenantPackage } = require('../server');

test('tenant package export excludes other organisations', () => {
  const original=read();
  try {
    const db={...original,
      projects:[{id:'P-A',organisationId:'ORG-A'},{id:'P-B',organisationId:'ORG-B'}],
      research:[{id:'R-A',organisationId:'ORG-A'},{id:'R-B',organisationId:'ORG-B'}],
      relationships:[{id:'REL-A',organisationId:'ORG-A'},{id:'REL-B',organisationId:'ORG-B'}],
      audit:[{id:'AUD-A',payload:{organisationId:'ORG-A'}},{id:'AUD-B',payload:{organisationId:'ORG-B'}}]
    };
    const scoped=tenantPackage(db,{organisationId:'ORG-A'});
    const pkg=exportPackage(scoped);
    assert.deepEqual(pkg.data.projects.map(x=>x.id),['P-A']);
    assert.deepEqual(pkg.data.research.map(x=>x.id),['R-A']);
    assert.deepEqual(pkg.data.relationships.map(x=>x.id),['REL-A']);
    assert.deepEqual(pkg.data.audit.map(x=>x.id),['AUD-A']);
    assert.deepEqual(pkg.data.sessions,[]);
    assert.deepEqual(pkg.data.users,[]);
    assert.deepEqual(pkg.data.organisations,[]);
  } finally { write(original); }
});
