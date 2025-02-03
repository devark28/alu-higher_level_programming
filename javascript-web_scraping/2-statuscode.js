#!/usr/bin/node
const [, , fileA, contentA] = process.argv;
require('request').writeFileSync(fileA, contentA, {encoding: 'utf-8'});
