#!/usr/bin/node
const [, , fileA] = process.argv;
require('fs').readFileSync(fileA,{encoding:'utf-8'});
