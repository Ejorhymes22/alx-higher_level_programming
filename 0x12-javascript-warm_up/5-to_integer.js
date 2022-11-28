#!/usr/bin/node
const args = process.argv;
const a = parseInt(args[2]);
if (Number.isInteger(a)) {
  console.log('My number: ' + a);
} else {
  console.log('Not a number');
}
