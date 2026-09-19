import { DMSService } from "./dms-service.js";
import type { AccessRequest, AccessDecision, Principal } from "./types.js";

export interface ServiceContext {
  principal: Principal;
  siteId?: string;
  productId?: string;
  organizationId?: string;
}

export interface ProtectedService {
  serviceId: string;
  featureIds: readonly string[];
  invoke<T>(featureId: string, context: ServiceContext, handler: () => T): T | AccessDecision;
}

export class DMSServiceGateway implements ProtectedService {
  constructor(
    public readonly serviceId: string,
    public readonly featureIds: readonly string[],
    private readonly dms = new DMSService()
  ) {}

  invoke<T>(featureId: string, context: ServiceContext, handler: () => T): T | AccessDecision {
    if (!this.featureIds.includes(featureId)) {
      return this.dms.authorize({principal: context.principal, featureId, siteId: context.siteId, productId: context.productId, organizationId: context.organizationId});
    }
    const decision = this.dms.authorize({principal: context.principal, featureId, siteId: context.siteId, productId: context.productId, organizationId: context.organizationId});
    return decision.allowed ? handler() : decision;
  }

  authorize(context: ServiceContext, featureId: string): AccessDecision {
    const request: AccessRequest = {principal: context.principal, featureId, siteId: context.siteId, productId: context.productId, organizationId: context.organizationId};
    return this.dms.authorize(request);
  }

  getAudit() { return this.dms.getAudit(); }
}
