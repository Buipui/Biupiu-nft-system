export type RedshiftHost =
  | "CINEMA_4D"
  | "MAYA"
  | "THREEDS_MAX"
  | "HOUDINI"
  | "KATANA"
  | "BLENDER"
  | "UNKNOWN";

export type RedshiftDeviceKind = "NVIDIA" | "APPLE_SILICON" | "AMD" | "CPU" | "UNKNOWN";

export interface RedshiftEnvironment {
  host: RedshiftHost;
  hostVersion: string | null;
  redshiftVersion: string | null;
  device: {
    kind: RedshiftDeviceKind;
    name: string | null;
    vramGb: number | null;
    driver: string | null;
  };
  detected: boolean;
}

export interface RedshiftValidationResult {
  gate: "RED-02";
  status: "PASS" | "FAIL" | "BLOCKED";
  checks: Record<string, "PASS" | "FAIL" | "BLOCKED">;
  environment: RedshiftEnvironment;
  failureReasons: string[];
}

export interface RedshiftAdapter {
  detectEnvironment(): Promise<RedshiftEnvironment>;
  validate(environment: RedshiftEnvironment): RedshiftValidationResult;
}

export const REDSHIFT_OSL_VALIDATION_SET = [
  "SpaceTransform.osl",
  "UberConstant.osl",
  "ColorShuffle.osl",
  "TextureNoTile.osl",
  "ThinFilmInterference.osl"
] as const;

export const REDSHIFT_VALIDATION_RULES = {
  failClosedWithoutLiveEnvironment: true,
  proprietaryBinaryRedistribution: false,
  deterministicRenderRequired: true,
  provenanceRequired: true,
  sourceAssetMustRemainAuthoritative: true
} as const;

export function validateRedshiftEnvironment(
  environment: RedshiftEnvironment
): RedshiftValidationResult {
  const checks: RedshiftValidationResult["checks"] = {
    hostDetected: environment.host !== "UNKNOWN" ? "PASS" : "FAIL",
    redshiftDetected: environment.redshiftVersion ? "PASS" : "FAIL",
    computeDeviceDetected:
      environment.device.kind !== "UNKNOWN" ? "PASS" : "FAIL",
    renderReady: environment.detected ? "PASS" : "BLOCKED"
  };

  const failureReasons: string[] = [];
  if (checks.hostDetected === "FAIL") failureReasons.push("Supported host not detected.");
  if (checks.redshiftDetected === "FAIL") failureReasons.push("Redshift version not detected.");
  if (checks.computeDeviceDetected === "FAIL") failureReasons.push("Compute device or CPU fallback not detected.");
  if (checks.renderReady === "BLOCKED") failureReasons.push("Live Redshift environment is not connected.");

  const status =
    failureReasons.length === 0
      ? "PASS"
      : environment.detected
        ? "FAIL"
        : "BLOCKED";

  return {
    gate: "RED-02",
    status,
    checks,
    environment,
    failureReasons
  };
}

export const REDSHIFT_PROVIDER_CONTRACT = {
  provider: "REDSHIFT",
  resourceIndex: "research/BIUPIU-REDSHIFT-RESOURCES-v1.0.md",
  validationGate: "research/BIUPIU-REDSHIFT-VALIDATION-GATE-v1.0.md",
  testScene: "research/BIUPIU-REDSHIFT-TEST-SCENE-SPEC-v1.0.md",
  proprietaryDependenciesEmbedded: false
} as const;
