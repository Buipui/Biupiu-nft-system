const EVIDENCE_STATES = new Set([
  'ESTABLISHED','SUPPORTED','PRELIMINARY','HYPOTHESIS','SPECULATIVE','CONTRADICTED','INCONCLUSIVE'
]);
const MATURITY = new Set(Array.from({length:10}, (_,i)=>`R${i}`));

function validateResearchObject(input) {
  const errors = [];
  if (!input || typeof input !== 'object') return ['object is required'];
  if (!input.id) errors.push('id is required');
  if (!input.title) errors.push('title is required');
  if (input.evidence_state && !EVIDENCE_STATES.has(input.evidence_state)) errors.push('invalid evidence_state');
  if (input.maturity && !MATURITY.has(input.maturity)) errors.push('invalid maturity');
  return errors;
}

function lifecycleTransition(from, to) {
  const order = ['SOURCE','CLAIM','HYPOTHESIS','MODEL','SIMULATION','EXPERIMENT','MEASUREMENT','VALIDATION','REPLICATION','IP','PROTOTYPE','PRODUCT'];
  const a = order.indexOf(from), b = order.indexOf(to);
  return a >= 0 && b >= 0 && b >= a;
}

module.exports = { EVIDENCE_STATES, MATURITY, validateResearchObject, lifecycleTransition };
