#!/usr/bin/node
const [, , URL] = process.argv;
require('request')(URL, (err, res, body) => {
  console.log(JSON.parse(body).reduce((acc, usr) => {
    return {[usr?.id]: (acc[usr?.id] || 0) + 1, ...acc};
  }, {}));
});
