#!/usr/bin/node
const [, , id] = process.argv;
const request = require('request');
request(`https://swapi-api.alx-tools.com/api/films/${id}`, (err, res, body) => {
  console.log(JSON.parse(body)?.title);
});
