import { FEATURE_REGISTRY } from "./feature-registry.js";
import type { AccessDecision, AccessRequest, FeatureDefinition } from "./types.js";

export class PolicyEngine {
  constructor(private readonly registry=FEATURE_REGISTRY) {}
  decide(request:AccessRequest):AccessDecision {
    const {principal,featureId}=request; const feature=this.registry[featureId];
    if(!feature) return this.deny(request,"FEATURE_NOT_REGISTERED");
    if(principal.accountStatus!=="ACTIVE") return this.deny(request,"ACCOUNT_NOT_ACTIVE");
    if(principal.role!=="ROOT"&&!feature.roles.includes(principal.role)) return this.deny(request,"ROLE_NOT_PERMITTED");
    if(principal.role!=="ROOT"&&!feature.tiers.includes(principal.subscription)) return this.deny(request,"SUBSCRIPTION_NOT_ENTITLED");
    if(principal.explicitEntitlements?.length && !principal.explicitEntitlements.includes(featureId) && feature.safetyClass!=="ESSENTIAL") return this.deny(request,"EXPLICIT_ENTITLEMENT_MISSING");
    if(principal.revokedEntitlements?.includes(featureId)) return this.deny(request,"ENTITLEMENT_REVOKED");
    if(feature.requiresMfa&&principal.role!=="ROOT"&&!principal.mfaVerified) return this.deny(request,"MFA_REQUIRED");
    if(feature.productRequired&&request.productId&&!principal.productIds.includes(request.productId)) return this.deny(request,"PRODUCT_SCOPE_DENIED");
    if(request.siteId&&!principal.siteIds.includes(request.siteId)&&principal.role!=="ROOT"&&principal.role!=="PLATFORM_ADMIN") return this.deny(request,"SITE_SCOPE_DENIED");
    return {allowed:true,reason:"AUTHORIZED",featureId,principalId:principal.id,obligations:feature.safetyClass==="EXPERIMENTAL"?["EXPERIMENTAL_CONSENT_REQUIRED","AUDIT_REQUIRED"]:["AUDIT_REQUIRED"]};
  }
  private deny(request:AccessRequest,reason:string):AccessDecision {
    return {allowed:false,reason,featureId:request.featureId,principalId:request.principal.id,obligations:["AUDIT_REQUIRED"]};
  }
  getFeature(featureId:string):FeatureDefinition|undefined{return this.registry[featureId];}
}
