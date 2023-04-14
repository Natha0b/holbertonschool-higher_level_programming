#!/usr/bin/node
/*
script that prints
*/

const { argv } = require('process');
const num1 = parseInt(argv[2]);
const num2 = parseInt(argv[3]);

function add (a, b) {
  if (arguments.length < 2 || typeof a !== 'number' || typeof b !== 'number') {
    console.log('NaN');
  } else {
    return a + b;
  }
}
console.log(add(num1, num2));
