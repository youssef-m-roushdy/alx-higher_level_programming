#!/usr/bin/node

class Rectangle {
  constructor (width, height) {
    if (width <= 0 || height <= 0 || isNaN(width) || isNaN(height)) {
      return;
    }
    this.width = width;
    this.height = height;
  }

  print () {
    for (let index = 0; index < this.height; index++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
