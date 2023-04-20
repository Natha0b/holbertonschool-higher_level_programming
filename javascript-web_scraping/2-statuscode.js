#!/usr/bin/node
/*
script that display the status code of a GET request.
*/
const url = process.argv[2];
const https = require('https');

https.get(url, (response) => {
  console.log(`code: ${response.statusCode}`);
});
