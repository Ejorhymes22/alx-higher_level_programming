#!/usr/bin/node
const a = process.argv[2];
let b = parseInt(a);
function recFactorial (a) {
  if (a === 1) {
    return (1);
  }
  return (a * recFactorial(a - 1));
}

if (Number.isInteger(b)) {
  let result;
  if (b === 0) {
    console.log(1);
  }
  if (b < 0) {
    b = b * (-1);
    result = recFactorial(b);
    result = result * (-1);
    console.log(result);
  } else if (b > 0) {
    result = recFactorial(b);
    console.log(result);
  }
} else {
  console.log(1);
}
