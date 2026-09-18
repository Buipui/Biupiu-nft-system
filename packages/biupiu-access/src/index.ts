export const PACKAGE = "@biupiu/access";
export type SubscriberStatus = "active" | "suspended" | "pending";
export interface AccessContext {
  subscriberId: string;
  tier: string;
  status: SubscriberStatus;
  entitlements: string[];
}
