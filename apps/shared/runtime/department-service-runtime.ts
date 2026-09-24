import { DepartmentServiceRequest, DepartmentServiceResult } from "./department-service";
import { DepartmentServiceRegistry } from "./department-service-registry";
import { EntitlementAwareServiceGateway } from "./department-service-gateway";
import type { SubscriberAccount } from "../../../../software/rnd-os/access/subscriber-model";

export class DepartmentServiceRuntime {
  constructor(
    private readonly registry: DepartmentServiceRegistry,
    private readonly account: SubscriberAccount
  ) {}

  dispatch(request: DepartmentServiceRequest): DepartmentServiceResult {
    const registration = this.registry.resolve(request.department, request.service);
    if (!registration) {
      return {
        ...request,
        status: "NOT_CONFIGURED",
        message: "No registered service adapter exists for this department."
      };
    }

    return new EntitlementAwareServiceGateway(registration.adapter, this.account).dispatch(request);
  }
}
