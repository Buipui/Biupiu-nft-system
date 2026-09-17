const { authenticate, authorise } = require('./api-security');
const { tenantScope } = require('./tenant-store');

const PUBLIC_ROUTES = new Set(['/api/health','/api/meta']);

function routePolicy(pathname, method) {
  if (PUBLIC_ROUTES.has(pathname)) return { public: true };
  if (method === 'GET' && pathname === '/api/package/export') return { role: 'viewer' };
  if (method === 'GET') return { role: 'viewer' };
  if (method === 'POST') return { role: 'researcher' };
  return { role: 'researcher' };
}

function enforceApiGate(req, db) {
  const policy = routePolicy(new URL(req.url, 'http://localhost').pathname, req.method);
  if (policy.public) return null;
  const user = authenticate(req, db);
  authorise(user, policy.role);
  return user;
}

function assertTenantRecord(user, record) {
  if (!record || !tenantScope(user, record)) {
    const error = new Error('organisation scope violation');
    error.statusCode = 403;
    throw error;
  }
  return true;
}

module.exports = { PUBLIC_ROUTES, routePolicy, enforceApiGate, assertTenantRecord };
