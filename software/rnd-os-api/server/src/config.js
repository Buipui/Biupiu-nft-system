export function loadConfig(env=process.env){
 const required=["DATABASE_URL","OIDC_ISSUER","OIDC_AUDIENCE"];
 const missing=required.filter(k=>!env[k]);
 if(env.NODE_ENV==="production"&&missing.length) throw new Error("Missing production configuration: "+missing.join(","));
 return {
  nodeEnv:env.NODE_ENV||"development",
  port:Number(env.PORT||8787),
  databaseUrl:env.DATABASE_URL||"file:./biupiu-rnd-os.db",
  oidcIssuer:env.OIDC_ISSUER||null,
  oidcAudience:env.OIDC_AUDIENCE||null
 };
}