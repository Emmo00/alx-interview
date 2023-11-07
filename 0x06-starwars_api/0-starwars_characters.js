#!/usr/bin/node
const request = require("request");

const filmId = process.argv[2];

request(
  `https://swapi-api.alx-tools.com/api/films/${filmId}`,
  function (error, response, body) {
    if (error) console.error(error);

    const data = JSON.parse(body);
    characterIds = data.characters.map((url) => Number(url.split("/").at(-2)));
    characterIds
      .sort((a, b) => a - b)
      .forEach((id) =>
        request(
          `https://swapi-api.alx-tools.com/api/people/${id}`,
          (error, res, character) => {
            if (error) console.error(error);
            console.log(JSON.parse(character).name);
          }
        )
      );
  }
);
