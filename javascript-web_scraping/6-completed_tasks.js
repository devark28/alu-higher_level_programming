const [, , URL] = process.argv;
require('request')(URL, (err, res, body) => {
  console.log(JSON.parse(body));
});