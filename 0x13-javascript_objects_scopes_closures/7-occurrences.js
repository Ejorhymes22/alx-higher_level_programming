#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
	let k = 0;
	for (let num of list){
		if (num === searchElement){
			k += 1;
		}
	}
	return (k);
}
