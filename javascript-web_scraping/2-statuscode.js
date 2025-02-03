#!/usr/bin/node
const [, , URL] = process.argv;
console.log(require('request')());
