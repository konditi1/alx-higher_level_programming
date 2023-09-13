#!/usr/bin/node
const { list } = require('./100-data.js');
const newList = list.map((x) => x * list.indexOf(x));
console.log(list);
console.log(newList);
