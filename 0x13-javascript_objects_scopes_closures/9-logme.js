#!/usr/bin/node
let counter = 0;
logMe = function (item) {
  console.log(counter + ': ' + item);
  counter++;
};
