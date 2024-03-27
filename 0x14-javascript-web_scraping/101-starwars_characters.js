#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(body);
  const characters = data.characters;

  const getData = async () => {
    for (const characterUrl of characters) {
      await new Promise((resolve, reject) => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            console.error(error);
            reject(error);
          }
          const data = JSON.parse(body);
          console.log(data.name);
          resolve();
        });
      });
    }
  };
  getData();
});
