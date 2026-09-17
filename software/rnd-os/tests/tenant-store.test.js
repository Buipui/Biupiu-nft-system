const test = require('node:test');
const assert = require('node:assert/strict');
const { scopedRecords, assertRecordAccess, assertWriteAccess } = require('../lib/tenant-store');

const user = { id: 'U1', organisationId: 'ORG-A', role: 'researcher' };
const records = [
  { id: 'R1', organisationId: 'ORG-A' },
  { id: 'R2', organisationId: 'ORG-B' }
];

test('tenant store only returns records in the authenticated organisation', () => {
  const db = { research: records };
  assert.deepEqual(scopedRecords(db, user, 'research'), [records[0]]);
});

test('tenant store rejects cross-organisation access', () => {
  assert.throws(() => assertRecordAccess(user, records[1]), /organisation scope violation/);
});

test('researcher has write access', () => {
  assert.equal(assertWriteAccess(user), true);
});

test('viewer does not have write access', () => {
  assert.throws(() => assertWriteAccess({ ...user, role: 'viewer' }), /insufficient role/);
});
