#!/usr/bin/node
const [, , URL, fileA] = process.argv;
require('request')(URL, (err, res, body) => {
  require('fs').writeFileSync(fileA, body, { encoding: 'utf-8' });
});
