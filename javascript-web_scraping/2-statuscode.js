#!/usr/bin/node
const [, , URL] = process.argv;
const request = require('request');
request(URL, (err, res, body) => {
  console.log(`code: ${res?.statusCode}`);
});
