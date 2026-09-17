const crypto = require('node:crypto');
const { hashToken, can, validRole } = require('./auth');

function bearerToken(req) {
  const header = req.headers.authorization || '';
  const match = header.match(/^Bearer\s+(.+)$/i);
  return match ? match[1] : null;
}

function findSession(db, token) {
  if (!token) return null;
  const hash = hashToken(token);
  const sessions = db.sessions || [];
  const now = Date.now();
  return sessions.find(s => s.tokenHash === hash && Date.parse(s.expiresAt) > now) || null;
}

function authenticate(req, db) {
  const token = bearerToken(req);
  const session = findSession(db, token);
  if (!session) {
    const error = new Error('authentication required');
    error.statusCode = 401;
    throw error;
  }
  const user = (db.users || []).find(u => u.id === session.userId && u.organisationId === session.organisationId);
  if (!user || !validRole(user.role)) {
    const error = new Error('invalid authenticated principal');
    error.statusCode = 401;
    throw error;
  }
  return user;
}

function authorise(user, minimumRole) {
  if (!can(user.role, minimumRole)) {
    const error = new Error('insufficient role');
    error.statusCode = 403;
    throw error;
  }
  return true;
}

function safeId() {
  return crypto.randomBytes(12).toString('hex');
}

module.exports = { bearerToken, findSession, authenticate, authorise, safeId };
