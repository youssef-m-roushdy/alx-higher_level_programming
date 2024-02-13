#!/usr/bin/node

const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  charPrint (c) {
    for (let index = 0; index < this.height; index++) {
      console.log(
        c === undefined ? 'X'.repeat(this.width) : c.repeat(this.width)
      );
    }
  }
}

module.exports = Square;
