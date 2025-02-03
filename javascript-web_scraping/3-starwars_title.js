#!/usr/bin/node
const [, , URL] = process.argv;
require('request')(URL, (err, res, body) => {
  console.log(`code: ${res?.statusCode}`);
});
