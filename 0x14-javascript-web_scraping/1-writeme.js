#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];

const msg = process.argv[3];

fs.writeFile(filePath, msg, (err) => {
  if (err) {
    console.error(err);
  }
});
