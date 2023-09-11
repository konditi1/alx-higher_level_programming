#!/usr/bin/node
const args = process.argv;
const parsedInt = parseInt(args[2]);
if (!isNaN(parsedInt)) {
  console.log('My number: ' + parsedInt);
} else {
  console.log('Not a number');
}
