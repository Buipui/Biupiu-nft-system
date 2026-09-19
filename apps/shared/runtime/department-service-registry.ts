import { DepartmentServiceAdapter, DepartmentServiceId } from "./department-service";

export interface DepartmentServiceRegistration {
  department: string;
  service: DepartmentServiceId;
  provider: string;
  version: string;
  adapter: DepartmentServiceAdapter;
}

export class DepartmentServiceRegistry {
  private readonly registrations: DepartmentServiceRegistration[] = [];

  register(registration: DepartmentServiceRegistration): void {
    const exists = this.registrations.some(
      item => item.department === registration.department && item.service === registration.service
    );
    if (exists) throw new Error("Service already registered");
    this.registrations.push(registration);
  }

  resolve(department: string, service: DepartmentServiceId): DepartmentServiceRegistration | null {
    return this.registrations.find(
      item => item.department === department && item.service === service
    ) ?? null;
  }

  list(department?: string): readonly DepartmentServiceRegistration[] {
    return department ? this.registrations.filter(item => item.department === department) : this.registrations;
  }
}
