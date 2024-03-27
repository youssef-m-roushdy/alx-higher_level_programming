#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const completedTasksByUsers = {};
  const data = JSON.parse(body);
  console.log(data);
  data.forEach((user) => {
    if (user.completed && !completedTasksByUsers[user.userId]) {
      completedTasksByUsers[user.userId] = 0;
    }

    if (user.completed) {
      ++completedTasksByUsers[user.userId];
    }
  });
  console.log(completedTasksByUsers);
});
