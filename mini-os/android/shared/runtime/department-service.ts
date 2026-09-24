export type DepartmentServiceId = "RESEARCH_REPOSITORY" | "AUTOMATION" | "AI" | "WORLD";

export interface DepartmentServiceRequest {
  service: DepartmentServiceId;
  department: string;
  action: string;
}

export interface DepartmentServiceResult {
  service: DepartmentServiceId;
  department: string;
  action: string;
  status: "AVAILABLE" | "NOT_CONFIGURED" | "DENIED";
  message: string;
}

export interface DepartmentServiceAdapter {
  supports(service: DepartmentServiceId, department: string): boolean;
  execute(request: DepartmentServiceRequest): DepartmentServiceResult;
}

export function createServiceRequest(service: DepartmentServiceId, department: string, action: string): DepartmentServiceRequest {
  return { service, department, action };
}
