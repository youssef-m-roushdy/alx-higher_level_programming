#!/usr/bin/node

const { argv } = require('process');

if (isNaN(Number.parseInt(argv[2]))) {
  console.log('Missing size');
} else {
  for (let index = 0; index < Number.parseInt(argv[2]); index++) {
    console.log('X'.repeat(Number.parseInt(argv[2])));
  }
}
