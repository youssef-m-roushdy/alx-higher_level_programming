#!/usr/bin/node

const { argv } = require('process');

if (isNaN(Number.parseInt(argv[2]))) {
  console.log('Not a number');
} else {
  console.log(Number.parseInt(argv[2]));
}
