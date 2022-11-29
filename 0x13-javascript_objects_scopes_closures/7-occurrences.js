#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let k = 0;
  for (const num of list) {
    if (num === searchElement) {
      k += 1;
    }
  }
  return (k);
};
