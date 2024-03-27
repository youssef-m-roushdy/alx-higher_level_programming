#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }

  const completedTasksByUsers = {};
  const data = JSON.parse(body);

  data.forEach((user) => {
    const userId = user.userId;
    const completed = user.completed;
    if (completed && !completedTasksByUsers[userId]) {
      completedTasksByUsers[userId] = 0;
    }

    if (completed) {
      ++completedTasksByUsers[userId];
    }
  });

  console.log(completedTasksByUsers);
});
