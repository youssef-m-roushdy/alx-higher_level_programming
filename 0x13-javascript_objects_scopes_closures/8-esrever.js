#!/usr/bin/node

exports.esrever = function (list) {
  const reversed = [];
  list.forEach((e) => {
    reversed.unshift(e);
  });
  return reversed;
};
