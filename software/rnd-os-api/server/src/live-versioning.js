// Gate 08 reference persistence helpers.
// These helpers are designed to be called inside a DB transaction.
export function ensureVersionColumn(db){
  const cols=db.prepare("PRAGMA table_info(records)").all().map(x=>x.name);
  if(!cols.includes("version")) db.exec("ALTER TABLE records ADD COLUMN version INTEGER NOT NULL DEFAULT 1");
  if(!cols.includes("content_hash")) db.exec("ALTER TABLE records ADD COLUMN content_hash TEXT");
  if(!cols.includes("updated_by")) db.exec("ALTER TABLE records ADD COLUMN updated_by TEXT");
}
export function revisionConflict(currentVersion,baseVersion){
  return Number(currentVersion)!==Number(baseVersion);
}