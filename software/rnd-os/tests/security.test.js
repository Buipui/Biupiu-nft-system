const test = require('node:test');
const assert = require('node:assert/strict');
const { can, validRole, issueToken } = require('../lib/auth');
const { tenantScope, assertRole, assertTenant } = require('../lib/tenant');

test('role hierarchy is ordered', () => {
  assert.equal(can('admin','researcher'), true);
  assert.equal(can('viewer','researcher'), false);
  assert.equal(validRole('research_lead'), true);
  assert.equal(validRole('unknown'), false);
});

test('token is issued with hashed secret and organisation scope', () => {
  const session = issueToken({id:'USR-1', organisationId:'ORG-1'});
  assert.ok(session.token);
  assert.notEqual(session.token, session.tokenHash);
  assert.equal(session.organisationId, 'ORG-1');
  assert.ok(session.expiresAt);
});

test('tenant scope rejects cross-organisation records', () => {
  const user = {id:'USR-1', organisationId:'ORG-1', role:'researcher'};
  assert.equal(tenantScope(user,{organisationId:'ORG-1'}), true);
  assert.equal(tenantScope(user,{organisationId:'ORG-2'}), false);
  assert.throws(() => assertTenant(user,{organisationId:'ORG-2'}), /organisation scope violation/);
});

test('role enforcement rejects insufficient privileges', () => {
  const viewer = {role:'viewer'};
  assert.throws(() => assertRole(viewer,'researcher'), /insufficient role/);
  assert.equal(assertRole({role:'researcher'},'reviewer'), true);
});
