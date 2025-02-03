#!/usr/bin/node
const [, , id] = process.argv;
require('request')(`https://swapi-api.alx-tools.com/api/films/${id}`, (err, res, body) => {
  console.log(body);
});
