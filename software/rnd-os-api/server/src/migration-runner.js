// Minimal migration contract. Production should use a transactional migration framework
// appropriate to the selected PostgreSQL deployment.
export const MIGRATIONS=[
 {version:1,file:"001-initial-schema.sql"},
 {version:2,file:"002-record-integrity.sql"},
 {version:3,file:"003-schema-version.sql"}
];
export function pendingVersions(applied=[]){
 const set=new Set(applied);
 return MIGRATIONS.filter(m=>!set.has(m.version));
}