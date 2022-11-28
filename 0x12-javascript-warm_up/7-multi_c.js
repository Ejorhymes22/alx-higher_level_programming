#!/usr/bin/node
const args = process.argv;
const len = parseInt(args[2]);
if (Number.isInteger(len)) {
  for (let i = 0; i < len; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
