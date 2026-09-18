import { resolveDepartment, type DepartmentRoute, type DepartmentTarget } from "./department-router";

export interface DepartmentRuntimeContext {
  subscriberId: string;
  tier: string;
  status: "active" | "suspended" | "pending";
  entitlements: string[];
}

export interface DepartmentRuntimeAdapter {
  target: DepartmentTarget;
  canStart: boolean;
  reason: "AUTHORIZED" | "NO_ENTITLEMENT" | "INACTIVE_ACCOUNT";
}

export function createDepartmentRuntime(
  context: DepartmentRuntimeContext,
  route: DepartmentRoute
): DepartmentRuntimeAdapter {
  if (context.status !== "active") {
    return { target: resolveDepartment(route), canStart: false, reason: "INACTIVE_ACCOUNT" };
  }

  const target = resolveDepartment(route);
  const allowed = route === "RND_OS" || context.entitlements.includes(route);

  return {
    target,
    canStart: allowed,
    reason: allowed ? "AUTHORIZED" : "NO_ENTITLEMENT"
  };
}
