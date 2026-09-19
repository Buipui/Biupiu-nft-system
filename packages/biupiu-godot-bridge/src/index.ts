export type GodotCapability =
  | "scene" | "physics" | "render" | "mobile" | "networking" | "xr"
  | "robotics" | "vision" | "compute" | "provenance";

export type ResourceGate = "reference" | "adapter-target" | "asset-review-required";

export interface GodotResource {
  id: string;
  url: string;
  license: string;
  gate: ResourceGate;
  capabilities: GodotCapability[];
}

export interface GodotAdapterRequest {
  sourceId: string;
  sceneId: string;
  capabilities: GodotCapability[];
  provenanceHash?: string;
}

export interface GodotAdapterPlan {
  engine: "godot";
  sourceId: string;
  sceneId: string;
  capabilities: GodotCapability[];
  provenanceRequired: true;
  releaseBlocked: boolean;
  reasons: string[];
}

export function planGodotExecution(
  request: GodotAdapterRequest,
  resource: GodotResource
): GodotAdapterPlan {
  const reasons: string[] = [];

  if (resource.gate === "asset-review-required") {
    reasons.push("resource contains assets requiring individual licence review");
  }

  const unsupported = request.capabilities.filter(
    capability => !resource.capabilities.includes(capability)
  );
  if (unsupported.length) {
    reasons.push("resource does not declare capabilities: " + unsupported.join(", "));
  }

  if (!request.provenanceHash) {
    reasons.push("provenance hash is required before release");
  }

  return {
    engine: "godot",
    sourceId: request.sourceId,
    sceneId: request.sceneId,
    capabilities: request.capabilities,
    provenanceRequired: true,
    releaseBlocked: reasons.length > 0,
    reasons,
  };
}
