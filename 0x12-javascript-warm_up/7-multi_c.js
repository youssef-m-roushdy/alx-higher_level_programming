#!/usr/bin/node

const { argv } = require('process');

const x = 'C is fun';

for (let index = 0; index < Number.parseInt(argv[2]); index++) {
  console.log(x);
}
