#!/usr/bin/node
require('request')(`https://swapi-api.alx-tools.com/api/films/`, (err, res, body) => {
  console.log(JSON.parse(body)?.results?.map((film) => {
    console.log(film);
  }));
});
