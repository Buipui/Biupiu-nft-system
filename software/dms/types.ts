export type Role = "ROOT"|"PLATFORM_ADMIN"|"DEPARTMENT_ADMIN"|"SITE_MANAGER"|"STAFF_OPERATOR"|"RND_USER"|"CUSTOMER"|"CUSTOMER_RND"|"DEVICE_SERVICE";
export type SubscriptionTier = "CORE"|"STANDARD"|"PRO"|"ENTERPRISE"|"RND_PARTNER";
export type AccountStatus = "ACTIVE"|"SUSPENDED"|"PENDING";
export type SafetyClass = "ESSENTIAL"|"OPTIONAL"|"EXPERIMENTAL";

export interface Principal {
  id: string; role: Role; accountStatus: AccountStatus;
  organizationId?: string; siteIds: string[]; productIds: string[];
  subscription: SubscriptionTier; explicitEntitlements?: string[];
  revokedEntitlements?: string[]; mfaVerified?: boolean;
}
export interface FeatureDefinition {
  id: string; module: string; action: string; safetyClass: SafetyClass;
  roles: Role[]; tiers: SubscriptionTier[]; requiresMfa?: boolean; productRequired?: boolean;
}
export interface AccessRequest {
  principal: Principal; featureId: string; organizationId?: string;
  siteId?: string; productId?: string; now?: Date;
}
export interface AccessDecision {
  allowed: boolean; reason: string; featureId: string; principalId: string; obligations: string[];
}
