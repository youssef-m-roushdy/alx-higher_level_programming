#!/usr/bin/node

const { argv } = require('process');

function add (a, b) {
  console.log(a + b);
}

add(Number.parseInt(argv[2]), Number.parseInt(argv[3]));
