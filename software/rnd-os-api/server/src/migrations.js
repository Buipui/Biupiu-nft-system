import Database from "better-sqlite3";
export function migrate(db){
 db.exec("CREATE TABLE IF NOT EXISTS schema_version(version INTEGER NOT NULL)");
 const row=db.prepare("SELECT version FROM schema_version ORDER BY version DESC LIMIT 1").get();
 if(!row){db.prepare("INSERT INTO schema_version VALUES(1)").run();return 1}
 return row.version;
}
export function currentVersion(db){return db.prepare("SELECT version FROM schema_version ORDER BY version DESC LIMIT 1").get()?.version||0}