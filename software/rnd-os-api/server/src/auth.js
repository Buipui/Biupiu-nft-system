// Gate 06 development auth adapter.
// Production must replace this with OIDC/OAuth2/JWT verification.
// Never trust client-supplied role headers outside isolated development.
export const ROLES=Object.freeze({VIEWER:0,RESEARCHER:1,REVIEWER:2,ADMIN:3});
export function requireRole(role,minimum){return (ROLES[role]??-1)>=(ROLES[minimum]??99)}
export function developmentIdentity(req){
  return {actor_id:req.headers["x-biupiu-actor"]||"local-test",role:req.headers["x-biupiu-role"]||"VIEWER"};
}