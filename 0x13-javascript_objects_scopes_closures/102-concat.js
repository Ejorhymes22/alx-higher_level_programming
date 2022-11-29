#!/usr/bin/node
const fs = require('fs');
const args = process.argv;

fs.readFile(args[2], 'utf-8', (err, data) => {
  if (err) throw err;
  fs.writeFile(args[4], data, (err) => {
    if (err) throw err;
  });
});

fs.readFile(args[3], 'utf-8', (err, data) => {
  if (err) throw err;
  fs.appendFile(args[4], data, (err) => {
    if (err) throw err;
  });
});
