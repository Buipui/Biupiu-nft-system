const test = require('node:test');
const assert = require('node:assert/strict');
const { routePolicy } = require('../lib/api-gate');

test('health and metadata routes are public', () => {
  assert.deepEqual(routePolicy('/api/health','GET'), { public: true });
  assert.deepEqual(routePolicy('/api/meta','GET'), { public: true });
});

test('read routes require viewer role', () => {
  assert.deepEqual(routePolicy('/api/research','GET'), { role: 'viewer' });
  assert.deepEqual(routePolicy('/api/dashboard','GET'), { role: 'viewer' });
});

test('mutating routes require researcher role', () => {
  assert.deepEqual(routePolicy('/api/research','POST'), { role: 'researcher' });
  assert.deepEqual(routePolicy('/api/relationships','POST'), { role: 'researcher' });
});
