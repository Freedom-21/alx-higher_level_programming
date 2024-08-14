#!/usr/bin/node
/* Class Square extends Rectangle with charPrint method */

const Square = require('./5-square');

class Square extends Rectangle {
  charPrint (c) {
    const char = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
}
module.exports = Square;
