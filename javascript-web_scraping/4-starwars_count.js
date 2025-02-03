#!/usr/bin/node
require('request')(`https://swapi-api.alx-tools.com/api/films/`, (err, res, body) => {
  console.log(JSON.parse(body).map((film) => {
    console.log(film);
  }));
});
