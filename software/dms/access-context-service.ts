import type { Principal } from "./types.js";
import type { DMSRepository } from "./repository-store.js";

export class AccessContextService {
  constructor(private readonly repository:DMSRepository) {}

  async resolvePrincipal(userId:string):Promise<Principal|null> {
    const identity=await this.repository.getIdentity(userId);
    if(!identity) return null;
    const subscription=await this.repository.getSubscription(identity.customerId);
    const entitlements=await this.repository.getEntitlements(identity.customerId);
    if(!subscription || subscription.status!=="ACTIVE") {
      return {
        id:identity.userId, role:identity.role, accountStatus:identity.accountStatus,
        organizationId:identity.organizationId, siteIds:identity.siteIds, productIds:identity.productIds,
        subscription: subscription?.plan ?? "CORE",
        explicitEntitlements:[],
        revokedEntitlements:entitlements.filter(e=>e.state==="REVOKED").map(e=>e.featureId),
        mfaVerified:identity.mfaVerified
      };
    }
    return {
      id:identity.userId, role:identity.role, accountStatus:identity.accountStatus,
      organizationId:identity.organizationId, siteIds:identity.siteIds, productIds:identity.productIds,
      subscription:subscription.plan,
      explicitEntitlements:entitlements.filter(e=>e.state==="GRANTED").map(e=>e.featureId),
      revokedEntitlements:entitlements.filter(e=>e.state==="REVOKED").map(e=>e.featureId),
      mfaVerified:identity.mfaVerified
    };
  }
}
