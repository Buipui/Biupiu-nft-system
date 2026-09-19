export const GATES=Object.freeze(["DRAFT","REVIEW","TESTNET","VERIFIED","RELEASED"]);
export const CONFLICT_STRATEGIES=Object.freeze(["USE_SERVER","SAVE_LOCAL_REVISION","MANUAL_MERGE"]);
export function validGateTransition(from,to){
  const i=GATES.indexOf(from),j=GATES.indexOf(to);
  return i>=0&&j>=0&&j>=i;
}
export function validConflictStrategy(strategy){
  return CONFLICT_STRATEGIES.includes(strategy);
}