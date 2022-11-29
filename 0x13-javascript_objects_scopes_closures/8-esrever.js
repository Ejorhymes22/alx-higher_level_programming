#!/usr/bin/node
exports.esrever = function (list) {
  let tmp;
  let end = list.length - 1;
  const j = list.length / 2;
  for (let i = 0; i < j; i++) {
    tmp = list[i];
    list[i] = list[end];
    list[end] = tmp;
    end--;
  }
  return (list);
};
