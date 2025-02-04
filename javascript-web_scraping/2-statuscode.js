#!/usr/bin/node
const [, , URL] = process.argv;
require('request')(URL, (err, res) => {
  console.log(`code: ${res?.statusCode}`);
});
