#!/usr/bin/node
const fs = require('fs');
const myArgs = process.argv.slice(2);
fs.writeFile(myArgs[0], myArgs[1], function (err) {
  if (err) {
    console.log(err);
  }
});
