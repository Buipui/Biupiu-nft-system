const { read, write } = require('../lib/store');
const { issueToken, validRole } = require('../lib/auth');
const { safeId } = require('../lib/api-security');

const db = read();
db.organisations ||= [];
db.users ||= [];
db.sessions ||= [];

let org = db.organisations.find(x => x.id === 'ORG-BIUPIU-DEV');
if (!org) {
  org = { id: 'ORG-BIUPIU-DEV', name: 'Biupiu Development Organisation', createdAt: new Date().toISOString() };
  db.organisations.push(org);
}

let user = db.users.find(x => x.id === 'USR-BIUPIU-DEV');
if (!user) {
  user = { id: 'USR-BIUPIU-DEV', organisationId: org.id, role: 'owner', name: 'Biupiu Development User' };
  db.users.push(user);
}
if (!validRole(user.role)) throw new Error('invalid development role');

const session = issueToken(user);
db.sessions = db.sessions.filter(s => Date.parse(s.expiresAt) > Date.now());
db.sessions.push({ id: safeId(), userId: session.userId, organisationId: session.organisationId, tokenHash: session.tokenHash, expiresAt: session.expiresAt, createdAt: new Date().toISOString() });
write(db);
console.log(JSON.stringify({ token: session.token, userId: user.id, organisationId: org.id, expiresAt: session.expiresAt }, null, 2));
