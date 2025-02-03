#!/usr/bin/node
const [, , URL] = process.argv;
require('request').get(URL);
