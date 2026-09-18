export type RuntimeClient = "android" | "windows";

export type RuntimeRoute =
  | "MAIN_HUB"
  | "SMART_FARMING"
  | "SMART_METAL_WORKSHOP"
  | "RND_OS";

export interface RuntimeSession {
  client: RuntimeClient;
  subscriberId: string;
  tier: string;
  status: "active" | "suspended" | "pending";
  entitlements: string[];
}

export interface RuntimeRouteState {
  route: RuntimeRoute;
  enterable: boolean;
  reason: "AUTHORIZED" | "NO_ENTITLEMENT" | "INACTIVE_ACCOUNT";
}

export function resolveRoute(
  session: RuntimeSession,
  route: RuntimeRoute
): RuntimeRouteState {
  if (session.status !== "active") {
    return { route, enterable: false, reason: "INACTIVE_ACCOUNT" };
  }
  if (route === "MAIN_HUB" || route === "RND_OS") {
    return { route, enterable: true, reason: "AUTHORIZED" };
  }
  const entitlement =
    route === "SMART_FARMING"
      ? "SMART_FARMING"
      : "SMART_METAL_WORKSHOP";
  return session.entitlements.includes(entitlement)
    ? { route, enterable: true, reason: "AUTHORIZED" }
    : { route, enterable: false, reason: "NO_ENTITLEMENT" };
}
