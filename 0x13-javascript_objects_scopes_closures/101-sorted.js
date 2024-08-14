#!/usr/bin/node
/* Script that imports a dictionary and computes a new dictionary of user ids by occurrence */

const dict = require('./101-data').dict;
const newDict = {};
for (const key in dict) {
  if (newDict[dict[key]] === undefined) {
    newDict[dict[key]] = [];
  }
  newDict[dict[key]].push(key);
}
console.log(newDict);
