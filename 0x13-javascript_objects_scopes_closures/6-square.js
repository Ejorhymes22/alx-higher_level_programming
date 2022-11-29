#!/usr/bin/node
const Square0 = require('./5-square');

class Square extends Square0 {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        let k = '';
        for (let j = 0; j < this.width; j++) {
          k += c;
        }
        console.log(k);
      }
    } else {
      super.print();
    }
  }
}

module.exports = Square;
