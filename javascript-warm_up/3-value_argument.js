#!/usr/bin/node
/*
script that prints
*/

const arg = process.argv[2];

if (arg) {
  console.log(arg);
} else {
  console.log('No argument');
}
