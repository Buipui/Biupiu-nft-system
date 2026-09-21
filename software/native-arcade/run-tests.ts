import { runNativeResourceRegistryTests } from './registry.test';
import { runNativeArcadeRuntimeTests } from './runtime.test';

async function main(): Promise<void> {
  runNativeResourceRegistryTests();
  await runNativeArcadeRuntimeTests();
  console.log('BIUPIU_NATIVE_ARCADE_TESTS: PASS');
}

void main().catch((error) => {
  console.error('BIUPIU_NATIVE_ARCADE_TESTS: FAIL');
  console.error(error);
  process.exitCode = 1;
});
