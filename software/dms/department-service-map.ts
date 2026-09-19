import type { DepartmentRoute } from "../../apps/shared/runtime/department-router.js";

export interface ProtectedDepartmentService {
  route: DepartmentRoute;
  featureIds: readonly string[];
}

export const PROTECTED_DEPARTMENT_SERVICES: Record<DepartmentRoute, ProtectedDepartmentService> = {
  SMART_FARMING: {route:"SMART_FARMING", featureIds:["agri.operations"]},
  SMART_METAL_WORKSHOP: {route:"SMART_METAL_WORKSHOP", featureIds:["manufacturing.production","manufacturing.advanced-analytics","maintenance.management"]},
  RND_OS: {route:"RND_OS", featureIds:["rnd.experiment-management","engineering.simulation","digital-twin.advanced"]},
  CREATIVE_AI: {route:"CREATIVE_AI", featureIds:["dms.profile.read"]}
};
