import { DepartmentServiceAdapter, DepartmentServiceRequest, DepartmentServiceResult } from "./department-service";

export interface DepartmentServiceGateway {
  dispatch(request: DepartmentServiceRequest): DepartmentServiceResult;
}

export class EntitlementAwareServiceGateway implements DepartmentServiceGateway {
  constructor(
    private readonly adapter: DepartmentServiceAdapter,
    private readonly authorizedDepartments: readonly string[]
  ) {}

  dispatch(request: DepartmentServiceRequest): DepartmentServiceResult {
    if (!this.authorizedDepartments.includes(request.department)) {
      return { ...request, status: "DENIED", message: "Department service access denied by entitlement boundary." };
    }
    return this.adapter.execute(request);
  }
}
