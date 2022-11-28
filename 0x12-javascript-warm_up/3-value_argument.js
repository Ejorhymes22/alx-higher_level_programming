#!/usr/bin/node
const args = process.argv;
let k = 0;
let i;
for (i of args) {
  if (i === args[2]) {
    console.log(args[2]);
    k++;
  }
}
if (k === 0) { console.log('No argument'); }
