#!/usr/bin/node
/* Function that returns the number of occurrences of an element in a list */

exports.nbOccurences = function (list, searchElement) {
    return list.filter(item => item === searchElement).length;
  };
  