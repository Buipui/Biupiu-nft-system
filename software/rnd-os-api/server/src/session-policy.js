// Production session policy contract. Token issuance/verification belongs to a
// dedicated identity provider; this module defines safe application expectations.
export const SESSION_POLICY=Object.freeze({
 accessTokenLifetimeSeconds:900,
 refreshRotation:true,
 secureCookie:true,
 sameSite:"strict",
 requireTls:true,
 noSecretsInClient:true
});
export function sessionIsUsable(session,now=Date.now()){
 return Boolean(session?.actorId && session?.expiresAt && new Date(session.expiresAt).getTime()>now);
}