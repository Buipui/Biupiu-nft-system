export type ResourcePromotion =
  | "REGISTERED"
  | "INTEGRATED"
  | "CONNECTED"
  | "VERIFIED"
  | "BLOCKED";

export interface ResourceCandidate {
  id: string;
  source: string;
  license: string;
  role: string;
  promotion: ResourcePromotion;
}

export interface ResourceGateResult {
  passed: boolean;
  blocked: string[];
  eligible: string[];
}

export class ResourceGateway {
  private readonly resources = new Map<string, ResourceCandidate>();

  register(resource: ResourceCandidate): void {
    if (this.resources.has(resource.id)) {
      throw new Error("duplicate-resource:" + resource.id);
    }
    if (!resource.id || !resource.source || !resource.license || !resource.role) {
      throw new Error("invalid-resource-contract");
    }
    this.resources.set(resource.id, { ...resource });
  }

  promote(id: string, target: ResourcePromotion): void {
    const resource = this.resources.get(id);
    if (!resource) throw new Error("unknown-resource:" + id);
    if (resource.promotion === "BLOCKED") {
      throw new Error("blocked-resource:" + id);
    }
    resource.promotion = target;
  }

  list(): ResourceCandidate[] {
    return [...this.resources.values()].map((resource) => ({ ...resource }));
  }

  evaluate(): ResourceGateResult {
    const resources = this.list();
    const blocked = resources
      .filter((resource) => resource.promotion === "BLOCKED")
      .map((resource) => resource.id);
    const eligible = resources
      .filter((resource) => resource.promotion !== "BLOCKED")
      .map((resource) => resource.id);
    return { passed: blocked.length === 0, blocked, eligible };
  }
}

export function runResourceGatewaySmokeTest(): boolean {
  const gateway = new ResourceGateway();
  gateway.register({
    id: "openxr-sdk",
    source: "https://github.com/KhronosGroup/OpenXR-SDK",
    license: "Apache-2.0",
    role: "xr-loader-api",
    promotion: "REGISTERED",
  });
  gateway.register({
    id: "jolt-physics",
    source: "https://github.com/jrouwe/JoltPhysics",
    license: "MIT",
    role: "physics-provider",
    promotion: "REGISTERED",
  });

  gateway.promote("openxr-sdk", "INTEGRATED");
  const result = gateway.evaluate();
  return (
    result.passed &&
    result.eligible.includes("openxr-sdk") &&
    result.eligible.includes("jolt-physics")
  );
}
