const test = require('node:test');
const assert = require('node:assert/strict');
const { validateResearchObject, lifecycleTransition } = require('../lib/domain');

test('relationship and lifecycle rules reject backwards transitions', () => {
  assert.equal(lifecycleTransition('HYPOTHESIS', 'EXPERIMENT'), true);
  assert.equal(lifecycleTransition('VALIDATION', 'MODEL'), false);
});

test('research objects use evidence-aware validation', () => {
  assert.deepEqual(validateResearchObject({ id: 'RES-1', title: 'X', evidence_state: 'SPECULATIVE', maturity: 'R3' }), []);
  assert.deepEqual(validateResearchObject({ id: 'RES-1', title: 'X', evidence_state: 'UNKNOWN' }), ['invalid evidence_state']);
});
