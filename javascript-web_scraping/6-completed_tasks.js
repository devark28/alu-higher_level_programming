#!/usr/bin/node
const [, , URL] = process.argv;
require('request')(URL, (err, res, body) => {
  console.log(JSON.parse(body));
  //   .reduce((acc, usr) => {
  //   return console.log({
  //     [usr?.userId]: (acc[usr?.userId] !== 0 ? acc[usr?.userId] + 1 : 0),
  //     ...acc
  //   });
  // }, {})
});
