export function productionChecklist(config){
 return [
  ["DATABASE_URL",Boolean(config.databaseUrl&&config.databaseUrl!=="file:./biupiu-rnd-os.db")],
  ["OIDC_ISSUER",Boolean(config.oidcIssuer)],
  ["OIDC_AUDIENCE",Boolean(config.oidcAudience)],
  ["TLS_REQUIRED",true],
  ["CLIENT_SECRETS_FORBIDDEN",true]
 ];
}
