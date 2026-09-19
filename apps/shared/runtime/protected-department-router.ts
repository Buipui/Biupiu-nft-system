import { resolveDepartment, type DepartmentRoute, type DepartmentTarget } from "./department-router.js";
import { DMSServiceGateway } from "../../../software/dms/service-gateway.js";
import { PROTECTED_DEPARTMENT_SERVICES } from "../../../software/dms/department-service-map.js";
import type { Principal } from "../../../software/dms/types.js";

export interface AuthorizedDepartmentRoute extends DepartmentTarget {
  allowed: boolean;
  deniedFeatureIds: string[];
  availableFeatureIds: string[];
}

export function resolveAuthorizedDepartment(
  route: DepartmentRoute,
  principal: Principal,
  siteId?: string,
  productId?: string
): AuthorizedDepartmentRoute {
  const target = resolveDepartment(route);
  const service = PROTECTED_DEPARTMENT_SERVICES[route];
  const gateway = new DMSServiceGateway(target.packageName, service.featureIds);
  const availableFeatureIds = service.featureIds.filter(featureId =>
    gateway.authorize({principal, siteId, productId}, featureId).allowed
  );
  return {
    ...target,
    allowed: availableFeatureIds.length > 0,
    deniedFeatureIds: service.featureIds.filter(id => !availableFeatureIds.includes(id)),
    availableFeatureIds
  };
}
