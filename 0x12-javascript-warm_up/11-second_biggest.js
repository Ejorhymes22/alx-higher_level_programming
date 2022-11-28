#!/usr/bin/node
const args = process.argv;
if (args.length <= 3) {
  console.log(0);
} else {
  let i;
  for (i of args) {
    let k = 0;
    for (let j = 0; j < args.length; j++) {
      if (parseInt(i) < parseInt(args[j])) {
        k += 1;
      }
      if (k > 1) {
        break;
      }
    }
    if (k === 1) {
      console.log(i);
      break;
    }
  }
}
