import type { AccountStatus, Principal, SubscriptionTier } from "./types.js";

export interface IdentityRecord {
  userId:string; role:Principal["role"]; customerId:string; organizationId?:string;
  siteIds:string[]; productIds:string[]; accountStatus:AccountStatus; mfaVerified:boolean;
}
export interface SubscriptionRecord {
  subscriptionId:string; customerId:string; plan:SubscriptionTier;
  status:"ACTIVE"|"SUSPENDED"|"EXPIRED"; startAt?:string; endAt?:string;
}
export interface EntitlementRecord {
  customerId:string; featureId:string; state:"GRANTED"|"REVOKED";
  effectiveFrom?:string; effectiveTo?:string;
}

export interface DMSRepository {
  getIdentity(userId:string):Promise<IdentityRecord|null>;
  getSubscription(customerId:string):Promise<SubscriptionRecord|null>;
  getEntitlements(customerId:string):Promise<EntitlementRecord[]>;
}

export class InMemoryDMSRepository implements DMSRepository {
  constructor(
    private readonly identities:IdentityRecord[]=[],
    private readonly subscriptions:SubscriptionRecord[]=[],
    private readonly entitlements:EntitlementRecord[]=[]
  ) {}
  async getIdentity(userId:string){return this.identities.find(x=>x.userId===userId)??null;}
  async getSubscription(customerId:string){return this.subscriptions.find(x=>x.customerId===customerId)??null;}
  async getEntitlements(customerId:string){return this.entitlements.filter(x=>x.customerId===customerId);}
}
