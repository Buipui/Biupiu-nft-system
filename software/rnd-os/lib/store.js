const fs = require('node:fs');
const path = require('node:path');

const DATA = path.join(__dirname, '..', 'data', 'db.json');
const DEFAULT = { organisations: [], users: [], projects: [], research: [], hypotheses: [], experiments: [], failures: [], ip: [], relationships: [], evidence: [], audit: [] };

function ensure() {
  fs.mkdirSync(path.dirname(DATA), { recursive: true });
  if (!fs.existsSync(DATA)) fs.writeFileSync(DATA, JSON.stringify(DEFAULT, null, 2));
}
function read() { ensure(); return JSON.parse(fs.readFileSync(DATA, 'utf8')); }
function write(value) { ensure(); fs.writeFileSync(DATA, JSON.stringify(value, null, 2)); return value; }
function collection(name) { const d = read(); d[name] ||= []; return d[name]; }

module.exports = { DATA, DEFAULT, ensure, read, write, collection };
