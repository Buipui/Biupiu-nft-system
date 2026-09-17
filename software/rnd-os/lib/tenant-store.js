const { tenantScope, assertTenant, assertRole } = require('./tenant');

const TENANT_COLLECTIONS = new Set([
  'projects','research','hypotheses','experiments','failures','ip','relationships','evidence'
]);

function scopedRecords(db, user, collection) {
  const records = db[collection] || [];
  if (!TENANT_COLLECTIONS.has(collection)) return records;
  return records.filter(record => tenantScope(user, record));
}

function assertRecordAccess(user, record) {
  return assertTenant(user, record);
}

function assertWriteAccess(user) {
  return assertRole(user, 'researcher');
}

module.exports = { TENANT_COLLECTIONS, scopedRecords, assertRecordAccess, assertWriteAccess };
