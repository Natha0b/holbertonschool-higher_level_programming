#!/usr/bin/node
/*
class Rectangle that defines a rectangle
*/
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
