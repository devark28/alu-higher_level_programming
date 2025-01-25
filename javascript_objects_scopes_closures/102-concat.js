#!/usr/bin/node
const { dict } = require('./101-data');
console.log(Object.entries(dict).reduce((acc, [key, val]) => ({
  ...acc,
  [val]: acc[val]?.length ? acc[val].concat(key) : [key]
}), {}));
