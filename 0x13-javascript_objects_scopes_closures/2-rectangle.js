#!/usr/bin/node
/* Class Rectangle with constructor and validation */

class Rectangle {
    constructor (w, h) {
      if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
      }
    }
  }
  module.exports = Rectangle;
  