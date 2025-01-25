#!/usr/bin/node
const [, , fileA, fileB, fileC] = process.argv;
const fileAData = require(`./${fileA}`);
const fileBData = require(`./${fileB}`);
require('fs').writeFileSync(fileC, JSON.stringify({ ...fileAData, ...fileBData }));
