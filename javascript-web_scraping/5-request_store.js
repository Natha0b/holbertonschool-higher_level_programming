#!/usr/bin/node
/*
script that gets the contents of a webpage
and stores it in a file.
*/
const fs = require('fs');
const request = require('request');
const { argv } = require('process');

request(argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(argv[3], body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
