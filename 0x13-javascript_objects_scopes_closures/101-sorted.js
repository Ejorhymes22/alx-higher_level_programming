#!/usr/bin/node
const dict = require('./101-data').dict;
const val = Object.values(dict);
const newDict = {};
const valSet = new Set(val);
for (const key of valSet) {
  const arr = [];
  for (const num in dict) {
    if (key === dict[num]) {
      arr.push(num);
    }
  }
  newDict[key] = arr;
}

console.log(newDict);
