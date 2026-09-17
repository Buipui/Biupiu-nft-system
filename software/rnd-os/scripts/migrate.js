const { createPool, runMigrations, closePool } = require('../lib/postgres');

async function main() {
  const pool = createPool();
  try {
    await runMigrations(pool);
    console.log('Biupiu R&D OS migrations applied.');
  } finally {
    await closePool(pool);
  }
}

main().catch(error => {
  console.error(error.message);
  process.exitCode = 1;
});
