#!/usr/bin/node
const [, , URL, fileA] = process.argv;
require('request')(URL, (_, _, body) => {
  require('fs').writeFileSync(fileA, body, { encoding: 'utf-8' });
});
