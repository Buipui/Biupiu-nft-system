import { BiupiuArcadeRuntime, ArcadeRuntimeAdapter } from './runtime';
import { NativeResourceRegistry } from './registry';
import { GameResource } from './types';

const resource: GameResource = {
  resourceId: 'test.runtime.game',
  title: 'Biupiu Runtime Test',
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

export async function runNativeArcadeRuntimeTests(): Promise<void> {
  const registry = new NativeResourceRegistry();
  registry.register(resource);

  let starts = 0;
  let stops = 0;
  const adapter: ArcadeRuntimeAdapter = {
    adapterId: 'biupiu-test-adapter',
    canHandle: (candidate) => candidate.platform === 'BIUPIU',
    start: async () => { starts += 1; },
    stop: async () => { stops += 1; },
  };

  const runtime = new BiupiuArcadeRuntime(registry, [adapter]);
  const launch = runtime.launch(resource.resourceId, 'session-1');
  expect(launch.allowed, 'verified resource should pass runtime launch gate');

  await runtime.start('session-1');
  expect(runtime.getSession('session-1')?.state === 'RUNNING', 'session should be running');
  expect(starts === 1, 'adapter start should execute once');

  await runtime.stop('session-1');
  expect(runtime.getSession('session-1')?.state === 'STOPPED', 'session should stop');
  expect(stops === 1, 'adapter stop should execute once');

  const missingAdapterRuntime = new BiupiuArcadeRuntime(registry);
  const denied = missingAdapterRuntime.launch(resource.resourceId, 'session-2');
  expect(!denied.allowed, 'runtime without adapter must fail closed');
  expect(denied.reasons.includes('runtime_adapter_not_available'), 'missing adapter reason missing');
}
