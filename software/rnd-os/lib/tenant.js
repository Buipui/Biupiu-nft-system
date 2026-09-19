const { can, validRole } = require('./auth');

function tenantScope(user, record) {
  return Boolean(user && record && user.organisationId && record.organisationId && user.organisationId === record.organisationId);
}

function assertTenant(user, record) {
  if (!tenantScope(user, record)) {
    const error = new Error('organisation scope violation');
    error.statusCode = 403;
    throw error;
  }
  return true;
}

function assertRole(user, minimumRole) {
  if (!user || !validRole(user.role) || !validRole(minimumRole) || !can(user.role, minimumRole)) {
    const error = new Error('insufficient role');
    error.statusCode = 403;
    throw error;
  }
  return true;
}

module.exports = { tenantScope, assertTenant, assertRole };
