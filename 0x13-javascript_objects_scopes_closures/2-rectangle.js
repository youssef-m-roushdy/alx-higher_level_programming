#!/usr/bin/node

class Rectangle {
  constructor (width, height) {
    if (width <= 0 || height <= 0 || isNaN(width) || isNaN(height)) {
      return;
    }
    this.width = width;
    this.height = height;
  }
}

module.exports = Rectangle;
