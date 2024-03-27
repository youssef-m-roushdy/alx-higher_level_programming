#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(body);
  function getCharacter () {
    const charactersArr = [];
    data.results.forEach((obj) => {
      obj.characters.forEach((character) => {
        charactersArr.push(character);
      });
    });

    for (let i = 0; i < charactersArr.length; i++) {
      const id = charactersArr[i]
        .split('/')
        .filter((ele) => Number.parseInt(ele))
        .join();
      if (Number.parseInt(id) === 18) return charactersArr[i];
    }
  }
  const charURL = getCharacter();
  request(charURL, (error, response, body) => {
    if (error) {
      console.error(error);
    }
    const data = JSON.parse(body);
    console.log(data.films.length);
  });
});
