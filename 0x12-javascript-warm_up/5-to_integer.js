#!/usr/bin/node

/*
Script that prints My number: <first argument converted to an integer>
*/

const arg = process.argv[2];
const num = parseInt(arg);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
