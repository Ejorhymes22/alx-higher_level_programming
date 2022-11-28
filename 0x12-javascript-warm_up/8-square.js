#!/usr/bin/node
const a = parseInt(process.argv[2]);
if (Number.isInteger(a)) {
  for (let i = 0; i < a; i++) {
    let x = '';
    for (let j = 0; j < a; j++) {
      x += 'X';
    }
    console.log(x);
  }
} else {
  console.log('Missing size');
}
