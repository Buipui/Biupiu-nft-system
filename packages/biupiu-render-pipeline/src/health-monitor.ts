export type HealthStatus="HEALTHY"|"DEGRADED"|"BLOCKED";
export interface ProviderHealth { provider:string; status:HealthStatus; latencyMs?:number; lastChecked:string; failureRate?:number; }
export interface HealthMonitor { check(provider:string):Promise<ProviderHealth>; }
export function selectHealthyProvider(health:ProviderHealth[]):string|undefined { return health.find(x=>x.status==="HEALTHY")?.provider; }