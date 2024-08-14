#!/usr/bin/node

/* Script that prints all characters of a Star Wars movie in the order of appearance */

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const characters = data.characters;
    printCharacters(characters, 0);
  }
});

function printCharacters (characters, index) {
  if (index >= characters.length) return;
  request(characters[index], (err, res, charBody) => {
    if (err) {
      console.log(err);
    } else {
      const character = JSON.parse(charBody);
      console.log(character.name);
      printCharacters(characters, index + 1);
    }
  });
}
