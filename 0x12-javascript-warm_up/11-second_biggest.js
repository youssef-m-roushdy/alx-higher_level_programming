#!/usr/bin/node

const { argv } = require('process');

if (argv.length === 3) {
  console.log(0);
} else {
  const arr = [];
  argv.forEach(e => {
    if (!isNaN(Number.parseInt(e))) {
      arr.push(Number.parseInt(e));
    }
  });
  arr.sort();
  console.log(arr[1]);
}
