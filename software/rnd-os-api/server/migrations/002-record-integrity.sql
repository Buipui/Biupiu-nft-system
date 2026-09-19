-- Gate 10 migration for existing installations.
-- Execute under controlled backup/transaction procedures.
ALTER TABLE records ADD COLUMN version INTEGER NOT NULL DEFAULT 1;
ALTER TABLE records ADD COLUMN content_hash TEXT;
ALTER TABLE records ADD COLUMN updated_by TEXT;