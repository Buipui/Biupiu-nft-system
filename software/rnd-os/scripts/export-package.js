const path = require('node:path');
const { read } = require('../lib/store');
const { writePackage } = require('../lib/package');

const target = process.argv[2] || path.join(__dirname, '..', 'data', `rnd-package-${new Date().toISOString().slice(0,10)}.json`);
console.log(`Exported research package: ${writePackage(target, read())}`);
