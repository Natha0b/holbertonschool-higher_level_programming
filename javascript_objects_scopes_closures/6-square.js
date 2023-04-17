#!/usr/bin/node
/*
class Square that defines a square and inherits from Square
*/
const Square = require('./5-square.js');

module.exports = class Squarec extends Square {
  charPrint (c = 'X') {
    let row = '';
    for (let i = 0; i < this.width; i++) {
      row += c;
    }
    for (let j = 0; j < this.height; j++) {
      console.log(row);
    }
  }
};
