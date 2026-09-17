const test = require('node:test');
const assert = require('node:assert/strict');
const { exportPackage, importPackage } = require('../lib/package');
const { can, validRole, issueToken } = require('../lib/auth');

test('research packages round-trip with checksum', () => {
  const db = { projects: [{ id: 'P1' }], research: [{ id: 'R1' }] };
  const pkg = exportPackage(db);
  assert.equal(pkg.format, 'biupiu-rnd-package');
  assert.deepEqual(importPackage(pkg), db);
  pkg.data.projects[0].id = 'TAMPERED';
  assert.throws(() => importPackage(pkg), /checksum/);
});

test('role hierarchy and token issuance are deterministic in shape', () => {
  assert.equal(validRole('researcher'), true);
  assert.equal(validRole('unknown'), false);
  assert.equal(can('admin', 'researcher'), true);
  assert.equal(can('viewer', 'admin'), false);
  const token = issueToken({ id: 'U1', organisationId: 'O1' });
  assert.match(token.token, /^[a-f0-9]{48}$/);
  assert.equal(token.tokenHash.length, 64);
});
