const crypto = require('node:crypto');

const ROLES = Object.freeze(['owner','admin','research_lead','researcher','reviewer','viewer']);
const ROLE_RANK = Object.freeze({ owner: 60, admin: 50, research_lead: 40, researcher: 30, reviewer: 20, viewer: 10 });

function hashToken(token) { return crypto.createHash('sha256').update(String(token)).digest('hex'); }
function issueToken(user) {
  const raw = crypto.randomBytes(24).toString('hex');
  return { token: raw, tokenHash: hashToken(raw), userId: user.id, organisationId: user.organisationId, expiresAt: new Date(Date.now() + 8 * 60 * 60 * 1000).toISOString() };
}
function can(role, minimum) { return (ROLE_RANK[role] || 0) >= (ROLE_RANK[minimum] || Infinity); }
function validRole(role) { return ROLES.includes(role); }

module.exports = { ROLES, hashToken, issueToken, can, validRole };
