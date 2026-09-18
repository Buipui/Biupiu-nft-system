import { createDepartmentRuntime, type DepartmentRuntimeContext } from "./department-runtime";
import type { DepartmentRoute } from "./department-router";

export interface DepartmentLaunchResult {
  route: DepartmentRoute;
  packageName: string;
  started: boolean;
  reason: "STARTED" | "NO_ENTITLEMENT" | "INACTIVE_ACCOUNT";
}

export function launchDepartment(
  context: DepartmentRuntimeContext,
  route: DepartmentRoute
): DepartmentLaunchResult {
  const runtime = createDepartmentRuntime(context, route);
  return {
    route,
    packageName: runtime.target.packageName,
    started: runtime.canStart,
    reason: runtime.canStart ? "STARTED" : runtime.reason
  };
}
