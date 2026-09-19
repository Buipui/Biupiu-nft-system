// Production identity-provider boundary.
// A concrete OIDC/JWT verifier and server-side role resolver are injected at deployment.
export function createOidcAdapter({verifyToken,roleResolver}){
 if(typeof verifyToken!=="function"||typeof roleResolver!=="function") throw new Error("OIDC adapter requires verifier and role resolver");
 return async function authenticate(req){
  const h=req.headers.authorization||"";
  if(!h.startsWith("Bearer ")) return {authenticated:false,error:"AUTH_REQUIRED"};
  try{
   const claims=await verifyToken(h.slice(7)),actorId=claims.sub,role=await roleResolver(actorId);
   if(!actorId||!role)return {authenticated:false,error:"FORBIDDEN"};
   return {authenticated:true,actorId,role,claims};
  }catch{return {authenticated:false,error:"AUTH_REQUIRED"}}
 }
}