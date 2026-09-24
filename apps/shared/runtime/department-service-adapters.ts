import {
  DepartmentServiceAdapter,
  DepartmentServiceId,
  DepartmentServiceRequest,
  DepartmentServiceResult
} from "./department-service";

const SERVICE_MAP: Record<string, readonly DepartmentServiceId[]> = {
  SMART_FARMING: ["WORLD", "AUTOMATION", "AI"],
  SMART_METAL_WORKSHOP: ["WORLD", "AUTOMATION", "AI"],
  RND_OS: ["WORLD", "RESEARCH_REPOSITORY", "AUTOMATION", "AI"]
};

export class ContractOnlyDepartmentServiceAdapter implements DepartmentServiceAdapter {
  supports(service: DepartmentServiceId, department: string): boolean {
    return SERVICE_MAP[department]?.includes(service) ?? false;
  }

  execute(request: DepartmentServiceRequest): DepartmentServiceResult {
    const supported = this.supports(request.service, request.department);
    return {
      ...request,
      status: supported ? "NOT_CONFIGURED" : "NOT_CONFIGURED",
      message: supported
        ? "Service contract is registered; platform adapter is not configured yet."
        : "Service is not registered for this department."
    };
  }
}
