#!/usr/bin/node
const dict = require('./101-data').dict
let val = Object.values(dict);
const newDict = {};
const valSet = new Set(val);
for (const key of valSet) {
	arr = [];
	for (const num in dict) {
		if (key === dict[num]) {
			arr.push(num);
		}
	}
	newDict[key] = arr;
}

console.log(newDict);
/*
const values = Object.values(dict);
//valSet = new Set(values);
console.log(values);

const entry = Object.entries(dict);
console.log(entry);
*/
