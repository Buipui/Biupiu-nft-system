import { PolicyEngine } from "./policy-engine.js";
import type { AccessDecision, AccessRequest, Principal, SubscriptionTier } from "./types.js";
export interface AuditEvent {timestamp:string;principalId:string;featureId:string;allowed:boolean;reason:string;}

export class DMSService {
  private readonly audit:AuditEvent[]=[];
  constructor(private readonly policy=new PolicyEngine()) {}
  authorize(request:AccessRequest):AccessDecision {
    const decision=this.policy.decide(request);
    this.audit.push({timestamp:(request.now??new Date()).toISOString(),principalId:request.principal.id,featureId:request.featureId,allowed:decision.allowed,reason:decision.reason});
    return decision;
  }
  can(principal:Principal,featureId:string,scope?:Omit<AccessRequest,"principal"|"featureId">):boolean {
    return this.authorize({principal,featureId,...scope}).allowed;
  }
  effectiveAccess(principal:Principal):string[] {
    return this.policy.listFeatures().filter(featureId=>this.can(principal,featureId));
  }
  setSubscription(principal:Principal,subscription:SubscriptionTier):Principal{return {...principal,subscription};}
  getAudit():readonly AuditEvent[]{return [...this.audit];}
}
