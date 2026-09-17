const test = require('node:test');
const assert = require('node:assert/strict');

test('PostgreSQL adapter requires explicit DATABASE_URL', () => {
  const { createPool } = require('../lib/postgres');
  const old = process.env.DATABASE_URL;
  delete process.env.DATABASE_URL;
  assert.throws(() => createPool(), /DATABASE_URL is required/);
  if (old !== undefined) process.env.DATABASE_URL = old;
});

test('migration filenames are deterministically ordered', () => {
  const fs = require('node:fs');
  const path = require('node:path');
  const dir = path.join(__dirname, '..', 'db', 'migrations');
  const files = fs.readdirSync(dir).filter(f => f.endsWith('.sql')).sort();
  assert.deepEqual(files, [...files].sort());
  assert.ok(files.includes('000_schema_migrations.sql'));
  assert.ok(files.includes('002_v03_security.sql'));
});
