#!/usr/bin/node
require('request')(`https://swapi-api.alx-tools.com/api/films/`, (err, res, body) => {
  console.log(JSON.parse(body)?.results?.reduce((count, film) => {
    if(film?.characters.find((ele) => ele.match(/.*\/18\/$/))){
      return ++count;
    }
    // console.log(film?.characters);
    return count;
  }, 0));
});
