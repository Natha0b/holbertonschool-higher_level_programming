#!/usr/bin/node
/*
script that prints
*/

const x = parseInt(process.argv[2]);

if (isNaN(x)) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < x) {
    let row = '';
    let j = 0;
    while (j < x) {
      row += 'X';
      j++;
    }
    console.log(row);
    i++;
  }
}
