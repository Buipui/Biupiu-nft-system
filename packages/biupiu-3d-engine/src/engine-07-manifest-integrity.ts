import { ResourceCandidate, ResourceGateway } from "./resource-gateway";

export interface ResourceManifestIntegrity {
  passed: boolean;
  duplicateIds: string[];
  invalidEntries: string[];
  blockedEntries: string[];
  resourceCount: number;
}

export function validateResourceManifest(
  candidates: readonly ResourceCandidate[],
): ResourceManifestIntegrity {
  const seen = new Set<string>();
  const duplicateIds: string[] = [];
  const invalidEntries: string[] = [];

  for (const resource of candidates) {
    if (seen.has(resource.id)) duplicateIds.push(resource.id);
    seen.add(resource.id);

    if (!resource.id || !resource.source || !resource.license || !resource.role) {
      invalidEntries.push(resource.id || "<missing-id>");
    }
  }

  const blockedEntries = candidates
    .filter((resource) => resource.promotion === "BLOCKED")
    .map((resource) => resource.id);

  return {
    passed:
      duplicateIds.length === 0 &&
      invalidEntries.length === 0 &&
      blockedEntries.length === 0,
    duplicateIds,
    invalidEntries,
    blockedEntries,
    resourceCount: candidates.length,
  };
}

export function runEngine07ManifestIntegritySmokeTest(): boolean {
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
  gateway.register({
    id: "project-chrono",
    source: "https://github.com/projectchrono/chrono",
    license: "BSD-3-Clause",
    role: "multiphysics-provider",
    promotion: "REGISTERED",
  });
  gateway.register({
    id: "mujoco",
    source: "https://github.com/google-deepmind/mujoco",
    license: "Apache-2.0",
    role: "robotics-physics-provider",
    promotion: "REGISTERED",
  });
  gateway.register({
    id: "openexr",
    source: "https://github.com/AcademySoftwareFoundation/openexr",
    license: "BSD-3-Clause",
    role: "hdr-interchange",
    promotion: "REGISTERED",
  });

  const integrity = validateResourceManifest(gateway.list());
  return (
    integrity.passed &&
    integrity.resourceCount === 5 &&
    integrity.duplicateIds.length === 0 &&
    integrity.invalidEntries.length === 0 &&
    integrity.blockedEntries.length === 0
  );
}
