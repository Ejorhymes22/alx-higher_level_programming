#!/usr/bin/node
exports.esrever = function (list) {
	let tmp;
	end = list.length - 1;
	j = list.length / 2;
	for (let i = 0; i < j; i++){
		tmp = list[i];
		list[i] = list[end];
		list[end] = tmp;
		end--;
	}
	return (list);
}
