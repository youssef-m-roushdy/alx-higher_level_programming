#!/usr/bin/node

const { argv } = require('process');

if (isNaN(Number.parseInt(argv[2], 10))) {
  console.log(1);
} else {
  function fact (num) {
    if (num === 1 || num === 0) {
      return 1;
    }
    const factor = num * fact(num - 1);
    return factor;
  }

  console.log(fact(Number.parseInt(argv[2], 10)));
}
