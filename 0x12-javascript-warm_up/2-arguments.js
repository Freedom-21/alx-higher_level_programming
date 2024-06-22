#!/usr/bin/node

/**
 * Arguments in Js
 */

const noArg = 'No argument';
const singleArg = 'Argument found';
const multiArgs = 'Arguments found';

const { argv } = require('process');

const argNum = argv.length - 2;

if (argNum === 0) {
  console.log(noArg);
} else if (argNum === 1) {
  console.log(singleArg);
} else {
  console.log(multiArgs);
}
