#!/usr/bin/node
/*
script that display the status code of a GET request.
*/
const request = require('request');
const { argv } = require('process');

request(argv[2], (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
