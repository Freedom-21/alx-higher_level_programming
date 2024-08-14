#!/usr/bin/node

/* Script that prints the number of movies where the character “Wedge Antilles” is present */

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const films = data.results;
    const wedgeCount = films.filter(film =>
      film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
    ).length;
    console.log(wedgeCount);
  }
});
