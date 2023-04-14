#!/usr/bin/node
/*
script that prints
*/

const args = process.argv.slice(2).map(Number);
let max = -Infinity;
let secondMax = -Infinity;

for (let i = 0; i < args.length; i++) {
  const num = args[i];
  if (num > max) {
    secondMax = max;
    max = num;
  } else if (num > secondMax && num < max) {
    secondMax = num;
  }
}

if (args.length < 2) {
  console.log(0);
} else if (args.length === 1) {
  console.log(0);
} else {
  console.log(secondMax);
}
