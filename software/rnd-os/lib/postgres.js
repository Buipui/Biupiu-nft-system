const { readFileSync, readdirSync } = require('node:fs');
const path = require('node:path');

let Pool;

function loadPg() {
  if (!Pool) {
    try {
      ({ Pool } = require('pg'));
    } catch {
      throw new Error('PostgreSQL runtime requires the pg package');
    }
  }
  return Pool;
}

function createPool(connectionString = process.env.DATABASE_URL) {
  if (!connectionString) throw new Error('DATABASE_URL is required for PostgreSQL runtime');
  const PgPool = loadPg();
  return new PgPool({
    connectionString,
    max: Number(process.env.PGPOOL_MAX || 10),
    idleTimeoutMillis: Number(process.env.PG_IDLE_TIMEOUT_MS || 30000),
    connectionTimeoutMillis: Number(process.env.PG_CONNECT_TIMEOUT_MS || 5000),
    ssl: process.env.PGSSL === 'require' ? { rejectUnauthorized: false } : undefined
  });
}

async function health(pool) {
  const result = await pool.query('SELECT 1 AS ok');
  return result.rows[0].ok === 1;
}

async function runMigrations(pool, migrationsDir = path.join(__dirname, '..', 'db', 'migrations')) {
  await pool.query('CREATE TABLE IF NOT EXISTS schema_migrations (filename TEXT PRIMARY KEY, applied_at TIMESTAMPTZ NOT NULL DEFAULT now())');
  const files = readdirSync(migrationsDir).filter(f => f.endsWith('.sql')).sort();
  for (const filename of files) {
    const exists = await pool.query('SELECT 1 FROM schema_migrations WHERE filename = $1', [filename]);
    if (exists.rowCount) continue;
    const sql = readFileSync(path.join(migrationsDir, filename), 'utf8');
    const client = await pool.connect();
    try {
      await client.query('BEGIN');
      await client.query(sql);
      await client.query('INSERT INTO schema_migrations(filename) VALUES($1)', [filename]);
      await client.query('COMMIT');
    } catch (error) {
      await client.query('ROLLBACK');
      throw error;
    } finally {
      client.release();
    }
  }
}

async function closePool(pool) {
  if (pool) await pool.end();
}

module.exports = { createPool, health, runMigrations, closePool };
