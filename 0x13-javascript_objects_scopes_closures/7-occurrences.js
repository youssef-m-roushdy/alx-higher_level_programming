#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let rep = 0;
  list.forEach((e) => {
    if (e === searchElement) {
      rep++;
    }
  });
  return rep;
};
