// Production adapter contract. A real deployment must inject an OIDC/JWT verifier.
// This reference intentionally fails closed when a production verifier is absent.
export function verifyAuthenticatedSession(req, verifier){
  if(typeof verifier!=="function") return {authenticated:false,error:"AUTH_VERIFIER_NOT_CONFIGURED"};
  try{
    const result=verifier(req);
    return result?.actorId&&result?.role
      ? {authenticated:true,...result}
      : {authenticated:false,error:"INVALID_SESSION"};
  }catch{ return {authenticated:false,error:"INVALID_SESSION"}; }
}