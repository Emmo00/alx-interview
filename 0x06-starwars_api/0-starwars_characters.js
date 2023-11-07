#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const apiURL = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request.get(apiURL, async (err, res, data) => {
  if (err) console.log(err);
  for (const character of JSON.parse(data).characters) {
    request.get(character, (error, res, data) => {
      if (error) console.log(error);
      console.log(JSON.parse(data).name);
    });
    await new Promise((resolve) => setTimeout(resolve, 200));
  }
});
