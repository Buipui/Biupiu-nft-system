const test = require('node:test');
const assert = require('node:assert/strict');
const { issueToken, hashToken } = require('../lib/auth');

test('development session token is stored as a hash, not raw bearer token', () => {
  const session = issueToken({ id: 'U1', organisationId: 'ORG-A', role: 'owner' });
  assert.equal(session.tokenHash, hashToken(session.token));
  assert.notEqual(session.tokenHash, session.token);
  assert.equal(session.organisationId, 'ORG-A');
  assert.ok(Date.parse(session.expiresAt) > Date.now());
});
