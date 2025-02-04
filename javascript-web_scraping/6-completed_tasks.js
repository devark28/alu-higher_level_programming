#!/usr/bin/node
const {logMe} = require("../javascript_objects_scopes_closures/9-logme");
const [, , URL] = process.argv;
require('request')(URL, (err, res, body) => {
  console.log(JSON.parse(body).reduce((acc, usr) => {
    return logMe({
      [usr?.userId]: (acc[usr?.userId] !== 0 ? acc[usr?.userId] + 1 : 0),
      ...acc
    });
  }, {}));
});
