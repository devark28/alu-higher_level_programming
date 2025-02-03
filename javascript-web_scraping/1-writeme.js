#!/usr/bin/node
const [, , fileA, contentA] = process.argv;
require('fs').readFileSync(fileA,{encoding:'utf-8'});
