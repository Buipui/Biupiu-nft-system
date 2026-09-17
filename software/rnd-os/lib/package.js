const crypto = require('node:crypto');
const fs = require('node:fs');
const path = require('node:path');

function exportPackage(db) {
  const payload = { format: 'biupiu-rnd-package', version: '0.2.0', exportedAt: new Date().toISOString(), data: db };
  const canonical = JSON.stringify(payload.data);
  payload.checksum = crypto.createHash('sha256').update(canonical).digest('hex');
  return payload;
}
function importPackage(pkg) {
  if (!pkg || pkg.format !== 'biupiu-rnd-package' || !pkg.data) throw new Error('invalid research package');
  const checksum = crypto.createHash('sha256').update(JSON.stringify(pkg.data)).digest('hex');
  if (pkg.checksum && pkg.checksum !== checksum) throw new Error('research package checksum mismatch');
  return pkg.data;
}
function writePackage(file, db) { fs.writeFileSync(file, JSON.stringify(exportPackage(db), null, 2)); return path.resolve(file); }

module.exports = { exportPackage, importPackage, writePackage };
