function recordSecurityEvent(db, event) {
  db.audit ||= [];
  db.audit.push({
    id: event.id || require('node:crypto').randomBytes(12).toString('hex'),
    timestamp: new Date().toISOString(),
    action: event.action || 'SECURITY_EVENT',
    entity: event.entity || 'api',
    entityId: event.entityId || null,
    payload: {
      method: event.method,
      path: event.path,
      userId: event.userId || null,
      organisationId: event.organisationId || null,
      outcome: event.outcome || 'unknown'
    }
  });
}

module.exports = { recordSecurityEvent };
