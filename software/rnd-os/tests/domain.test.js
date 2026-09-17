const test = require('node:test');
const assert = require('node:assert/strict');
const { validateResearchObject, lifecycleTransition } = require('../lib/domain');

test('research object requires id and title', () => {
  assert.deepEqual(validateResearchObject({}), ['id is required','title is required']);
});

test('evidence and maturity values are validated', () => {
  assert.deepEqual(validateResearchObject({id:'RO-1',title:'Test',evidence_state:'BAD'}), ['invalid evidence_state']);
  assert.deepEqual(validateResearchObject({id:'RO-1',title:'Test',maturity:'R10'}), ['invalid maturity']);
});

test('lifecycle cannot move backwards', () => {
  assert.equal(lifecycleTransition('SOURCE','HYPOTHESIS'), true);
  assert.equal(lifecycleTransition('EXPERIMENT','CLAIM'), false);
});
