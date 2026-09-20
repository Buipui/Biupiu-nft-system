import { ResourceGateway } from "./resource-gateway";

export interface Engine06Report {
  passed: boolean;
  resourceCount: number;
  smokeTestPassed: boolean;
  promotion: "VERIFIED" | "BLOCKED";
}

export function runEngine06RealityGate(): Engine06Report {
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

  const smokeTestPassed = runGatewayCheck(gateway);
  return {
    passed: smokeTestPassed,
    resourceCount: gateway.list().length,
    smokeTestPassed,
    promotion: smokeTestPassed ? "VERIFIED" : "BLOCKED",
  };
}

function runGatewayCheck(gateway: ResourceGateway): boolean {
  const resources = gateway.list();
  if (resources.length !== 5) return false;

  const first = resources[0];
  gateway.promote(first.id, "INTEGRATED");

  const result = gateway.evaluate();
  return (
    result.passed &&
    result.blocked.length === 0 &&
    result.eligible.length === resources.length &&
    result.eligible.includes(first.id)
  );
}
