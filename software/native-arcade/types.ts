export type RightsState = 'GREEN' | 'BLUE' | 'YELLOW' | 'ORANGE' | 'RED' | 'GREY';
export type VerificationState = 'REGISTERED' | 'IMPLEMENTED' | 'VERIFIED' | 'RELEASED';
export type ResourceClass =
  | 'native_biupiu_game'
  | 'open_source_game'
  | 'licensed_game'
  | 'freeware_game'
  | 'emulator_runtime'
  | 'community_mod'
  | 'unreal_asset'
  | 'unity_asset'
  | 'biupiu_engine_asset'
  | 'museum_reference';

export interface GameResource {
  resourceId: string;
  title: string;
  resourceClass: ResourceClass;
  platform: string;
  creator?: string;
  publisher?: string;
  rightsHolder?: string;
  licence?: string;
  rightsState: RightsState;
  commercialUse: boolean;
  redistributionAllowed: boolean;
  sourceUrl?: string;
  sourceVersion?: string;
  dependencies: string[];
  runtimeAdapter?: string;
  contentHash?: string;
  compatibilityStatus: 'UNKNOWN' | 'PASS' | 'FAIL';
  securityStatus: 'UNKNOWN' | 'PASS' | 'FAIL';
  approval: 'PENDING' | 'APPROVED' | 'REJECTED';
  verificationState: VerificationState;
}

export interface ModdingStationJob {
  jobId: string;
  creatorId: string;
  engine: 'UNREAL' | 'UNITY' | 'BIUPIU';
  packagePath: string;
  declaredLicence: string;
  dependencies: string[];
  requestedCapabilities: string[];
  status: 'SUBMITTED' | 'VALIDATING' | 'BLOCKED' | 'READY_FOR_REVIEW' | 'APPROVED';
}

export interface ArcadeLaunchDecision {
  allowed: boolean;
  reasons: string[];
}
