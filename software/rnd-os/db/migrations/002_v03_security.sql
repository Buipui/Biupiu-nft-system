-- Biupiu R&D OS v0.3 security/runtime migration
-- Target: PostgreSQL 15+
CREATE TABLE IF NOT EXISTS sessions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  organisation_id UUID NOT NULL REFERENCES organisations(id) ON DELETE CASCADE,
  token_hash TEXT NOT NULL UNIQUE,
  expires_at TIMESTAMPTZ NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_sessions_user ON sessions(user_id);
CREATE INDEX IF NOT EXISTS idx_sessions_org ON sessions(organisation_id);
CREATE INDEX IF NOT EXISTS idx_sessions_expiry ON sessions(expires_at);

ALTER TABLE projects ADD COLUMN IF NOT EXISTS organisation_id UUID REFERENCES organisations(id);
ALTER TABLE research_objects ADD COLUMN IF NOT EXISTS organisation_id UUID REFERENCES organisations(id);
ALTER TABLE experiments ADD COLUMN IF NOT EXISTS organisation_id UUID REFERENCES organisations(id);
ALTER TABLE evidence_records ADD COLUMN IF NOT EXISTS organisation_id UUID REFERENCES organisations(id);
ALTER TABLE relationships ADD COLUMN IF NOT EXISTS organisation_id UUID REFERENCES organisations(id);

CREATE INDEX IF NOT EXISTS idx_projects_org ON projects(organisation_id);
CREATE INDEX IF NOT EXISTS idx_research_objects_org ON research_objects(organisation_id);
CREATE INDEX IF NOT EXISTS idx_experiments_org ON experiments(organisation_id);
CREATE INDEX IF NOT EXISTS idx_evidence_org ON evidence_records(organisation_id);
CREATE INDEX IF NOT EXISTS idx_relationships_org ON relationships(organisation_id);
