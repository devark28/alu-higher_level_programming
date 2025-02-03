#!/usr/bin/node
require('request')(`https://swapi-api.alx-tools.com/api/films/`, (err, res, body) => {
  console.log(JSON.parse(body)?.results?.reduce((count, film) => {
    return (film?.characters.find((ele) => ele.match(/.*\/18\/$/))) ? ++count : count;
  }, 0));
});
