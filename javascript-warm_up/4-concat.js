#!/usr/bin/node
/*
script that prints
*/
const arg1 = process.argv[2];
const arg2 = process.argv[3];

if (arg1 && arg2) {
  console.log(`${arg1} is ${arg2}`);
} else if (arg1) {
  console.log(`${arg1} is undefined`);
} else {
  console.log('undefined is undefined');
}
