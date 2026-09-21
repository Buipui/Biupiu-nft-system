import { NativeResourceRegistry } from './registry';
import { GameResource, ModdingStationJob } from './types';

const baseResource: GameResource = {
  resourceId: 'test.native.game',
  title: 'Biupiu Native Test Game',
  resourceClass: 'native_biupiu_game',
  platform: 'BIUPIU',
  rightsState: 'GREEN',
  commercialUse: true,
  redistributionAllowed: true,
  dependencies: [],
  compatibilityStatus: 'PASS',
  securityStatus: 'PASS',
  approval: 'APPROVED',
  verificationState: 'VERIFIED',
};

function expect(condition: boolean, message: string): void {
  if (!condition) throw new Error(message);
}

export function runNativeResourceRegistryTests(): void {
  const registry = new NativeResourceRegistry();

  const denied: GameResource = {
    ...baseResource,
    resourceId: 'test.denied.game',
    rightsState: 'RED',
  };
  registry.register(denied);

  const deniedDecision = registry.canLaunch(denied.resourceId);
  expect(!deniedDecision.allowed, 'red rights must fail closed');
  expect(deniedDecision.reasons.includes('rights_not_cleared'), 'red rights reason missing');

  const approvedDecisionBeforeRegistration = registry.canLaunch('missing.resource');
  expect(!approvedDecisionBeforeRegistration.allowed, 'missing resources must fail closed');

  registry.register(baseResource);
  const approvedDecision = registry.canLaunch(baseResource.resourceId);
  expect(approvedDecision.allowed, 'fully verified resource should be launchable');

  const invalidJob: ModdingStationJob = {
    jobId: '',
    creatorId: '',
    engine: 'BIUPIU',
    packagePath: '',
    declaredLicence: '',
    dependencies: [''],
    requestedCapabilities: [],
    status: 'SUBMITTED',
  };
  const errors = registry.validateModJob(invalidJob);
  expect(errors.length >= 4, 'invalid mod job should produce validation errors');

  let duplicateRejected = false;
  try {
    registry.register(baseResource);
  } catch {
    duplicateRejected = true;
  }
  expect(duplicateRejected, 'duplicate resource IDs must be rejected');
}
