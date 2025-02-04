#!/usr/bin/node
const [, , URL] = process.argv;
require('request')(URL, (err, res, body) => {
  console.log(JSON.parse(body).reduce((acc, usr) => {
    return {[usr?.userId]: (acc[usr?.userId] ? acc[usr?.userId] + 1 : 1), ...acc};
  }, {}));
});
