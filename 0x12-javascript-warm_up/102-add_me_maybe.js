#!/usr/bin/node

/*
Function that increments a number and then calls a function
*/

exports.addMeMaybe = function (number, theFunction) {
    number++;
    theFunction(number);
  };
  