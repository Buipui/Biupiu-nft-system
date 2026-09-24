import { DepartmentServiceAdapter, DepartmentServiceRequest, DepartmentServiceResult } from "./department-service";
import {
  canEnterDepartment,
  authorizeDepartmentCapability,
  type SubscriberAccount,
  type DepartmentScope
} from "../../../../software/rnd-os/access/subscriber-model";

const SERVICE_CAPABILITY: Record<DepartmentServiceRequest["service"], string> = {
  WORLD: "department_simulations",
  RESEARCH_REPOSITORY: "research_sandbox",
  AUTOMATION: "virtual_workshop_tools",
  AI: "advanced_simulation"
};

export interface DepartmentServiceGateway {
  dispatch(request: DepartmentServiceRequest): DepartmentServiceResult;
}

export class EntitlementAwareServiceGateway implements DepartmentServiceGateway {
  constructor(
    private readonly adapter: DepartmentServiceAdapter,
    private readonly account: SubscriberAccount
  ) {}

  dispatch(request: DepartmentServiceRequest): DepartmentServiceResult {
    const department = request.department as DepartmentScope;

    if (!canEnterDepartment(this.account, department)) {
      return {
        ...request,
        status: "DENIED",
        message: "Department service access denied by subscriber entitlement."
      };
    }

    const capability = SERVICE_CAPABILITY[request.service];
    if (!authorizeDepartmentCapability(this.account, department, capability)) {
      return {
        ...request,
        status: "DENIED",
        message: `Service access denied by subscriber tier capability: ${capability}.`
      };
    }

    return this.adapter.execute(request);
  }
}
